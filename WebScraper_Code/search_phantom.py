from selenium import webdriver
from bs4 import BeautifulSoup as soup
from utils import validateURL
import json
import time
import datetime
import re
from urllib.parse import unquote
from db_service import get_regions_with_news_sites
browser = webdriver.PhantomJS()
regions=get_regions_with_news_sites()
all_urls=[]
def keyword_search(keyword):
    global all_urls
    for region in regions:
        print(region['region'])
        for i in region['homepages']:
            searched_results=dict()
            searched_results={'url':i,'searched_urls':[]}
            #print(i)
            searchGoogle = "https://www.google.com.np/#q=site://"+i+" "+keyword
            browser.get(searchGoogle)
            time.sleep(4)
            content=browser.page_source
            souped_page=soup(content,'html.parser')
            #print(content)
            header=souped_page.find_all('h3',{'class':'r'})
            for head in header:
                url_clumsy=head.find('a')['href']
                #print(url_clumsy)
                final_url=url_clumsy.split("q=")[1].split("&sa=U")[0]
                #remove topic and tag all_urls
                if("/tags/" in final_url or "/tag/" in final_url  or "/topics" in final_url or "/topic/" in final_url):
                    pass
                else:
                    if(validateURL(final_url)!=None):
                        searched_results['searched_urls'].append(unquote(final_url))
            all_urls.append(searched_results)
    return all_urls
"""

def find_header(soup_content):
    try:
        print("looking for h1 with class")
        heads=soup_content.find('h1',{'class':re.compile(r'head|title',re.IGNORECASE)})
        if(heads==None):
            print("looking for h1 without class")
            heads=soup_content.find('h1')
            if(heads==None):
                print("looking for h2")
                heads=soup_content.find('h2',{'class':re.compile(r'head|title',re.IGNORECASE)})
                if(heads==None):
                    print("looking for div")
                    heads=soup_content.find('div',{'class':re.compile(r'head|title',re.IGNORECASE)})
                    if(heads==None):
                        print("looking for p")
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



def find_image(soup_content):
    try:
        imgs=soup_content.find_all('img',attrs={'src':True})
        for img in imgs:
            return img['src']
    except:
        return None

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
    exclusion=['screen-reader-text', 'media__body__label', 'util-bar-share-summary-description', 'small-12', 'linkro-darkred', 'mg-b-20', 'site-description', 'css-1cbhw1y', 'hidden', 'header-light', 'footer-p', 'imageCaption', 'meta', 'submit', 'css-12lb1tb', 'media__body__label--theme-science_technology', 'share-email-success-pane-description', 'ui-btn', 'e2kc3sl0', 'copyright', 'caption', 'css-1ft1ynw', 'util-bar-flyout-subtitle-share', 'sharing__text', 'nav', 'image-credit-wrap', 'css-1i0edl6', 'header-nav-dropdown-dark-btn', 'mol-style-caption', 'jp-relatedposts-post-date', 'footer__text', 'mastDate', 'vjs-modal-dialog-description', 'bold', 'video-item-title', 'weather-nav-location-cancel-btn', 'partner-scroll-message', 'weather-nav-location-name', 'c-social-share__title', 'appstext', 'weather-nav-settings-header', 'util-bar-flyout-subtitle-comments', 'link', 'css-1jp8k9w', 'site-nav-firefly-dropdown-text', 'weather-nav-location-set-btn', 'util-bar-success-description-facebook', 'copy', 'css-1u889ti', 'css-x1m1tm', 'mol-para-with-font', 'hidden-xs', 'media__body__label-programs-icons', 'link-newswire', 'column', 'media__body__label--theme-news', 'jp-relatedposts-post-excerpt', 'forgetmenot', 'author-text', 'e1x1pwtg1', 'jp-relatedposts-post-context', 'util-bar-success-description', 'util-bar-flyout-subtitle', 'vjs-control-text', 'upgrade_browser_msg', 'header-nav-dropdown-light-btn']
    paragraphs=soup_content.find_all("p")
    with open("para.txt","a") as pfile:
        #data=dict({"head":header.get_text(),"classes":[],"content":""})
        for p in paragraphs:
            if(p.has_attr("class")):
                if(not any(i in p['class'] for i in exclusion)):
                    data["content"]+=str(p.get_text().encode("utf-8"))
                    data["classes"].extend(p['class'])
            else:
                data["content"]+=str(p.get_text().encode("utf-8"))
        json.dump(data,pfile)
    #return data

def parse_content(url):
    url = unquote(url)
    print("Fetching for"+url)
    browser.get(url)
    #time.sleep(4)
    content=browser.page_source
    soup_content=soup(content,'html.parser')
    header,text=find_header(soup_content)
    print(text)
    time=find_time(soup_content)
    print(time)
    content=find_content_text(header,soup_content)
    #print(title)
    # parsed_content=find_content(soup_content)
    #article_time=find_time(soup_content)
    #print(article_time)
    #data_to_store={"title":title,"content":parsed_content,"time":str(article_time),'scrapedtime':str(datetime.datetime.now())}
    #print(data_to_store)

def fetch_data(keyword):
    with open('search_urls_2.txt', 'w') as outfile:
        response=keyword_search(keyword)
        json.dump(response, outfile)

def load_data():
    global all_urls
    with open("search_urls_2.txt","r") as infile:
        all_urls=json.load(infile)


#fetch_data()
# fetch_data("Solar Probe")
#load_data()

def parse_articles(all_urls):
    for url in all_urls:
        urls_list=list(url['searched_urls'])
        #print(urls_list)
        if(len(urls_list)>0):
            search_page=urls_list[0]
            parse_content(search_page)
    # for search_page in url['searched_urls']:
    #     parse_content(search_page)
"""
