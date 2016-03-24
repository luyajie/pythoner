import threading, logging, time

from kafka import KafkaConsumer, KafkaProducer
import ujson


class Producer(threading.Thread):
    daemon = True

    def run(self):
        producer = KafkaProducer(bootstrap_servers='172.16.13.86:9092')

        while True:
            producer.send('archive_test', ujson.dumps({'filename': 'y'}))
            time.sleep(1)


class Consumer(threading.Thread):
    daemon = True

    def run(self):
        consumer = KafkaConsumer(bootstrap_servers='172.16.13.86:9092',
                                 auto_offset_reset='earliest')
        consumer.subscribe(['archive_test'])

        for message in consumer:
            print message.value


def main():
    threads = [
        #Producer(),
        Consumer()
    ]

    for t in threads:
        t.start()

    time.sleep(1)

if __name__ == "__main__":
    main()
