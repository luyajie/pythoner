from kafka import KafkaProducer
from time import sleep

import ujson


if __name__ == '__main__':

    producer = KafkaProducer(bootstrap_servers='172.16.13.86:9092', value_serializer=ujson.loads)

    while True:
        print 'Send Start'
        producer.send('archive_test', {'filename': 'test'})
        print 'Sleep 60s'
        sleep(60)
