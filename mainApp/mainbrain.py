from bs4 import BeautifulSoup
import requests
import re
import time

# from mainApp.csIndia import csIndia as lis
# from mainApp.csWorld import csWorld as lis
from mainApp.csWorld_gt4 import csWorld_gt4 as lis

def verify_city(address,city):
    for i in [" ","\n"," ","-"]:
        if i+city in address.lower() or city+i in address.lower():
            return True
    return False

def analyseAddress(city,address,address_set):
    address = re.sub(r"\n+", "\n", address)
    address = re.sub(r" +", " ", address)
    
    # c = address.lower().find(city)
    # print(city)
    # address = address[:c][-200:] + address[c:][:200]
    # print(address)
    # print (city)

    imp_condition1 = verify_city(address.lower(),city)
    # print (address)
    # imp_condition1 = True
    if len(address)<300 and len(address)>20 and imp_condition1:
        remove_address = list()
        toAdd = True
        for i in address_set:
            if address in i:
                toAdd = False
                break
            elif i in address:
                toAdd = True
                remove_address.append(i)
        
        for i in remove_address:
            address_set.remove(i)
        if toAdd:
            address_set.add(address)

def checkInChildren(city,temp,address_set):
    if temp and city and len(temp.findChildren()):
        for k in temp.findChildren():
            if city in k.text.lower():
                address = k.text
                address_raw,l = checkInChildren(city,k,address_set)
                if address_raw==None:
                    if city in address.lower():
                        analyseAddress(city,address.strip(),address_set)
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
        return list()

    try:
        soup = BeautifulSoup(page,"html.parser")
        # soup = soup.encode('utf8')
        print ("got url2 soup")
        time.sleep(1)
        i = soup.find("body")
        time.sleep(1)        
        lis.append({"city":"address"})
        if i:
            for j in lis:
                if j["city"] in i.text.lower():
                    print(j["city"])
                    checkInChildren(j["city"],i,address_set)
        
        c = 0
        address_list = list()
        if len(address_set):
            address_list = list(address_set)
            # for i in address_set:
            #     if len(i)<200 and len(i)>20:
            #         address_list.append(i)
            #         print (c+1,i,"\n")
            #         c+=1
        else:
            # print (re.findall(r"\+\d{2}\s?0?\d{10}",str(soup)))
            email_address_list = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}",str(soup))
            address_list += list(set(email_address_list))
        # print ("\n\n\n")
        
        if len(address_list):
            return address_list
        else:
            return list()
            
    except Exception as e:
        return list()

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
        return {"success":False,"error":True,"address_list":list(),"message":"url is not accessible"}
    try:
        soup = BeautifulSoup(page,"html.parser")
        time.sleep(1)        
        complete_address_list = list()

        url2_list = list()
        for i in soup.findAll(href=True):
            for j in ["contact"]:
                if j in i["href"].lower():
                    url2_list.append(i["href"])
                elif not i.findChild():
                    if j in i.text.lower():
                        url2_list.append(i["href"])

        if not len(url2_list):
            print ("couldn't find contact page")
            # Lets get something on about page
            for i in soup.findAll(href=True):
                for j in ["about"]:
                    if j in i["href"].lower():
                        url2_list.append(i["href"])
                    elif not i.findChild():
                        if j in i.text.lower():
                            url2_list.append(i["href"])
        else:
            url2_list = list(set(url2_list))
            print (url2_list)
            for url2 in url2_list:
                if "http" not in url2:
                    if url2[0]=="/" or url[-1]=="/":
                        url2Final = url+url2
                    else:
                        url2Final = url+"/"+url2
                else:
                    url2Final = url2

                print (url2Final)
                if url2Final!="":
                    addr_list = getAddress(url2Final.strip())
                    complete_address_list+=addr_list

        if not len(complete_address_list):
            addr_list = getAddress(url.strip())
            complete_address_list+=addr_list
        
        if len(complete_address_list):
            return {"success":True,"error":False,"address_list":list(set(complete_address_list)),"message":"Got " + str(len(complete_address_list))}
        else:
            return {"success":False,"error":False,"address_list":list(set(complete_address_list)),"message":"Got " + str(len(complete_address_list))}
            
    except Exception as e:
        return {"success":False,"error":True,"address_list":list(),"message":e.__str__()}

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