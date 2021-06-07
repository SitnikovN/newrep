from abc import ABC, abstractmethod

class DBClient(ABC):

    @abstractmethod
    def select_data(self,sql_stmt):
        """selecting data from database and saving it to built-in Python data structures """
        pass

    def dump_df(self,sql_stmt):
        """dumping data into pandas dataframe """
        pass

    def insert_data(self,tbl_pref,tbl_name,columns = None,*values):
        """insert data into a table"""
        pass

    def kill(self):
        """close connection to the database"""