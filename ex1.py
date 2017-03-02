import requests

def getHTMLText(url):
	try:
		r=requests.get(url,timeout=30)
		r.raise_for_status
		r.status_code
		r.encoding
		print(r.apparent_encoding)
		q.head(url)
		#print(r.head(url))
		r.text
		#q=requests.head(url)
		#print(q.headers)

	except:
		#return "err"
		#//raise
		#print("err")
		return "err"
 
if __name__ == '__main__':
	#main()
	url="http://www.baidu.com"
	#getHTMLText(url)

kv={'k1':'v1','k2':'v2'}
r=requests.request('GET','http://pt123.io/wa',params=kv)
print(r.url)
body="content"
r=requests.request('POST','http://pt123.io/wa',data=body)
print(r.url)

r=requests.request('POST','http://pt123.io/wa',json=kv)
print(r.url)

hd={'user-agent':'chrome/10'}
r=requests.request('POST','http://pt123.io/wa',headers=hd)
print(r.url)