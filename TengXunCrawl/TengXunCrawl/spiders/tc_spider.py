# -*- coding: utf-8 -*-
import re
import scrapy
from scrapy.selector import Selector
from ..items import *
import redis
import pymysql
import urllib
import json

class tc_Spider(scrapy.spiders.Spider):
    name = "tcSpider"

    def __init__(self):
        self.pattern = re.compile(r'https://new.qq.com/.*')
        self.item = TengxuncrawlItem()
        self.r = redis.Redis(host='127.0.0.1', port=6379,db=0)
        self.hostUrl = 'https://news.qq.com/'
        self.db = pymysql.connect('localhost','root','3.141592653579','qqnews',charset='utf8' )

    def start_requests(self):
        '''
        如果待爬队列为空那么需要启动两次爬虫程序，第一次爬取hostirl的内容,第二次爬取队列内容,并填充队列
        :return:
        '''
        if self.r.llen('tcSpider:items') == 0:
            yield scrapy.Request(url=self.hostUrl, callback=self.parse)
        while self.r.llen('tcSpider:items')> 0:
            url = eval(self.r.lpop('tcSpider:items'))['url']
            yield scrapy.Request(url=url, callback=self.parse)
        self.CloseMysql()

    def parse(self, response):
        urlList = Selector(text=response.body).css('a').xpath('@href').extract()  #获取<a>的href值
        content_div = Selector(text=response.body).xpath("//div[contains(@class,'content clearfix')]").extract()  #获取内容
        if len(content_div) > 0:  #是内容页
            title = Selector(text=response.body).xpath("//div[contains(@class,'qq_conent clearfix')]").xpath("//div[contains(@class,'LEFT')]").css('h1::text').extract()[0]
            content = self.getChinese(content_div[0]) #获取内容
            id_href = Selector(text=response.body).xpath("//a[contains(@id,'cmtLink')]").xpath('@href').extract()[0] #获取id
            cmtNum_str = Selector(text=response.body).xpath("//a[contains(@id,'cmtLink')]").css('div i::text').extract()[0]
            id = self.getNum(id_href)
            cmtNum = int(cmtNum_str)
            jsonData = self.getJson(id)
            self.InsertMysql(content,id,title,cmtNum,jsonData)  #插入mysql

        for url in urlList:
            if self.pattern.search(url):
                self.item['url'] = url
                yield self.item

    def getNum(self,str):
        pattern = "\d+"
        regex = re.compile(pattern)
        results = regex.findall(str)
        str = ''
        for r in results:
            str = str+r
        return int(str)

    def getChinese(self,str):
        pattern = "[\u4e00-\u9fa5]+"
        regex = re.compile(pattern)
        results = regex.findall(str)
        str = ''
        for r in results:
            str = str+r
        return str

    def InsertMysql(self,content,id,title,cmtNum,JsonData):
        self.db.ping(reconnect=True)
        cursor = self.db.cursor()
        sql = "INSERT INTO news(content,id,title,cmtnum,comment) VALUES ('%s','%d','%s','%d','%s')" %(content,id,title,cmtNum,pymysql.escape_string(json.dumps(JsonData)))
        print(sql)
        try:
            cursor.execute(sql)
            self.db.commit()
            print('--------------------------------------------------------------')
        except:
            self.db.rollback()
            print('**************************************************************')

    def CloseMysql(self):
        self.db.close()

    def getJson(self,idStr):
        id = str(idStr)
        pattern = re.compile('[(](.*)[)]')
        response = urllib.request.urlopen(
            'http://coral.qq.com/article/' + id + '/comment/v2?callback=_article' + id + 'commentv2&orinum=30')
        m = pattern.search(str(response.read().decode('utf-8')))
        p1 = re.compile(r'\(')
        p2 = re.compile(r'\)')
        s1 = p1.sub('[', m.group())
        s2 = p2.sub(']', s1)
        value = json.loads(s2)
        return value

