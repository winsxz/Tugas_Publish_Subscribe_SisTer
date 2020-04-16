# import paho
import paho.mqtt.client as mqtt

# definsi broker yang digunakan
broker_address = "192.168..188"
#broker_address = "test.mosquitto.org"

# buat client bernama P1
print("creating new instance")
client = mqtt.Client("P1")

# client terkoneksi ke broker
print("connecting to broker")
client.connect(broker_address, port=1883)

# print "baca file"
print ("read file")

# buka file surf.jpg
with open("surf.jpg", "rb") as file:
    # baca semua isi file
    jpg = file.read()
    # ubah file dalam bentuk byte gunakan fungsi byte()
    msg = bytes(jpg)

# publish dengan topik photo dan data dipublish adalah file
print("publish foto")
client.publish("photo", msg)

# client loop mulai
client.loop_start()

# tutup file
file.close()