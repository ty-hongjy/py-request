# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 14:46:49 2017

@author: hongjy
"""

#CrowTaobaoPrice.py 

import requests
import re 
from bs4 import BeautifulSoup

def getHTMLText(url):
    try:
        kv={'user-agent':'Mozilla/5.0'}
        r=requests.get(url,headers=kv,timeout=30)
        #r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return "err"

def CategoryList(ilt,html):
    #print(html)
    #html=getHTMLText(course_url)
    #soup=BeautifulSoup(html,'html.parser')
    #soupbody=soup.body.contents
    #print(soup.body.prettify())
    #soup.get(attrs)
    #ls=re.findall('r\"data-cate=*\"',html)
    #print(ls)

    try:
        tlt=re.findall(r'data-label="..{2,5}"',html)
        print(tlt)
        print(len(tlt))
        
        for i in range(len(tlt)):
                cate=eval(tlt[i].split('=')[1])
                print(cate)
                cate1=re.findall(r'.*[^\d{1,2}]',cate)
                print(cate1)
                ilt.append(cate1)
    except:
        print("")

def printCategoryList(ilt):
    tplt="{:4}\t{:8}"
    print(tplt.format("序号","分类"))
    count=0
    for g in ilt:
        count=count+1
        print(tplt.format(count,g[0]))


def main():
    infoList=[]

    category_url='http://www.icourse163.org/category/all'
    category_url='http://www.icourse163.org/'

    course_url='http://www.icourse163.org/category/computer'
    html=getHTMLText(category_url)
    CategoryList(infoList,html)
    printCategoryList(infoList)
    
if __name__ == '__main__':
    main()
        