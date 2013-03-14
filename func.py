#!/usr/bin/env python
# -*- coding: utf-8 -*-

import plugins
from config.settings import weixin_token
import hashlib

import web
render = web.template.render('respond/')

def check(data):
    """检验消息来源"""
    signature = list()
    signature.append(weixin_token)
    try:
        signature.append(data['nonce'])
        signature.append(data['timestamp'])
    except:
        return False
    signature.sort()
    signature = "".join(signature)
    signature = hashlib.sha1(signature).hexdigest().encode('utf-8')
    if signature == data['signature']:
        return True
    else:
        return False


def magic(msg):
    """
    msg.text_msg(content, star=0)
    # 返回文本消息
    text = msg.text_msg("测试")
    return render.text(text)
    
    msg.musci_msg(title, url, description=None, HQ_url=None)
    # 返回音乐消息
    music = msg.musci_msg("一生所爱", "http://hui.lu")
    return render.music(musci)

    msg.news_msg(news, stat=0)
    # 返回图文消息
    news = [    # news 最多 10 条，如果超过则只返回前 10 条
            ["标题", "描述", "图片链接", "链接"],
            ["标题", "描述", "图片链接", "链接"],
            ["标题", "描述", "图片链接", "链接"],
            ]
    news_msg = msg.news_msg(news)
    return render.news(news_msg)
    """
    music = msg.music_msg("一生所爱", "http://hui.lu")
    return render.music(music)
