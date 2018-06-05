from bs4 import BeautifulSoup
import requests

url = "https://valiancesolutions.com"

page = requests.get(url).text
soup = BeautifulSoup(page,"html.parser")

for i in soup.findAll():
    if i.text.lower() in ["contact us","contact","write","connect"]:
        print (i)

# got contact url somehow using href in i

url2 = "https://valiancesolutions.com/contact-us/"
page = requests.get(url2).text
soup = BeautifulSoup(page,"html.parser")

address = ""
for i in soup.findAll("div",{"class":"vc_column-inner vc_custom_1489495538574"}):
    if i.text!="":
        address+=i.text

replaced = re.sub(r"\n+", "\n", address)
print(replaced)