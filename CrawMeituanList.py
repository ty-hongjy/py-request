# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 14:46:49 2017

@author: hongjy
"""

#CrowTaobaoPrice.py 

import requests
import re 
from bs4 import BeautifulSoup

#SubCategoryList=[]

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
        
        print(len(soup.select(".nav-level2-keywords--content")))


def printCategoryList(ilt):
    tplt="{:4}\t{:8}"
    print(tplt.format("序号","分类"))
#    tplt="{:4}\t{:8}\t{:20}"
#   print(tplt.format("序号","分类","URL"))
    count=0
    for g in ilt:
        count=count+1
        print(tplt.format(count,g[0],g[1]))
        

def getSubCategoryList(ilt,html,num):
    #print(html)
    #html=getHTMLText(course_url)
    soup=BeautifulSoup(html,'html.parser')
    if num==0:
        print(soup.select(".inline-block-list"))
        for a1 in soup.select(".inline-block-list")[0]:
            print(a1.li.a)
        print(soup.select(".inline-block-list")[0].text)
    elif num==1:
        str1=soup.select(".filter-sect-list")[12]
        #print(str1)
        #for a1 in str1:
        #print(len(str1))
        
        if len(str1.text.strip())>0:
            print(str1.text)
        
        '''for a in str1:
            if len(a.text.strip())>0:
                print(a.strip())
         '''   
            
            
            #print(soup.select(".filter-sect-list")[12])
            #print(soup.select(".filter-sect-list")[12].text)
            #print("----------")
            #str1=soup.select(".filter-sect-list")[12].li
            #str1=soup.select(".filter-sect-list")[12].find_all("label")
            #str2=re.findall("<lable>*</label>",str1)
            #str3=re.split()
            #print(str2)
            #str2=str1.find_all(a)
            #print(str2)
            #str2=soup.find_all("label")
            #print(str2)
    elif num==2:
        #print(soup.select(".recommend-movies"))
        print(soup.select(".recommend-movies")[0].text)
        #print(type(soup.select(".recommend-movies")[0].text))
        #print(len(soup.select(".recommend-movies")[0].text))
        
        #print(soup.select(".recommend-movies")[0].h3.text)
        #print(soup.select(".reco-movieinfo__name"))#[0])#3
    #print(soup.select(".nav-level2-keywords--content"))
    #print(soup.select(".nav-level2-keywords--title"))
    #print(soup.body.prettify())
    else:
        print("not fininsh,waiting ")

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
    
    category_url='http://ty.meituan.com/'

    html=getHTMLText(category_url)
    CategoryList1(CategoryList,html)
    printCategoryList(CategoryList)

    while True:
        sele=input("请输入选择子类编号：[1-14],显示分类请输入[R] or [r],退出选择[Q] or [q]")
        if sele=="Q" or sele=="q":
            break
        if sele=="R" or sele=="r":
            printCategoryList(CategoryList)
        else:
            subcatnum=eval(sele)-1
            SubCategory_url=CategoryList[subcatnum][1]
            print(SubCategory_url)
            html=getHTMLText(SubCategory_url)
            getSubCategoryList(SubCategoryList,html,subcatnum)
            #SubCategoryList1(html,subcatnum)
            
    print("End")
    
if __name__ == '__main__':
    main()
