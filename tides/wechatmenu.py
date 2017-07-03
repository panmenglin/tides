# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf8')

from wechatpy import WeChatClient

client = WeChatClient("wxb791cfcb989d9344", "0a8cbe5d2df4c72954b193008f66ceae")
client.menu.add_conditional({
    "button":[
        {
            "type":"click",
            "name":"今日歌曲",
            "key":"V1001_TODAY_MUSIC"
        },
        {
            "type":"click",
            "name":"歌手简介",
            "key":"V1001_TODAY_SINGER"
        },
        {
            "name":"菜单",
            "sub_button":[
                {
                    "type":"view",
                    "name":"搜索",
                    "url":"http://www.soso.com/"
                },
                {
                    "type":"view",
                    "name":"视频",
                    "url":"http://v.qq.com/"
                },
                {
                    "type":"click",
                    "name":"赞一下我们",
                    "key":"V1001_GOOD"
                }
            ]
        }
    ],
    "matchrule":{
      "group_id":"2",
      "sex":"1",
      "country":"中国",
      "province":"广东",
      "city":"广州",
      "client_platform_type":"2"
    }
})