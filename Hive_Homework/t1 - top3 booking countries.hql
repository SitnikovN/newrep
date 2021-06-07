select hotel_country
from
    (
        select  
            hotel_country,count(hotel_country) cnt_book
        from train
        where is_booking = 1
        group by hotel_country
        order by cnt_book desc
        limit 3
    ) tab