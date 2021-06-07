import config as cfg
import pandas as pd

"""helper functions and other stuff not related to static hardcoded data"""

def get_rsi_clmn_name(vw_name):
    return cfg.UNUSUAL_RSI_CLMN_NAME.get(vw_name, 'roche_specimen_id')

def get_mdh_tb_pref(vw_name):
    return cfg.MDH_TABLE_PREFIX.get(vw_name, vw_name)

def assert_df_equal(df1,df2):
    check = df1.equals(df2)
    return check