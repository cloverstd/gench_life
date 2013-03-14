#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
from time import time


msg_text = """<xml>
<ToUserName><![CDATA[toUser]]></ToUserName>
<FromUserName><![CDATA[fromUser]]></FromUserName> 
<CreateTime>1348831860</CreateTime>
<MsgType><![CDATA[text]]></MsgType>
<Content><![CDATA[this is a test]]></Content>
<MsgId>1234567890123456</MsgId>
</xml>"""
msg_image = """<xml>
<ToUserName><![CDATA[toUser]]></ToUserName>
<FromUserName><![CDATA[fromUser]]></FromUserName>
<CreateTime>1348831860</CreateTime>
<MsgType><![CDATA[image]]></MsgType>
<PicUrl><![CDATA[this is a url]></PicUrl>
<MsgId>1234567890123456</MsgId>
</xml>"""
msg_locate = """<xml>
<ToUserName><![CDATA[toUser]]></ToUserName>
<FromUserName><![CDATA[fromUser]]></FromUserName>
<CreateTime>1351776360</CreateTime>
<MsgType><![CDATA[location]]></MsgType>
<Location_X>23.134521</Location_X>
<Location_Y>113.358803</Location_Y>
<Scale>20</Scale>
<Label><![CDATA[位置信息]]></Label>
<MsgId>1234567890123456</MsgId>
</xml>"""
msg_url = """<xml>
<ToUserName><![CDATA[toUser]]></ToUserName>
<FromUserName><![CDATA[fromUser]]></FromUserName>
<CreateTime>1351776360</CreateTime>
<MsgType><![CDATA[link]]></MsgType>
<Title><![CDATA[公众平台官网链接]]></Title>
<Description><![CDATA[公众平台官网链接]]></Description>
<Url><![CDATA[url]]></Url>
<MsgId>1234567890123456</MsgId>
</xml>"""
msg_event = """<xml>
<ToUserName><![CDATA[toUser]]></ToUserName>
<FromUserName><![CDATA[fromUser]]></FromUserName>
<CreateTime>123456789</CreateTime>
<MsgType><![CDATA[event]]></MsgType>
<Event><![CDATA[LOCATION]]></Event>
<Latitude>23.137466</Latitude>
<Longitude>113.352425</Longitude>
<Precision>119.385040</Precision>
</xml>"""
class Message(object):

    def __init__(self, recv_msg):
        self.__recv_msg = dict()
        try:
            root = ET.fromstring(recv_msg)
            self.recv_msg = dict()
            for child in root:
                self.__recv_msg.setdefault(child.tag, child.text)
        except:
            raise TypeError("recv_msg shold be weixin receive message")

    def __getitem__(self, name):
        if name in self.__recv_msg.keys():
            return self.__recv_msg[name]
        else:
            raise KeyError("No key %s" % name)

    def keys(self):
        return self.__recv_msg.keys()

    def text_msg(self, content, star=0):
        """返回一个 text 消息的 list """
        text_msg = list()
        text_msg.append(self.__recv_msg['FromUserName'])
        text_msg.append(self.__recv_msg['ToUserName'])
        text_msg.append(time())
        text_msg.append(content)
        text_msg.append(star)
        return text_msg

    def music_msg(self, title, url, description=None, HQ_url=None, star=0):
        """返回一个 music 消息的 list """
        music_msg = list()
        music_msg.append(self.__recv_msg['FromUserName'])
        music_msg.append(self.__recv_msg['ToUserName'])
        music_msg.append(time())
        music_msg.append(title)
        music_msg.append(description if description else title)
        music_msg.append(url)
        music_msg.append(HQ_url if HQ_url else url)
        music_msg.append(star)
        return music_msg

    def news_msg(self, news, star=0):
        """返回一个 news 消息的 list """
        news_msg = list()
        news_msg.append(self.__recv_msg['FromUserName'])
        news_msg.append(self.__recv_msg['ToUserName'])
        news_msg.append(time())
        if len(news) > 10:
            news = news[:10]
        news_msg.append(len(news))
        news_msg.append(news)
        news_msg.append(star)
        return news_msg





if __name__ == '__main__':
    msg = Message(msg_url)
    print msg['MsgType']
    print msg.text_msg("消息", 0)
    print msg.music_msg("一生所爱", "http://hui.lu")
    news = [
            ["标题", "描述", "图片链接", "链接"],
            ["标题", "描述", "图片链接", "链接"],
            ["标题", "描述", "图片链接", "链接"],
            ["标题", "描述", "图片链接", "链接"],
            ["标题", "描述", "图片链接", "链接"],
            ["标题", "描述", "图片链接", "链接"],
            ["标题", "描述", "图片链接", "链接"],
            ]
    print msg.news_msg(news)
