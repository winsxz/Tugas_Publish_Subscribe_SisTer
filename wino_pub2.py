import paho.mqtt.client as mqtt

def on_publish(client, userdata, message):
    message = input("Masukkan Pesan :")
    print("Publish: Chat 2")

broker_address = "192.168.0.80"
client = mqtt.Client("Wino Pub1")

client.on_publish = on_publish
client.connect(broker_address, port=1883)

client.on_publish = on_publish

client.publish("hai", message)

client.loop(2)