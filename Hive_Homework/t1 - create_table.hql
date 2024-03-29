create database big_data_101;
use big_data_101;

create external table train(
    date_time string,
    site_name int,
    posa_continent int,
    user_location_country int,
    user_location_region int,
    user_location_city int,
    orig_destination_distance double,
    user_id int,
    is_mobile tinyint,
    is_package int,
    channel int,
    srch_ci string,
    srch_co string,
    srch_adults_cnt int,
    srch_children_cnt int,
    srch_rm_cnt int,
    srch_destination_id int,
    srch_destination_type_id int,
    is_booking tinyint,
    cnt bigint,
    hotel_continent int,
    hotel_country int,
    hotel_market int,
    hotel_cluster int
    )
row format delimited fields terminated by ',' lines terminated by '\n'
location '/user/input_files/train'
tblproperties("skip.header.line.count"="1");