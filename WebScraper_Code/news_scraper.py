from db_service import *
from selenium import webdriver
from bs4 import BeautifulSoup as soup
from utils import validateURL,exclusions
import json
import time
import datetime
import re
from urllib.parse import unquote
all_urls=[]

def load_data():
    global all_urls
    print("Loading all urls")
    with open("search_urls_2.txt","r") as infile:
        all_urls=json.load(infile)
    return all_urls


def find_header(soup_content):
    print("Finding Headers")
    try:
        #print("looking for h1 with class")
        heads=soup_content.find('h1',{'class':re.compile(r'head|title',re.IGNORECASE)})
        if(heads==None):
            #print("looking for h1 without class")
            heads=soup_content.find('h1')
            if(heads==None):
                #print("looking for h2")
                heads=soup_content.find('h2',{'class':re.compile(r'head|title',re.IGNORECASE)})
                if(heads==None):
                    #print("looking for div")
                    heads=soup_content.find('div',{'class':re.compile(r'head|title',re.IGNORECASE)})
                    if(heads==None):
                        #print("looking for p")
                        heads=soup_content.find('p',{'class':re.compile(r'head|title',re.IGNORECASE)})
        return (heads,None if heads==None else heads.get_text())
    except Exception as e:
        print(e)
        return None

def find_time(soup_content):
    try:
        elem=soup_content.find_all(["span","p","div","time"],{'class':re.compile("time*|date*")})
        #print(elem)
        for el in elem:
            #if(elem!=None):
            if(re.search(r'\d',el.get_text())):
                return el.get_text()
    except Exception as e:
        print(e)
        return None


""" not used
def find_image(soup_content):
    try:
        imgs=soup_content.find_all('img',attrs={'src':True})
        for img in imgs:
            return img['src']
    except:
        return None
"""
def find_content_text(header,soup_content):
    # with open("para.txt","a") as pfile:
    #     paragraphs=soup_content.find_all("p")
    #     data=dict({"head":header.get_text(),"content":""})
    #     for p in paragraphs:
    #         data["content"]+=str(p.get_text().encode("utf-8"))
    #     json.dump(data,pfile)

    # article_holder=soup_content.find('article')
    # paragraphs_container=None
    # if(article_holder==None):
    #     print("no article tag")
    #     content_holder=header.find_next('div',{'id':re.compile('articleBody|story-content*|story*|content*',re.IGNORECASE)})
    #     if(content_holder==None):
    #         print("no content with id")
    #         content_holder=soup_content.find('div',{'class':re.compile('article*|story-content*|story*|content*',re.IGNORECASE)})
    #     paragraphs_container=content_holder
    # else:
    #     #print(article_holder.get_text())
    #     for content in article_holder.find_all("p"):
    #         print(content.get_text())
    # else:
    #     paragraphs_container=article_holder
    exclusion=exclusions()
    paragraphs=soup_content.find_all("p")
    #temp log in local file for validation
    with open("para.txt","a") as pfile:
        data=dict({"head":header.get_text(),"classes":[],"content":""})
        for p in paragraphs:
            if(p.has_attr("class")):
                if(not any(i in p['class'] for i in exclusion)):
                    data["content"]+=str(p.get_text())
                    data["classes"].extend(p['class'])
            else:
                data["content"]+=str(p.get_text())
        json.dump(data,pfile)
    return data['content']

def parse_content(url):
    url = unquote(url)
    print("Fetching for - "+url)
    browser = webdriver.PhantomJS()
    browser.get(url)
    #time.sleep(4)
    content=browser.page_source
    soup_content=soup(content,'html.parser')
    header,text=find_header(soup_content)
    #print(text)
    time=find_time(soup_content)
    #print(time)
    content=find_content_text(header,soup_content)
    browser.quit()
    return {"header":text,"time":time,"content":content}

def parse_articles(all_urls,keyword):
    print("Starting the Scraping Process..\n  It might take some time.. \n Have a cup of coffee and be back.. \n You wont be disappointed !")
    for url_continer in all_urls:
        urls_list=list(url_continer['searched_urls'])
        #print(urls_list)
        for url in urls_list:
            try:
                parsed_content=parse_content(url)
                parsed_content['url']=url
                parsed_content['scraped_time']=datetime.datetime.now()
                parsed_content['parent_keyword']=keyword.lower()
                save_article_to_db(parsed_content)
                time.sleep(3)
            except Exception as e:
                print(e)
    return "Done"
