# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 14:04:23 2019

@author: shiyu
"""
from xml.etree.ElementTree import parse
import urllib.request, urllib

KEY = 'AIzaSyD_b_uTd5vQpsqL581aVDZu3BxYlouqXS0'

class GetData(object):
    def __init__(self):
        self.values = {'q': '', 
                'sensor': 'false', 
                'output': 'xml', 
                'oe': 'utf8'}
        self.url = 'http://maps.google.com/maps/place'

    def catchData(self, city, key=KEY):
        '''
        利用google map api从网上获取city的经纬度。
        '''
        self.values['q'] = city
        print (self.values)
        #self.values['key'] = key
        arguments = urllib.parse.urlencode(self.values)
        url_get = self.url + '/' + arguments
        handler = urllib.request.urlopen(url_get)
        try:
            self.lon, self.lat = self.parseXML(handler)
            #print 'lon:%d\tlat:%d' % (self.lon, self.lat)
            return self.lon, self.lat
        except IndexError:
            print ('城市: %s' % (city,))
        finally:
            handler.close()
        
    def parseXML(self, handler):
        '''
        解析从API上获取的XML数据。
        '''
        xml_data = parse(handler)
        data = xml_data.getElementsByTagName('coordinates')[0].firstChild.data
        coordinates = data.split(',')
        lon = int(float(coordinates[0]) * 1000000)
        lat = int(float(coordinates[1]) * 1000000)
        return lon, lat
'''       
if __name__ == '__main__':
    for c in b:
    getData = GetData()
    cityName = raw_input('请输入一个城市：')
    longitude, latitude = getData.catchData(cityName)
    print '%s \n经度：%d\n纬度：%d\n' % (cityName, longitude, latitude)
'''