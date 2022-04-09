from mq_setup import BasicPikaClient
import pika

class MessageSender(BasicPikaClient):
    def send_message(self, exchange, routing_key, body):
        self.check_setup()
        channel = self.connection.channel()
        channel.basic_publish(exchange=exchange,
                              routing_key=routing_key,
                              body=body, properties=pika.BasicProperties(delivery_mode = 2))
        print(f"Sent message. Exchange: {exchange}, Routing Key: {routing_key}, Body: {body}")