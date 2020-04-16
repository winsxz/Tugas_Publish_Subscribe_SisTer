# import paho mqtt
import paho.mqtt.client as mqtt

# import time untuk sleep()
import time

# import datetime untuk mendapatkan waktu dan tanggal
import datetime


# definisikan nama broker yang akan digunakan
broker_address = "192.168.0.80"
#broker_address = "test.mosquitto.org"

# buat client baru bernama P3
print("creating new instance")
client = mqtt.Client("P3")

# koneksi ke broker
print("connecting to broker")
client.connect(broker_address, port=1883)

# mulai loop client
client.loop_start()

# lakukan 20x publish topik 2
print("publish something")
for i in range (20):
    # sleep 1 detik
    time.sleep(1)
    # publish waktu sekarang topik 2
    msg = str(datetime.datetime.now())
    client.publish("topik_2", 'BBB' + ' ' + msg)

#stop loop
client.loop_stop()
