from time import sleep
import threading
from random import choice, randint,uniform
from kafka import KafkaProducer
from datetime import datetime,timedelta
import json

def get_random_value():
    book_event_dict = {}
    now = datetime.now()
    ci_date = now + timedelta(days=randint(1,30))
    co_date = now + timedelta(days=randint(31, 50))

    v_date_time = now.strftime('%d.%m.%Y %H:%M:%S')
    v_ci_date = ci_date.strftime('%d.%m.%Y')
    v_co_date = co_date.strftime('%d.%m.%Y')

    book_event_dict['date_time'] = v_date_time
    book_event_dict['site_name'] = randint(0, 100)
    book_event_dict['posa_continent'] = randint(0, 100)
    book_event_dict['user_location_country'] = randint(0, 100)
    book_event_dict['user_location_region'] = randint(0, 100)
    book_event_dict['user_location_city'] = randint(0, 100)
    book_event_dict['orig_destination_distance'] = round(uniform(50.01, 99.99), 2)
    book_event_dict['user_id'] = randint(0, 100)
    book_event_dict['is_mobile'] = randint(0, 100)
    book_event_dict['is_package'] = randint(0, 100)
    book_event_dict['channel'] = randint(0, 100)
    book_event_dict['srch_ci'] = v_ci_date
    book_event_dict['srch_co'] = v_co_date
    book_event_dict['srch_adults_cnt'] = randint(0, 100)
    book_event_dict['srch_children_cnt'] = randint(0, 100)
    book_event_dict['srch_rm_cnt'] = randint(0, 100)
    book_event_dict['srch_destination_id'] = randint(0, 100)
    book_event_dict['srch_destination_type_id'] = randint(0, 100)
    book_event_dict['hotel_continent'] = randint(0, 100)
    book_event_dict['hotel_country'] = randint(0, 100)
    book_event_dict['hotel_market'] = randint(0, 100)
    book_event_dict['is_booking'] = choice([True,False])
    book_event_dict['cnt'] = randint(0, 100)
    book_event_dict['hotel_cluster'] = randint(0, 100)

    return book_event_dict

class Producer(threading.Thread):
    def run(self):
        producer = KafkaProducer(bootstrap_servers=['test-bigdata.us-central1-a.c.bigdatalearn-274318.internal:6667'],
                                 value_serializer=lambda x: json.dumps(x).encode('utf-8'))
        my_topic = 'test'
        while True:
            data = get_random_value()
            future = producer.send(topic=my_topic, value=data)
            print('Thread ' + self.name  + ' sent message:--->' + str(data))
            sleep(7)

def main():
    threads = ['t1','t2','t3']
    for thr in threads:
        thr = Producer()
        thr.start()

if __name__ == '__main__':
    main()