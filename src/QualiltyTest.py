import db_clients as dc
import config as cfg
import creds
import pandas as pd
import test_helper as th

class TestTeradataCygnus():
    def __init__(self,vw_name,mdh_tbl_mask = cfg.MDH_DEFAULT_TBL_MASK):
        self.CygClient = dc.PostgreClient(creds.CONN_PARAMS_CYGNUS_TST)
        self.TrdClient = dc.TeradataClient(creds.CONN_PARAMS_QUASAR)

        self._vw_name = vw_name
        self._trd_obj,self._cyg_obj = map(lambda tbl_pref,vw_name: tbl_pref + vw_name,
                                            [cfg.MDH_DEFAULT_TBL_PREFIX,cfg.CYGNUS_DEFAULT_TBL_PREFIX],
                                          [mdh_tbl_mask.format(th.get_mdh_tb_pref(self._vw_name)),
                                            '.v_bodi_{}'.format(self._vw_name)
                                           ]
                                          )
        self._base_column = th.get_rsi_clmn_name(self._vw_name)

    def prepare_test_dataframes(self,sql_const,query_params_cyg,query_params_mdh):

        cygnus_sql = sql_const.format(**query_params_cyg)
        mdh_sql = sql_const.format(**query_params_mdh)

        df_mdh = self.TrdClient.dump_df(mdh_sql)
        mdh_columns = df_mdh.columns.values
        df_cygnus = self.CygClient.dump_df(cygnus_sql, mdh_columns)

        return df_mdh,df_cygnus

    def run_quality_test(self):
        """Finding RSI's with equal number of returned rows"""
        cygnus_params = {'base_clmn' : self._base_column, 'obj' : self._cyg_obj}
        mdh_params = {'base_clmn': self._base_column, 'obj' : self._trd_obj}

        df_mdh,df_cygnus = self.prepare_test_dataframes(cfg.SQL_GROUP_BY_ENTITY,
                                               query_params_cyg=cygnus_params,
                                               query_params_mdh=mdh_params
                                               )

        df_mdh.cnt = df_mdh.cnt.astype(int)
        df_joined_rsi = pd.merge(df_mdh, df_cygnus, how='inner', on=['base_clmn', 'cnt'],
                                 indicator='found')

        rsi_lst = df_joined_rsi['base_clmn'].iloc[:3].tolist()

        for rsi in rsi_lst:
            print('Testing RSI : {}'.format(rsi))
            cygnus_rsi_params = {'base_clmn': self._base_column, 'obj': self._cyg_obj,'val' : rsi}
            mdh_rsi_params =  {'base_clmn': self._base_column, 'obj': self._trd_obj,'val' : rsi}

            df_mdh_rsi, df_cygnus_rsi = self.prepare_test_dataframes(cfg.SQL_ALL_COLUMNS_FILTERED,
                                                             query_params_cyg=cygnus_rsi_params,
                                                             query_params_mdh=mdh_rsi_params
                                                             )
            clmn_list = df_mdh_rsi.columns.tolist()
            for clmn in clmn_list:

                df_distcnt_cyg = df_cygnus_rsi[clmn].agg(['nunique', 'count', 'size']).to_frame()
                df_distcnt_mdh = df_mdh_rsi[clmn].agg(['nunique', 'count', 'size']).to_frame()
                if not th.assert_df_equal(df_distcnt_mdh, df_distcnt_cyg):
                    df_joined = df_distcnt_mdh.join(df_distcnt_cyg,
                                                    lsuffix='_mdh',
                                                    rsuffix='_cygnus',
                                                    how='inner')
                    #filename = 'Smoke_Test_Results\\v_{}_{}.csv'.format(i, rsi)
                    #df_joined.to_csv(filename, header=True, mode='a')
                    print(df_joined)

        self.CygClient.kill()
        self.TrdClient.kill()


test = TestTeradataCygnus('1182')
test.run_quality_test()