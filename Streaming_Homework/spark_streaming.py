from pyspark.sql import SparkSession, column
from pyspark.sql.functions import *
from pyspark.sql.types import StructType, StructField, DoubleType, StringType,IntegerType,BooleanType

spark = SparkSession.builder.appName('firstStream').getOrCreate()

schema = StructType([
    StructField('date_time',StringType()),
    StructField('site_name', IntegerType()),
    StructField('posa_continent', IntegerType()),
    StructField('user_location_country', IntegerType()),
    StructField('user_location_region', IntegerType()),
    StructField('user_location_city', IntegerType()),
    StructField('orig_destination_distance', DoubleType()),
    StructField('user_id', IntegerType()),
    StructField('is_mobile', IntegerType()),
    StructField('is_package', IntegerType()),
    StructField('channel', IntegerType()),
    StructField('srch_ci', StringType()),
    StructField('srch_co', StringType()),
    StructField('srch_adults_cnt', IntegerType()),
    StructField('srch_children_cnt', IntegerType()),
    StructField('srch_rm_cnt', IntegerType()),
    StructField('srch_destination_id', IntegerType()),
    StructField('srch_destination_type_id', IntegerType()),
    StructField('hotel_continent', IntegerType()),
    StructField('hotel_country', IntegerType()),
    StructField('hotel_market', IntegerType()),
    StructField('is_booking', BooleanType()),
    StructField('cnt', IntegerType()),
    StructField('hotel_cluster', IntegerType())
]
)

df = spark.readStream.format('kafka')\
    .option('kafka.bootstrap.servers','test-bigdata.us-central1-a.c.bigdatalearn-274318.internal:6667')\
    .option('subscribe','test')\
    .load()\
    .withColumn('value',from_json(column('value').cast('string'),schema))

data = df.select(
        'value.date_time',
        'value.site_name',
        'value.posa_continent',
        'value.user_location_country',
        'value.user_location_region',
        'value.user_location_city',
        'value.orig_destination_distance',
        'value.user_id',
        'value.is_mobile',
        'value.is_package',
        'value.channel',
        'value.srch_ci',
        'value.srch_co',
        'value.srch_adults_cnt',
        'value.srch_children_cnt',
        'value.srch_rm_cnt',
        'value.srch_destination_id',
        'value.srch_destination_type_id',
        'value.hotel_continent',
        'value.hotel_country',
        'value.hotel_market',
        'value.is_booking',
        'value.cnt',
        'value.hotel_cluster'
            )
df_stream = data\
        .writeStream\
        .format('csv')\
        .trigger(processingTime='20 seconds') \
        .option("path", '/files/') \
        .option("checkpointLocation", 'files/chck/') \
        .outputMode('append') \
        .start()\
        .awaitTermination()
