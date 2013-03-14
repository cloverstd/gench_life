#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web
from message import Message
from func import magic
from func import check

urls = ('/', 'WeiXin')

web.config.debug = True

class WeiXin:

    def GET(self):
        # msg = Message(msg_text)
        # return magic(msg)
        data = web.input()
        print data['signature']
        # try:
        if not check(data):
            print "test"
            return u"非法入侵者"
        else:
            return data['echostr']
        # except:
            # return u"非法入侵者"

    def POST(self):
        data = web.input()

        if not check(data):
            return u"非法入侵者"

        data = web.data()
        # print data
        msg = Message(data)
        return magic(msg)

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
