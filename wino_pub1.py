import paho.mqtt.client as mqtt

def on_publish(client, userdata, message):
    pass
broker_address = "192.168.0.80"
client = mqtt.Client("Wino Pub1")

client.on_publish = on_publish
client.connect(broker_address, port=1883)

client.loop_start()
while True:
    msg = input("Masukkan pesan :")

    client.publish("hello", msg)
client.loop_stop()