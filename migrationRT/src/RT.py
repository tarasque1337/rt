'''
Created on 05.04.2018

@author: DK
'''

#!/usr/bin/env python
# -*- coding: utf-8 -*-
__version__ = 5.23


import sys
import imp
import os
import pymysql as sql
import codecs
import requests
import base64
import struct
import socket
import json
from pip._vendor.pyparsing import line


class REST:
    def __init__(self):
        self.base_url = ""

    def uploader(self, data, url):
        payload = data
        payload = json.dumps(payload)
        headers = {
             'Content-Type': 'application/json',
             'Accept': 'application/json',
             'Authorization': 'Token '
        }

        r = requests.post(url, data=payload,headers=headers, verify=False)
        print url
        print payload
        print headers

    def post_ip(self,data):
        url = self.base_url + 'api/'

    def get_subnet(self,data):
        url = self.base_url + 'api/ipam/prefixes/add/'
        self.uploader(data, url)
        
    def post_building(self, data):
        url = self.base_url + 'api/dcim/sites/'
        self.uploader(data, url)
        print data



class DB:
    def __init__(self):
        self.con = None
        self.tables = []
        self.rack_map = []
        self.vm_hosts = {}
        self.chassis = {}
        self.rack_id_map = {}
        self.container_map = {}
        self.building_room_map = {}

    def connect(self):
        self.con = sql.connect("localhost","root","","racktables")
        print('connecting to DB')
     
    @staticmethod    
    def convert_ip(ip_raw):
        
        ip = socket.inet_ntoa(struct.pack('!I', ip_raw))
        
    def get_subnets(self):
        
        subs = {}
        if not self.con:
            self.connect()
            
        with self.con:
            cur = self.con.cursor()
            q = "SELECT * FROM IPv4Network"
            cur.execute(q)
            subnets = cur.fetchall()
            
        for line in subnets:
            sid, raw_sub, mask, name, x = line
            subnet = self.convert_ip(raw_sub)
            str(mask)
            "{}/{}".format(raw_sub, mask)=prefix
            subs.update({'prefix': prefix)})
            subs.update({'is_pool': 'true'})
            subs.update({'description': name})
            rest.post_subnet(subs)
        
    def get_ips(self):
        
        adress=[]
        if not self.con
            self.connect()
        with.self.con:
            cur = self.con.cursor()
            q = 'SELECT * FROM IPv4Address WHERE IPv4Address.name != ""'
            cur.execu(q)
            ips = cur.fetchall()
            
        for line in ips:
            net{}
            ip_raw, name, comment, reserverd = line
            ip = self.convert_ip(ip_raw)
            adress.append(ip)
        
            net.update({'ipaddress': ip})
            net.update({'tag': name})
            rest.post_ip(net)
    
    def get_infrastructure(self):
test
        buildings_map = {}
        rooms_map = {}
        rows_map = {}
        racks = []
        if not self.con:
            self.connect()

    with self.con:
        #con = sql.connect("localhost","root","","racktables")
        cur = con.cursor()
        q = """select id,name, parent_id, parent_name from Location"""
        cur.execute(q)
        raw = cur.fetchall()
        for rec in raw:
            building_id, building_name, parent_id, parent_name = rec
            buildings_map.update({building_id: building_name})

        bdata = {}
for bid, building in buildings_map.items():
            bdata.update({'name': building})
            bdata.update({'slug': building})
            rest.post_building(bdata)


def main():
    db = DB()
    db.get_infrastructure()

if __name__ == '__main__':
    rest = REST()
    main()
    print ('\n[!] Done!')
    sys.exit()
