"""Config / Helper data structures"""
import teradata

#edit it to clmn_name:[vw1,vw2,vw3] structure?
UNUSUAL_RSI_CLMN_NAME = {
    'co41101': '"RRID"',
    '1124': '"RRID"',
    '1209': '"RRID"',
    '1194': '"RRID"', ''
    '64a': '"RRID"',
    '1182': '"RRID"',
    '24': '"Roche Specimen ID"',
    '136': '"Roche Specimen ID"',
    '138': '"Roche Specimen ID"',
    '1217': '"Accession Number"',
    '135a': '"Accession Number"',
    '176': '"Accession.Number"',
    '1209': '"RRID"',
    '103a': '"screening_number"',
    '95a': '"screening_number"',
    '71': 'scrn',
    '10': '"ROCHE_SPECIMEN_ID"',
    '70': 'q2s_roche_specimen_id',
    '1046': '"Accession.Number"',
    '135': '"Accession.Number"',
    'wo41554': 'hgx_roche_specimen_id',
    '86': '"ROCHE_SPECIMEN_ID"',
    '61': '"BOMREFID"'
}

MDH_TABLE_PREFIX = {
            'co41101': '_co41101',
            'go41717': '_GO41717',
            'wo41554':'_WO41554',
            'co41012': '_co41012',
            'ga41003': '_ga41003',
            'go39775':'_go39775',
            'go41582':'_go41582'
            }

#select for grouping rows by base column
SQL_GROUP_BY_ENTITY = """
            select {base_clmn} as base_clmn,
                count(*) cnt
            from {obj}
            group by {base_clmn}
        """

SQL_ALL_COLUMNS_FILTERED = """
            select * 
            from {obj}
            where {base_clmn} = '{val}' 
      """

UDAExec = teradata.UdaExec(appName='TdiToMdh',
                               version=1.0,
                               configureLogging=False)

MDH_DEFAULT_TBL_PREFIX = 'BODI_Project_Pub'
CYGNUS_DEFAULT_TBL_PREFIX = 'cygnus_pub_tst'

MDH_DEFAULT_TBL_MASK = '.BODI{}'