# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

import urllib2
import re
import codecs
import json


def getHoldings(code):
    request = urllib2.Request("http://fund.jrj.com.cn/archives,"+code+",cgmx.shtml")
    response = urllib2.urlopen(request)

    content = response.read().decode("GBK")
    pattern = re.compile('<div.*?class="tbcont.*?>.*?<table.*?>(.*?)</table>.*?</div>',re.S)
    items = re.findall(pattern,content)

    holdings = items[0]
    holdingsFilter = re.compile(r'<tr.*?>.*?<td.*?><a.*?>(.*?)</a></td>.*?<td.*?><a.*?>(.*?)</a></td>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?</tr>',re.S)
    holdingsItems = re.findall(holdingsFilter,holdings)

    # 返回重仓股json
    # holdingsArr = []
    # for item in holdingsItems:
    #     holdingsArr.append({'code':item[0], 'name':item[1], 'holdings':item[2], 'marketValue':item[3], 'proportion':item[4]})

    # return json.dumps(holdingsArr,ensure_ascii=False)
    
    # 返回重仓股消息
    holdingsArr = ''
    for item in holdingsItems:
        holdingsArr += '代码:' + item[0] + '  名称:' + item[1]+ '  占比:' + item[4] + '\n'

    fundTitleFilter = re.compile('<div.*?id="minfo".*?>.*?<h3>(.*?)</h3>.*?</div>',re.S)
    fundTitle = re.findall(fundTitleFilter,content);

    
    return fundTitle[0] + ' 重仓股信息：' + '\n' + holdingsArr