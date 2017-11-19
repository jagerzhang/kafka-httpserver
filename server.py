#!/usr/bin/env python
__author__ = 'jagerzhang'  
import time  
from kafka import KafkaClient,SimpleProducer  
from flask import Flask, request
from werkzeug.contrib.fixers import ProxyFix 

class Producer():  
    def __init__(self,hosts,batch_send=False,batch_send_every_n=20,async=True):  
        self.hosts=hosts  
        self.client=KafkaClient(self.hosts)  
        self.batch_send=batch_send  
        self.batch_send_every_n=batch_send_every_n  
        self.producer = SimpleProducer(self.client,batch_send=batch_send,batch_send_every_n=batch_send_every_n)  
    def send_messages(self,topic,msg):  
        self.producer.send_messages(topic,msg)  

app = Flask(__name__)
@app.route('/<topic>', methods=['GET', 'POST'])

def index(topic):
    data = request.get_data()
    hosts={'kafka.host1':'9092','kafka.host2':'9092','kafka,host3':'9092'}
    producer=Producer(hosts,False,20)
    producer.send_messages(topic,data)
    return 'success'

app.wsgi_app = ProxyFix(app.wsgi_app)

if __name__=="__main__":  
    app.run()
