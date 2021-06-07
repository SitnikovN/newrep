from pyspark.sql import SparkSession
from pyspark.sql.functions import concat_ws

def top1_country_booked_hotel_same_loc(df):
   df_agg = df.filter('is_booking = 1 and user_location_country = hotel_country').\
        groupBy('hotel_country').\
        count().\
        orderBy('count',ascending=0).\
        limit(1).\
        withColumnRenamed('hotel_country','country')
   return df_agg

def top3_hotels_between_couples(df):
    df_agg = df.withColumn('hotel',concat_ws('_','hotel_continent','hotel_country','hotel_market')).\
        filter('srch_adults_cnt = 2').\
        groupBy('hotel').\
        count().\
        orderBy('count',ascending=0).\
        limit(3)
    return df_agg

def top3_srch_hotel_between_couples_with_chldrn(df):
    df_agg = df.withColumn('hotel',concat_ws('_','hotel_continent','hotel_country','hotel_market')).\
         filter('srch_adults_cnt = 2  and srch_children_cnt > 0 and is_booking = 0').\
           groupBy('hotel').\
           count().\
           orderBy('count',ascending=0).\
           limit(3)
    return  df_agg


if __name__ == "__main__":
    spark = SparkSession.builder.master('local').appName('test').getOrCreate()
    df = spark.read.load(
        'hdfs://test-bigdata.us-central1-a.c.bigdatalearn-274318.internal/user/input_files/train/train.csv',
        format='csv', sep=',', header='true')
    print('Top 3 hotels between couples:\n',
            top3_hotels_between_couples(df).collect(),'\n---------------')
    print('Most popular country where hotels are booked and searched from the same country is:\n',
            top1_country_booked_hotel_same_loc(df).collect(),'\n---------------')
    print('Top 3 non-booked hotels between couples with children:\n',
            top3_srch_hotel_between_couples_with_chldrn(df).collect())

