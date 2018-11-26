from pymongo import MongoClient
import datetime
import json
from utils import *
#parent data for regions and the home urls
def get_regions_with_news_sites():
    regions=[{"region":"ANZ","homepages":["https://www.news.com.au/","https://www.nzherald.co.nz/"]},
    {"region":"India","homepages":["https://www.thehindu.com/","https://indianexpress.com/" ,"https://www.deccanchronicle.com/"]},
    {"region":"Singapore","homepages":["https://www.straitstimes.com/" ,"https://www.channelnewsasia.com/" ]},
    {"region":"China","homepages":["http://www.xinhuanet.com/english/","http://www.chinadaily.com.cn/"]},
    {"region":"Russia","homepages":["https://russia-insider.com/en"  ]},
    {"region":"Europe","homepages":["http://www.dailymail.co.uk","https://www.neweurope.eu/","http://www.euronews.com/"]},
    {"region":"US","homepages":["https://www.usatoday.com/","https://www.nytimes.com/" ]},
    {"region":"Nigeria","homepages":["https://www.vanguardngr.com/","http://dailypost.ng/"]},
    {"region":"South Africa","homepages":["https://www.iol.co.za/","https://mg.co.za/" ]},
    {"region":"UAE","homepages":["https://gulfnews.com/" ]},
    {"region":"Mexico","homepages":["https://mexiconewsdaily.com"]}]
    return regions
connection=None

#establish a connection to mongodb hosted at mlab
def connect_to_db():
    global connection
    connection=MongoClient('ds119442.mlab.com',19442)
    db = connection['worldnews']
    db.authenticate('vk', 'starks4nus')
    return db

#close the database connection
def close_connection():
    if(connection!=None):
        connection.close()
#first time, store the homepages and the regions
def store_region_and_urls():
    try:
        db=connect_to_db()
        if(db.homepages.count()==0):
            db.homepages.insert_many(get_regions_with_news_sites())
        else:
            return "Already Exists"
    except Exception as e:
        print(e)
        return "Error"
    close_connection()
    return "Inserted"

#check if the keyword is already present in the log along with the time delta,
#else rreturn false so as to start the scraping process again
def check_if_keyword_present(keyword,timedelta=None):
    check_date=get_check_date(timedelta)
    db=connect_to_db()
    if(check_date==None):
        print("looking for "+keyword.lower())
        if(db.scraped_url_log.find({"keyword":keyword.lower()}).count()>0):
            close_connection()
            return True
        else:
            close_connection()
            return False
    else:
        print("looking for "+keyword.lower()+ " scraped after "+str(check_date))
        if(db.scraped_url_log.find({"keyword":keyword.lower(),'log_time':{"$gte": check_date}}).count()>0):
            close_connection()
            return True
        else:
            close_connection()
            return False

#fetch all the insights based on the time delta
def get_insights(keyword,timedelta=None):
    check_date=get_check_date(timedelta)
    results=[]
    db=connect_to_db()
    if(check_date==None):
        resp=db.insights.find({"parent_keyword":keyword.lower()},{'_id':0})
        if(resp.count()>0):
            for doc in resp:
                results.append(doc)
        close_connection()
        return results
    else:
        print("looking for "+keyword.lower()+" with time")
        results=[]
        resp=db.insights.find({"parent_keyword":keyword.lower(),'processed_time':{"$gte": check_date}},{'_id':0})
        if(resp.count()>0):
            for doc in resp:
                results.append(doc)
        close_connection()
        return results


#save the scrap_log so as to check the time for fetching again or not
def save_urls(all_urls,keyword):
    with open('search_urls_2.txt', 'w') as outfile:
        json.dump(all_urls, outfile)
    db=connect_to_db()
    db.scraped_url_log.update({"keyword":keyword.lower()},{"$set":{"keyword":keyword.lower(),"log_time":datetime.datetime.now(),"urls":all_urls}},upsert=True)
    close_connection()

def save_article_to_db(article):
    db=connect_to_db()
    db.articles.update({'url':article['url']},{"$set":article},upsert=True)
    #db.articles.insert(article)
    close_connection()

def save_insights_to_db(insight):
    db=connect_to_db()
    db.insights.update({'url':insight['url']},{"$set":insight},upsert=True)
    close_connection()

#retrive articles after the check date
def fetch_articles(keyword,timedelta=None):
    check_date=get_check_date(timedelta)
    db=connect_to_db()
    results=[]
    if(check_date==None):
        print("fetching for" + keyword.lower())
        resp=db.articles.find({"parent_keyword":keyword.lower()},{'_id':0})
        results=[]
        for doc in resp:
            results.append(doc)
        close_connection()
    else:
        print("fetching for" + keyword.lower())
        resp=db.articles.find({"parent_keyword":keyword.lower(),'scraped_time':{"$gte": check_date}},{'_id':0})
        results=[]
        for doc in resp:
            results.append(doc)
        close_connection()
        return results

#store_region_and_urls()
