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
        #r.encoding='UTF-8'
        #r.encoding='gbk'
        return r.text
    except:
        return "err"

def CategoryList(ilt,html):
    try:
        tlt=re.findall(r'data-label="..{2,5}"',html)
        
        for i in range(len(tlt)):
                cate=eval(tlt[i].split('=')[1])
                cate1=re.findall(r'.*[^\d{1,2}]',cate)
                ilt.append(cate1)
    except:
        print("")
        
def CategoryList1(ilt,html):
        soup=BeautifulSoup(html,'html.parser')
        for p in soup.select(".nav-level1__label"):
            #print(p.text)
            #print(p.select(".slideTop-cateFunc-f_div200_a201"))
            #print(p.select(".slideTop-cateFunc-f_div200_a201")[1].text)
            #print(p.attrs['href'])
            #print(p.get("a"))
            ilt.append([p.text,p.attrs['href']])
        ilt.append(["Quit",""])
        
        print(soup.select(".nav-level2-keywords--content"))


def printCategoryList(ilt):
    tplt="{:4}\t{:8}"
    print(tplt.format("序号","分类"))
#    tplt="{:4}\t{:8}\t{:20}"
#   print(tplt.format("序号","分类","URL"))
    count=0
    for g in ilt:
        count=count+1
        print(tplt.format(count,g[0],g[1]))
        
def SubCategoryList(ilt,html):
    print(html)
    #html=getHTMLText(course_url)
    soup=BeautifulSoup(html,'html.parser')
    #soupbody=soup.body.contents
    #print(soupbody)
    #print(soup.body.prettify())
    #soup.get(attrs)
    #ls=re.findall('r\"data-cate=*\"',html)
    #print(ls)
    #soup=BeautifulSoup(r.text,'html.parser')
    #print(soup.ul)
    #print(soup.select(".inline-block-list"))
    ilt.append(['234'])
    
'''    try:
        tlt=re.findall(r'alt="..{2,20}"',html)
        
        print(len(tlt))
        print(tlt)
        
        for i in range(len(tlt)):
                course=eval(tlt[i].split('=')[1])
                print(course)
                #cate1=re.findall(r'.*[^\d{1,2}]',cate)
                #print(cate1)
                ilt.append(course)
    except:
        print("")
'''

def SubCategoryList1(html):
    #print(html)
    #html=getHTMLText(course_url)
    soup=BeautifulSoup(html,'html.parser')
    #print(soup.ul)
    #print(soup.select(".inline-block-list"))
    #print(soup.select(".inline-block-list")[0])#0
    #print(soup.select(".filter-sect-list")[12])#2
    #print(soup.select(".recommend-movies")[0])
    #print(soup.select(".reco-movieinfo__name"))#[0])#3
    print(soup.select(".nav-level2-keywords--content"))
    print(soup.select(".nav-level2-keywords--title"))
    #print(soup.body.prettify())


def printSubCategoryList(ilt):
    tplt="{:4}\t{:8}"
    print(tplt.format("序号","课程"))    #ilt.append(['234'])

    count=0
    for g in ilt:
        count=count+1
        print(tplt.format(count,g[0]))


def main():
    CategoryList=[]
    SubCategoryList=[]
    list1=[]
    
    category_url='http://ty.meituan.com/'

    html=getHTMLText(category_url)
    CategoryList1(CategoryList,html)
    printCategoryList(CategoryList)

    SubCategory_url=CategoryList[1][1]
    print(SubCategory_url)
    html=getHTMLText(SubCategory_url)
    SubCategoryList1(html)
    http://ty.meituan.com/multiact/default//category/meishi
    http://ty.meituan.com/multiact/default//category/meishi
    #SubCategoryList(SubCategoryList,html)
    
if __name__ == '__main__':
    main()
