import db_client_abc as dca
import pandas as pd
import config as cfg
import creds

class PostgreClient(dca.DBClient):
    def __init__(self, con_params):
        import psycopg2 as ps
        try:
            self.con = ps.connect(**con_params)
            self.cursor = self.con.cursor()
            print('Connected to the Postgres server')

        except ps.Error as e:
            print('Failed to connect to the Postgres server')
            print(e.pgerror)
            exit(1)

    def select_data(self,sql_stmt):
        self.cursor.execute(sql_stmt)
        data = []
        for x in self.cursor:
            data.append(x)
        return data

    def dump_df(self,sql_stmt,column_lst):
        data_to_dump  = self.select_data(sql_stmt)
        df = pd.DataFrame.from_records(data_to_dump, columns=column_lst)
        return df

    def kill(self):
        self.con.close()
        print('Connection has been closed')

class TeradataClient(dca.DBClient):
    def __init__(self,con_params):
        import teradata
        try:
            self.con = cfg.UDAExec.connect(**con_params)
            print('Connected to the Teradata server')

        except:
            print('Failed to connect to the server')
            exit(1)
            
    def select_data(self,sql_stmt):
        res = self.con.execute(sql_stmt)
        if res.rowcount == 0:
            return []
        else:
            columnNames = []
            for col in res.description:
                columnNames.append(col[0])
            testlist = []
            for row in res:
                testlist.append(dict(zip(columnNames, row)))
            return testlist

    def dump_df(self,sql_stmt):
        df = pd.read_sql(sql_stmt, self.con)
        return df

    def kill(self):
        self.con.close()
        print('Connection has been closed')

