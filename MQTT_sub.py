#!/usr/bin/python3
# -*- coding: utf-8 -*-

import paho.mqtt.client as mqtt
import json
from DataBase.DataBaseAPI import DataBaseAPI
import os
import tkinter as tk
import time

class MQTT_sub:
    MQTT_ADDRESS = ''
    MQTT_USER = ''
    MQTT_PASSWORD = ''
    MQTT_TOPIC = ''
    mqtt_client = mqtt.Client()
    dataAPI = DataBaseAPI()

    def __init__(self ,MQTT_addr, MQTT_us, MQTT_pwd, MQTT_t):
        #inialisation 
        self.MQTT_ADDRESS = MQTT_addr
        self.MQTT_USER = MQTT_us
        self.MQTT_PASSWORD = MQTT_pwd
        self.MQTT_TOPIC = MQTT_t

        self.dataAPI.delete_database()
        self.dataAPI.create_table()
        self.dataAPI.export_to_csv()
        self.mqtt_client.username_pw_set(self.MQTT_USER, self.MQTT_PASSWORD)
        self.mqtt_client.on_connect = self.on_connect
        self.mqtt_client.on_message = self.on_message

    def on_connect(self,client, userdata, flags, rc):
        """ The callback for when the client receives a CONNACK response from the server."""
        print('Connected with result code ' + str(rc))
        client.subscribe(self.MQTT_TOPIC)

    def on_message(self,client, userdata, msg):
        """The callback for when a PUBLISH message is received from the server."""
        #print(msg.topic + ' ' + str(msg.payload))
        msg_decode=str(msg.payload.decode("utf-8","ignore"))
        print("data Received",msg_decode)
        print("Converting from Json to Object")
        msg_in=json.loads(msg_decode) #decode json data
        self.dataAPI.insert_data(msg_in["device"],msg_in["sensorType"],msg_in["timestamp"], msg_in["temperature"], msg_in["humidity"],msg_in["mouvement"],msg_in["luminosity"])
        self.dataAPI.update_csv()

    def on_disconnect(self,client, userdata,rc=0):
        print("DisConnected result code "+str(rc))
        client.loop_stop()

    def connect_broker(self):
        
        self.mqtt_client.connect(self.MQTT_ADDRESS, 1883)

def main():
    

    mySub1 = MQTT_sub('172.20.10.11','baoLE','12345678','home/outdoor')
    mySub1.connect_broker()
    
    mySub2 = MQTT_sub('172.20.10.11','baoLE','12345678','home/indoor')
    mySub2.connect_broker()

    mySub1.mqtt_client.loop_start()
    mySub2.mqtt_client.loop_start()
    p = True
    while p == True:
        p = True

if __name__ == '__main__':
    print('----------------Start-------------------')
    main()