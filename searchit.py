import requests
import urllib.request
from bs4 import BeautifulSoup
import re
import webbrowser as wb
import sys

def saveinfo(nick, url, name, action):
    stored=open("stored.txt",'a')
    stored.write(nick+" "+url+" "+name+" "+action+"\n")
    stored.close()
        
def readinfo():
    try:
        stored=open("stored.txt",'r')
        saved=stored.readlines()
        stored.close()
    except FileNotFoundError:
        saved=[]
    for i in range(len(saved)):
        saved[i]=saved[i].split()
    return saved
        
def checkurl(adr):
    return re.match("(https://|http://)(\w+\.)*(.+(?=\.))(\..+)",adr)

def fixurl(adr):
    if(not re.match("https://|http://",url)):
        adr="https://"+adr
    if(not checkurl(adr) and adr[-1]=="."):
        adr=adr[0:-1]
    if(not checkurl(adr)):
        if(re.match("(https://|http://)(\w+\.)*(.+)",adr)):
            print("Domain name like (eg. .com) is missing from the given website.")
            domain=input("Use .com as the domain?(Y/Insert custom domain)").lower()
            if(domain=="y" or domain==""):
                adr=adr+".com"
            else:
                adr=adr+domain
    if(checkurl(adr)):
        return adr
    else:
        if(input("The url is still broken. Attempt repair again or try using the given address ?(Y/N)").lower()=="y"):
            fixurl(adr)
        else:
            return adr

def siteinfo(adr):
    name=""
    action=""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    forms=soup.find_all("form")
    for form in forms:
        inputs=form.find_all("input")
        for urlinput in inputs:
            name=urlinput.get("name")
            inputtype=urlinput.get("type")
            autocomplete=urlinput.get("autocomplete")
            if(name != None and (inputtype == "text" or inputtype=="search")):
                action=form.get("action")
                break
            if(name != None and autocomplete != None):
                action=form.get("action")
                break
        if(action!=""):
            break
    if(action==""):
        print("Unable to find correct search parameters. Attempting common approach.")
        action="/search"
        name="q"
    
    return (name,action)

websaved=readinfo()
issaved=False
islinked=False
sys.argv.pop(0)
url=sys.argv[0]

sys.argv.pop(0)
search="+".join(sys.argv)
    
for webpage in websaved:
    if(webpage==[]):
        continue
    if(url==webpage[0]):
        url=webpage[1]
        name=webpage[2]
        action=webpage[3]
        issaved=True
        break

if(issaved==False):
    if(not checkurl(url)):
        url=fixurl(url)

    name, action=siteinfo(url)
 
    
if("https" in action or "http" in action):
    final=action+"?"+name+"="+search
else:
    final=url+action+"?"+name+"="+search

wb.open(final)

if(issaved==False):
    for link in websaved:
        if(link[1]==url):
            islinked=True
            break
    if(islinked==False):
        wantsave=input("Would you like to save this website?(Enter name for website "+url+" or leave blank)")
        if(wantsave!=""):
            saveinfo(wantsave,url,name,action)

# amazon would work but BeautifulSoup can't get the page properly. Can be added manually if needed.
