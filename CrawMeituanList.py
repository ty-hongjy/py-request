#-*-coding:utf-8-*-
"""
CreatedonFriMar1714:46:492017

@author:hongjy
"""

#CrowMeiTuanList.py

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
        return"err"

def CategoryList1(ilt,html):
    try:
        tlt=re.findall(r'data-label="..{2,5}"',html)
        
        for i in range(len(tlt)):
            cate=eval(tlt[i].split('=')[1])
            cate1=re.findall(r'.*[^\d{1,2}]',cate)
            ilt.append(cate1)
    except:
        print("")

def getCategoryList(ilt,html):
    soup=BeautifulSoup(html,'html.parser')
    for p in soup.select(".nav-level1__label"):
        ilt.append([p.text,p.attrs['href']])
    ilt.append(["Quit",""])
    
def printCategoryList(ilt):
    tplt="{:4}\t{:8}"
    print(tplt.format("序号","分类"))
    count=0
    for g in ilt:
        count=count+1
        print(tplt.format(count,g[0],g[1]))
    
def getSubCategoryList(ilt,html):
    	count=0
    	soup=BeautifulSoup(html,'html.parser')
    	sub1=soup.select(".nav-level2-keywords--content")
    	for g in sub1:
    		count=count+1
    		ilt.append(g.text)
    	print("-----------")

def printSubCategoryList(ilt,num):
    	print("-----------")
    	print(ilt[num])

def main():
    CategoryList=[]
    SubCategoryList=[]
    
    category_url='http://ty.meituan.com/'
    
    html=getHTMLText(category_url)
    getCategoryList(CategoryList,html)
    printCategoryList(CategoryList)
    getSubCategoryList(SubCategoryList,html)

    while True:
        sele=input("请输入选择子类编号：[1-9],显示分类请输入[R]or[r],退出选择[Q]or[q]")
        if sele=="Q" or sele=="q":
            break
        elif sele=="R" or sele=="r":
            printCategoryList(CategoryList)
        elif eval(sele)>1 and eval(sele)<=9:
            subcatnum=eval(sele)-1
            printSubCategoryList(SubCategoryList,subcatnum)
        else:
            continue
    print("End")

if __name__=='__main__':
	main()
