from kafka import KafkaProducer
import serial

producer = KafkaProducer(bootstrap_servers=['192.168.168.72:9092'],api_version=(0,10))
arduino = serial.Serial('COM3', 115200)
while True:
	data = arduino.readline()[:-2] #the last bit gets rid of the new-line chars
	if data:
		print data
		if (data == 'GG'):
			producer.send('goals', 'Gold')
		elif (data == 'BG'):
			producer.send('goals', 'Black')
		elif (data == 'GD'):
			producer.send('drops', 'Gold')
		elif (data == 'BD'):
			producer.send('drops', 'Black')
		producer.flush()

    
# producer.flush()

# Block until a single message is sent (or timeout)
# future = producer.send('test', b'another_message')
# result = future.get(timeout=60)
#  # Block until all pending messages are at least put on the network
#  # NOTE: This does not guarantee delivery or success! It is really
#  # only useful if you configure internal batching using linger_ms
#  producer.flush()
#  # Use a key for hashed-partitioning
#  producer.send('foobar', key=b'foo', value=b'bar')
#  # Serialize json messages
#  import json
#  producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('utf-8'))
#  producer.send('fizzbuzz', {'foo': 'bar'})
#  # Serialize string keys
#  producer = KafkaProducer(key_serializer=str.encode)
#  producer.send('flipflap', key='ping', value=b'1234')
#  # Compress messages
#  producer = KafkaProducer(compression_type='gzip')
#  for i in range(1000):
#      producer.send('foobar', b'msg %d' % i)