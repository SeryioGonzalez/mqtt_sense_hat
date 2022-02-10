import paho.mqtt.client as paho
import sys
import time

mqtt_broker_host="broker.hivemq.com"
mqtt_broker_port=1883

connected_to_broker=False

#Read topic from CLI
try:
   mqtt_broker_topic=sys.argv[1]
except IndexError:
   print ("ERROR: Please provide an MQTT topic to connect")
   print ("Usage: python3 {} topic_name".format(sys.argv[0]))
   sys.exit()

print("Selected topic {}".format(mqtt_broker_topic))

#Callback methods
def on_connect(client, userdata, flags, response_code):
    if response_code == 0:
       print("CONNACK received")
       global connected_to_broker
       connected_to_broker = True
    else:
       print("ERROR: Connection failed")
       sys.exit()


def on_message(client, userdata, message):
   message_text = message.payload.decode("utf-8")
   print("Message Received: " + message_text)

#Create the MQTT client
client = paho.Client()
#Register callx backs
client.on_connect = on_connect
client.on_message = on_message

print("Connecting to broker")
client.connect(mqtt_broker_host, mqtt_broker_port)
client.loop_start()

#Wait until connected to broker. Callback will set control variable to True
while connected_to_broker == False:
    time.sleep(0.1)
print("Connected to broker")

print("Subscribing to topic {}".format(mqtt_broker_topic))
client.subscribe(mqtt_broker_topic)

#Waiting forever until there is a keyboard interrupt
try:
   while True:
      time.sleep(1)
except KeyboardInterrupt:
   print("Exiting program")
   client.disconnect()
   client.loop_stop()


