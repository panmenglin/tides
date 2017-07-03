# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

import sys
reload(sys)
sys.setdefaultencoding('utf8')

# import module from django & wechat_sdk
# pip install django && pip install wechat_sdk first
from django.http.response import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt

from wechatpy import WeChatComponent
from wechatpy.utils import check_signature
from wechatpy.exceptions import InvalidSignatureException
from wechatpy import parse_message, create_reply


from tool import is_fundcode
from fund import getHoldings
from config import config
# pass csrf check

conf = config()

@csrf_exempt
def wechat_home(request):
    # get signature, timestamp and nonce
    signature = request.GET.get('signature')
    timestamp = request.GET.get('timestamp')
    nonce = request.GET.get('nonce')

    if request.method == 'GET':
        signature = request.GET.get('signature', '')
        timestamp = request.GET.get('timestamp', '')
        nonce = request.GET.get('nonce', '')
        echo_str = request.GET.get('echostr', '')
        try:
            check_signature(conf['token'], signature=signature, timestamp=timestamp, nonce=nonce)
        except InvalidSignatureException:
            echo_str = 'error'
        response = HttpResponse(echo_str, content_type="text/plain")
        return response
    else:
        reply = None
        msg = parse_message(request.body)
        if msg.type == 'text':
            if is_fundcode(msg.content):
                reply = create_reply(getHoldings(msg.content), message=msg)
            else:
                reply = create_reply('你可以输入基金代码来查询基金信息', message=msg)
        else:
            pass

        if not reply or not isinstance(reply, BaseReply):
            reply = create_reply('你可以输入基金代码来查询基金信息', message=msg)

        response = HttpResponse(reply.render(), content_type="application/xml")
        return response
