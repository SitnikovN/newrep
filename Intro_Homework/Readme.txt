Установка HDP Sandbox 2.6.5:

1. С оф сайта скачивается HDP_2.6.5_virtualbox_180626.ova файл (название может отличаться). Запускается через VB. 
После успешного запуска файла нужно зайти в web shell client (localhost:4200) и заресетить пароль admin юзера, чтобы попасть в Ambari UI. После смены пароля нужно прописать ambari-server restart и подождать пока рестартанет сервер. После некоторого времени можно подключиться к Ambari UI (localhost:8080). Также необходимо вручную стартовать сервисы Ambari, внизу для этого есть кнопка-выпадающий список "Services".

Kafka CLI :
2. в директории /usr/hdp/current/kafka-broker/bin находятся скрипты для управления сервисом. 
kafka-topics.sh - работа с топиками топика.
kafka-console-producer.sh - producer консоль.
kafka-console-consumer.sh - producer консоль.

выполненные команды:
  создание топика - sh kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic test 
  отправка сообщений: sh kafka-console-producer.sh --broker-list sandbox-hdp.hortonworks.com:6667 --topic test 
  чтение сообщений: sh kafka-console-consumer.sh --bootstrap-server sandbox-hdp.hortonworks.com:6667 --topic test --from-beginning


Установка CDH Express 6.3.2 (proof of concept version):
установка происходит через запуск cloudera-manager-installer.bin, подробная инструкция: https://docs.cloudera.com/documentation/enterprise/6/6.3/topics/poc_run_installer.html 
*После отработки bin файла нужно пройти на localhost:7180 и проследовать все 
подстепы installation Wizard'а

Kafka CLI :
	Изначально при установке Kafka сервис по дефолту не подключен. Видео с настройкой: https://www.youtube.com/watch?v=bI3c_HlOfac
	скрипты для управления : /opt/cloudera/parcels/CDH/lib/kafka/bin
	*команды для создания топика, запуска консолей producer и consumer те же самые, с другим адресом сервера (у меня развернут Google Cloud, + listeting на других портах происходит: 9092)



