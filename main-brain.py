from bs4 import BeautifulSoup
import requests
import re

from csIndia import csIndia as lis

# url = "https://valiancesolutions.com"
urls = [
    "https://valiancesolutions.com",
    "http://corifictechnologies.com",
    "https://www.hcltech.com",
    "https://www.wipro.com",
    "https://www.kpit.com",
    "https://www.scatech.com",
    "https://axtria.com",
    "http://www.qcin.org"
    ]

for url in urls:
    page = requests.get(url).text
    soup = BeautifulSoup(page,"html.parser")
    
    url2 = ""
    for i in soup.findAll():
        for j in ["contact us","contact","contact-us"]: 
            if j in i.text.lower():
                try:
                    if i["href"]:
                        url2 = i["href"]
                except Exception as e:
                    pass
                break

    if url2=="":
        print ("couldn't find")
        # use url as url2
    else:
        if url in url2:
            print (url2)
        else:
            if url2[0]=="/":
                print (url+url2)
            else:
                print (url+"/"+url2)                

# def checkInChildren(city,temp):
#     if temp and city and len(temp.findChildren()):
#         for k in temp.findChildren():
#             if city in k.text.lower():
#                 address = k.text
#                 address_raw,l = checkInChildren(city,k)
#                 if address_raw==None:
#                     if city in address.lower():
#                         address_set.add(address)
#                         break
#         return (None,None)
#     else:
#         return (None,None)

# urls = [
#     "https://valiancesolutions.com/contact-us/",
#     "http://corifictechnologies.com/contact",
#     "https://www.hcltech.com/contact-us/customer",
#     "https://www.wipro.com/en-IN/contact-wipro/",
#     "https://www.kpit.com/contact-us",
#     "https://www.scatech.com/contact-us/overview/",
#     "https://axtria.com/company/contact/",
#     "http://www.qcin.org/contact.php"
#     ]

# for url in urls: 
#     page = requests.get(url).text
#     soup = BeautifulSoup(page,"html.parser")

#     i = soup.find("body")
#     for j in lis:
#         if j["city"] in i.text.lower():
#             checkInChildren(j["city"],i)

#     c = 0
#     for i in address_set:
#         if len(i)<200 and len(i)>20:
#             print (c+1,i,"\n")
#             c+=1
    
#     print ("\n\n\n")