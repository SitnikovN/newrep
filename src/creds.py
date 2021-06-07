"""Credentials store"""

"""MDH creds"""

CONN_PARAMS_QUASAR = {
        'method': 'odbc',
        'system': 'google.ind.com',
        'DSN': 'mdh_prd',
        'username': 'userprod',
        'password': 'Nevada2018',
        'autoCommit': False
    }

"""cygnus_tst creds"""
###
CONN_PARAMS_CYGNUS_TST = {
                'dbname':'postgres',
                'user' : 'my_user',
                'password':'pass',
                'host':'my_host',
                'port' : 5432
                        }

"""redshift creds"""
###


