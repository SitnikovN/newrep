from sparktestingbase.sqltestcase import SQLTestCase
from pyspark.sql.types import StructType

class SparkSqlTestCase(SQLTestCase):
    #overriding to create an actual Spark session
    def setUp(self):
        try:
            from pyspark.sql import SparkSession
            self.session = SparkSession.builder.master('local').appName('test').getOrCreate()
            self.sqlCtx = self.session._wrapped
        except Exception:
            from pyspark.sql import SQLContext
            self.sqlCtx = SQLContext(self.sc)

    #To align test dataframe nullable column values with the expected one
    def schema_nullable_helper(self, df, expected_schema, fields=None):
        new_schema = []
        current_schema = df.schema
        if not fields:
            fields = df.columns

        for item in current_schema:
            if item.name in fields:
                for expected_item in expected_schema:
                    if expected_item.name == item.name:
                        item.nullable = expected_item.nullable
            new_schema.append(item)

        new_schema = StructType(new_schema)
        df = self.session.createDataFrame(
            df.rdd, schema=new_schema
        )
        return df