import requests
from bs4 import BeautifulSoup
import re
import webbrowser as wb
from string import punctuation
import codecs

def asci_encoder(find):
    new_find = ""
    special = set(punctuation)
    special.add(' ')
    for ch in find:
        if ch in special:
            new_find +="%"+str(codecs.encode(str.encode(ch), "hex"),"ascii")
        else:
            new_find += ch
    return new_find

def savecheck(url):
    websaved=readinfo()
    for page in websaved:
        if(page[0]==url):
            return page[1]

def findparam(url):
    name=""
    website=re.search("(https://|http://)(\w+\.)*(.+(?=\.))(\..+)(?=\?)",url)
    shorted=url[website.span()[1]:]
    if "&" in shorted:
        shorted=shorted.split("&")
    else:
        shorted=[shorted]
    for arguments in shorted:
        if "test" in arguments:
            values=arguments.split("?")
            name=values[1].split("=")[0]
            break
    nickname=input("Enter the name for saved page: ")
    saveinfo(nickname, f"{website.group()}?{name}=")
            
def saveinfo(nick, link):
    stored=open("stored.txt",'a')
    stored.write(f"{nick} {link}\n")
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
    if(not re.match("https://|http://",adr)):
        adr=f"https://{adr}"
    if(not checkurl(adr)):
        if(re.match("(https://|http://)(\w+\.)*(.+)",adr)):
            print("Domain name like (.com) is missing from the given website.")
            domain=input("Use .com as the domain?(Y(default)/Insert custom domain)").lower()
            if(domain=="y" or domain=="" or domain=="yes"):
                adr=f"{adr}.com"
            else:
                if(domain[0]=="."):
                    adr=f"{adr}{domain}"
                else:
                    adr=f"{adr}.{domain}"
    return adr

def getlink(adr):
    name=""
    action=""
    response = requests.get(adr)
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
    if("http" in action):
        return(f"{action}?{name}=")
    else:
        return(f"{adr}{action}?{name}=")

def browse(adr, find):
    issaved=savecheck(adr)
    if(issaved==None):
        if(not checkurl(adr)):
            adr=fixurl(adr)
        fullsearch=getlink(adr)
        wb.open(f"{fullsearch}{find}")
        savename=input(f"Would you like to save this website?(Enter name for website {adr} or leave blank)")
        if(savename!=""):
            saveinfo(savename,fullsearch)
    else:
        wb.open(f"{issaved}{find}")
