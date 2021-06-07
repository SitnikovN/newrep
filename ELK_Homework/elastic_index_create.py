from elasticsearch import Elasticsearch

settings = {
        "settings": {
            "number_of_shards": 1,
            "number_of_replicas": 0
        },
        "mappings": {
                "properties": {
                    "date_time": {
                        "type": "date",
                        "format":"dd.MM.yyyy HH:mm:ss"
                    },
                    "site_name": {
                        "type": "long"
                    },
                    "posa_continent": {
                        "type": "long"
                    },
                    "user_location_country": {
                        "type": "long"
                    },
                    "user_location_region": {
                        "type": "long"
                    },
                    "user_location_city": {
                        "type": "long"
                    },
                    "orig_destination_distance": {
                        "type": "long"
                    },
                    "user_id": {
                        "type": "long"
                    },
                    "is_mobile": {
                        "type": "long"
                    },
                    "is_package": {
                        "type": "long"
                    },
                    "channel": {
                        "type": "long"
                    },
                    "srch_ci": {
                        "type": "text"
                    },
                    "srch_co": {
                        "type": "text"
                    },
                    "srch_adults_cnt": {
                        "type": "long"
                    },
                    "srch_children_cnt": {
                        "type": "long"
                    },
                    "srch_rm_cnt": {
                        "type": "long"
                    },
                    "srch_destination_id": {
                        "type": "long"
                    },
                    "srch_destination_type_id": {
                        "type": "long"
                    },
                    "hotel_continent": {
                        "type": "long"
                    },
                    "hotel_country": {
                        "type": "long"
                    },
                    "hotel_market": {
                        "type": "long"
                    },
                    "is_booking": {
                        "type": "boolean"
                    },
                    "cnt": {
                        "type": "long"
                    },
                    "hotel_cluster": {
                        "type": "long"
                    }
                }

        }
    }
es = Elasticsearch([{'host':'localhost','port':9200}])
es.indices.create(index='test13',ignore = 400, body=settings)
