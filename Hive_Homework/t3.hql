select 
    hotel
from
    (
        select  
            hotel_continent || '_' || hotel_country || '_' || hotel_market hotel,
            count(*) cnt_book
        from train
        where is_booking = 0
        group by hotel_continent || '_' || hotel_country || '_' || hotel_market 
        order by cnt_book desc
        limit 3
    ) tab