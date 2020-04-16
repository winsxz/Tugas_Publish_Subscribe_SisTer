import paho.mqtt.client as mqtt

def on_message(client, userdata, message):
    print("Topik    :", message.topic)
    print("Isi Chat :",str(message.payload))
broker = "192.168.0.80"
client = mqtt.Client("Wino Sub1")
client.on_message = on_message
client.connect(broker, port=1883)
client.subscribe("hai")
client.loop_forever()
