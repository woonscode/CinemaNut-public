import ssl
import pika

class BasicPikaClient:
    # Initialises Amazon MQ client
    def __init__(self, rabbitmq_broker_id, rabbitmq_user, rabbitmq_password, region):
        self.broker_id = rabbitmq_broker_id
        self.user = rabbitmq_user
        self.password = rabbitmq_password
        self.region = region
        # SSL Context for TLS configuration of Amazon MQ for RabbitMQ
        ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
        ssl_context.set_ciphers('ECDHE+AESGCM:!ECDSA')

        url = f"amqps://{self.user}:{self.password}@{self.broker_id}.mq.{self.region}.amazonaws.com:5671"
        parameters = pika.URLParameters(url)
        parameters.ssl_options = pika.SSLOptions(context=ssl_context)

        self.connection = pika.BlockingConnection(parameters)
        self.channel = self.connection.channel()
        self.setup()
    
    # Sets up exchanges and queues
    def setup(self):
        channel = self.connection.channel()
        exchange_name = "cinemanut"
        queue_name = "activity_log"
        channel.exchange_declare(exchange=exchange_name, exchange_type="direct", durable=True)
        channel.queue_declare(queue=queue_name, durable=True)
        channel.queue_bind(exchange=exchange_name, queue=queue_name, routing_key="activity_log")
    
    # Allows children classes to check if connection and channel is open before publishing and consuming
    def check_setup(self):
        if not self.test_connection_open():
            ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
            ssl_context.set_ciphers('ECDHE+AESGCM:!ECDSA')
            
            url = f"amqps://{self.user}:{self.password}@{self.broker_id}.mq.{self.region}.amazonaws.com:5671"
            parameters = pika.URLParameters(url)
            parameters.ssl_options = pika.SSLOptions(context=ssl_context)

            self.connection = pika.BlockingConnection(parameters)
            self.channel = self.connection.channel()
        if self.channel.is_closed:
            self.setup()
    # Helper function to check connection status
    def test_connection_open(self):
        try:
            self.connection.process_data_events()
            return True
        except pika.exceptions.AMQPError as e:
            print("AMQP Error:", e)
            print("...creating a new connection.")
            return False