from kafka import KafkaConsumer
from time import sleep
import ujson


if __name__ == '__main__':
    consumer = KafkaConsumer(bootstrap_servers='172.16.13.86:9092',
                             auto_offset_reset='earliest')
    consumer.subscribe(['archive_test'])

    print 'Consume Start'
    for msg in consumer:
        print msg.value
