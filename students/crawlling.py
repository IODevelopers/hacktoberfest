import requests
from bs4 import BeautifulSoup
query = input ("search for ... ")
url= "https://www.bing.com/search?q=" + query
print(url)
data= requests.get(url)
print(data)
soup= BeautifulSoup(data.content,"html.parser")
ResponseData=soup.find_all("li",{'class':'b_algo'})
#print(ResponseData[0].text)
for result in ResponseData :
	print(result.text)
	print(" ")
