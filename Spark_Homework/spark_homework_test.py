from spark_homework import *
from sparkSQLTestCase import SparkSqlTestCase
import unittest2


class TestSparkHomeWork(SparkSqlTestCase):
    def setUp(self):
        super(TestSparkHomeWork,self).setUp()

    def compare_dataframes(self,result_df,expected_data,expected_sch):
        expected_df = self.session.createDataFrame(expected_data,expected_sch)
        result_df = self.schema_nullable_helper(result_df,expected_df.schema)
        self.assertDataFrameEqual(expected_df,result_df)

    def test_top1_country_booked_hotel_same_loc(self):
        init_schema = ['is_booking', 'user_location_country', 'hotel_country']
        init_data = [(1, 101, 101), (0, 201, 301), (1, 101, 101), (1, 201, 101), (1, 401, 401)]
        exp_schema = ['country','count']
        exp_data = [(101,2)]

        initial_df = self.session.createDataFrame(init_data, init_schema)
        result_df = top1_country_booked_hotel_same_loc(initial_df)

        self.compare_dataframes(result_df,exp_data,exp_schema)

    def test_top3_hotels_between_couples(self):
        init_schema_1 = ['hotel_continent', 'hotel_country','hotel_market','srch_adults_cnt']
        init_data_1 = [
                    (1000, 101, 10,2),
                    (1000, 101, 10,2),
                    (1000, 101, 10,2),
                    (2000, 101, 10,2),
                    (2000, 101, 10,2),
                    (2000, 101, 30,1),
                    (1000, 301, 30, 2),
                    (1000, 301, 30, 2),
                    (1000, 301, 30, 2),
                    (1000, 301, 30, 2),
                    (2000, 201, 30, 2),
                    (2000, 101, 90, 2),
                 ]
        exp_schema_1 = ['hotel','count']
        exp_data_1 = [('1000_301_30',4),('1000_101_10',3),('2000_101_10',2)]
        initial_df = self.session.createDataFrame(init_data_1, init_schema_1)
        result_df = top3_hotels_between_couples(initial_df)

        self.compare_dataframes(result_df,exp_data_1,exp_schema_1)

    def test_top3_srch_hotel_between_couples_with_chldrn(self):
        init_schema_1 = ['hotel_continent', 'hotel_country','hotel_market','srch_adults_cnt','srch_children_cnt','is_booking']
        init_data_1 = [
                    (1000, 101, 10,2,1,0),
                    (1000, 101, 10,2,3,0),
                    (1000, 101, 10,2,0,1),
                    (2000, 101, 10,2,1,0),
                    (2000, 101, 10,2,0,1),
                    (2000, 101, 30,1,0,1),
                    (1000, 301, 30, 2,3,0),
                    (1000, 301, 30, 2,2,0),
                    (1000, 301, 30, 2,1,0),
                    (1000, 301, 30, 2,0,1),
                    (2000, 201, 30, 2,0,1),
                    (2000, 101, 90, 2,0,1),
                 ]
        exp_schema_1 = ['hotel','count']
        exp_data_1 = [('1000_301_30',3),('1000_101_10',2),('2000_101_10',1)]
        initial_df = self.session.createDataFrame(init_data_1, init_schema_1)
        result_df = top3_srch_hotel_between_couples_with_chldrn(initial_df)

        self.compare_dataframes(result_df,exp_data_1,exp_schema_1)

if __name__ == '__main__':
    unittest2.main()
