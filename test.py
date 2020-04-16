import paho.mqtt.client as mqtt

broker_address = "192.168.0.80"

client = mqtt.Client("P5")

def on_publish(client, userdata, result):
    print("test")

client.on_publish = on_publish

print("Connenting to broker")
client.connect(broker_address, port=1883)

client.loop_start()

print("Test Publish Nama dan NIM\n")

nama = "Nama    : Wino Rama Putra"
nim =  "NIM     : 1301174696"

msg = nama + "\n" +nim

client.publish("test", msg)

client.loop_stop()
