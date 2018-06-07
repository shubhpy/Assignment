from bs4 import BeautifulSoup
import requests
import re

from mainApp.csIndia import csIndia as lis

def checkInChildren(city,temp,address_set):
    if temp and city and len(temp.findChildren()):
        for k in temp.findChildren():
            if city in k.text.lower():
                address = k.text
                address_raw,l = checkInChildren(city,k,address_set)
                if address_raw==None:
                    weird_condition1 = (city=="agra" and "instagram" in address.lower())
                    if city in address.lower() and (not weird_condition1):    
                        address = re.sub(r"\n+", "\n", address)
                        address = re.sub(r" +", " ", address)
                        address_set.add(address.strip())
                    break
        return (None,None)
    else:
        return (None,None)

def getAddress(url):
    address_set = set()    
    try:
        page = requests.get(url,timeout=15).text
    except Exception as e:
        print ("url is not accessible",e.__str__())        
        return {"success":False,"address_list":[],"message":"url is not accessible"}
    
    try:
        soup = BeautifulSoup(page,"html.parser")
        soup = soup.encode('utf8')
        print ("got url2 soup")
        i = soup.find("body")
        for j in lis:
            if j["city"] in i.text.lower():
                checkInChildren(j["city"],i,address_set)

        c = 0
        address_list = list()
        if len(address_set):
            for i in address_set:
                # if len(i)<200 and len(i)>20:
                address_list.append(i)
                print (c+1,i,"\n")
                c+=1
        else:
            # print (re.findall(r"\+\d{2}\s?0?\d{10}",str(soup)))
            address_list = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}",str(soup))
            address_list = list(set(address_list))
        # print ("\n\n\n")
        if len(address_list):
            return {"success":True,"address_list":address_list,"message":"Got " + str(len(address_list)) }
        else:
            return {"success":False,"address_list":address_list,"message":"Got 0"}
    except Exception as e:
        return {"success":False,"address_list":list(),"message":e.__str__()}        

# for url in urls:
def mainMethod(url):
    if "http" not in url:
        url = "http://" + url.lower().strip()
    else:
        url = url.lower().strip()

    try:
        print (url)
        page = requests.get(url,timeout=15).text
    except Exception as e:
        print ("url is not accessible",e.__str__())
        return {"success":False,"address_list":list(),"message":"url is not accessible"}
    try:
        soup = BeautifulSoup(page,"html.parser")
        soup = soup.encode('utf8')
        # for i in soup.findAll(href=True):
        #     for j in ["contact"]:
        #         if j in i["href"].lower() or j in i.text.lower():
        #             print (i)
        #             url2 = i["href"]
        #             break
        
        url2 = ""
        for i in soup.findAll(href=True):
            for j in ["contact"]:
                if j in i["href"].lower():
                    url2 = i["href"]
                    break
        
        if url2=="":
            print ("couldn't find contact page")
            # Lets get something on about page
            for i in soup.findAll(href=True):
                for j in ["about"]:
                    if j in i["href"].lower():
                        url2 = i["href"]
                        break
            # use url as url2
        else:
            if "http" not in url2:
                if url2[0]=="/":
                    url2 = url+url2
                else:
                    url2 = url+"/"+url2
        
        print (url2)
        if url2!="":    
            return getAddress(url2.strip())
    except Exception as e:
        return {"success":False,"address_list":list(),"message":e.__str__()}

urls = [
    # "https://valiancesolutions.com",
    # "http://corifictechnologies.com",
    # "https://www.hcltech.com",
    # 'http://wikitravel.org',
    # 'https://w3.org',
    # 'Shiksha.com',
    # 'http://upperstall.com/',
    # "https://www.wipro.com",
    # "https://www.kpit.com",
    # "https://www.scatech.com",
    # "https://axtria.com",
    # "http://www.qcin.org"
    # 'www.sunsilkgangofgirls.com'
    # 'www.wcd.nic.in',
    
    # 'www.accel-india.com',
    # 'www.adsi-us.com',
    # 'www.apar.com',
    # 'www.apcc.com',
    # 'www.daxil.com',
    # 'www.aptech-worldwide.com',
    # 'www.autodesk.com',
    # 'www.baan.com',
    # 'www.bdpsindia.com',
    # 'www.bflsoftware.com',
    # 'www.bitechm.com',
    # 'www.bslindia.com',
    # 'www.birlasoft.com',
    # 'www.bsil.com',
    # 'www.bplglobal.com',
    # 'www.iflexsolution.com',
    # 'www.citibank.com',
    # 'www.cmcltd.com',
    # 'www.cms.co.in',
    # 'www.cognizant.com',
    # 'www.ca.com',
    # 'www.datacraft-asia.com',
    # 'www.dataproinfoworld.com',
    # 'www.dbups.com',
    # 'www.deldot.com',
    # 'www.digitalindiasw.com',
    # 'www.dlink-india.com',
    # 'www.epson.co.in',
    # 'www.hclinfosystems.com',
    # 'www.hp.com',
    # 'www.ibm.com',
    # 'www.itil.com',
    # 'www.infy.com',
    # 'www.zensar.com',
    # 'www.itsindia.com',
    # 'www.ltitl.com',
    # 'www.lccinfotech.com',
    # 'www.lgsi.co.in',
    # 'www.lotus.com',
    # 'www.mahindraconsulting.com',
    # 'www.monitorsindia.com',
    # 'www.netsol.co.in',
    # 'www.nexuscomputers.com',
    # 'www.nortelnetworks.com',
    # 'www.novell.com',
    # 'www.patni.com',
    # 'www.pcsil.com',
    # 'www.pentamedia-grafix.com',
    # 'www.pentafour.com',
    # 'www.polaris.co.in',
    # 'www.rolta.com',
    # 'www.samsungindia.com',
    # 'www.sap.com',
    # 'www.satyam.com',
    # 'www.sasi.com',
    # 'www.silverline.com',
    # 'www.ssil-india.com',
    # 'www.sqlstarintl.com',
    # 'www.sumitindia.com',
    # 'www.tataelxsi.com',
    # 'www.tatainfotech.com',
    # 'www.tata.com',
    # 'www.tulipsoftware.com',
    # 'www.vxl.com',
    # 'www.wellwin-india.com'
    ]