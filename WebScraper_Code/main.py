from db_service import *
from search_phantom import keyword_search
from news_scraper import *
from analyser import *
from utils import *
import sys
#keyword and time delta input from command line arguments. !
keyword = sys.argv[1]
#assumption timedelta representing the relevance of the scraped data Y-Year, M-Month W-Week D-Day
if(len(sys.argv)>2):
    timedelta = sys.argv[2]
else:
    timedelta = None #M,W,D
#do the checking for the keyword and fetch insights directly
def start_process(keyword,timedelta):
    if(check_if_keyword_present(keyword,timedelta)):
        #if keyword exist, check for existence of insights
        print("Keyword Already Exists ")
        print("Checking for insights ")
        insights=get_insights(keyword,timedelta)
        #if insights doesn't exist, fetch the articles in that timeframe and pass it on to analytics
        if(len(insights)==0):
            print("Uh oh !! No insights found ! Lets get this done ! ")
            articles=fetch_articles(keyword,timedelta)
            analyse(articles)
            insights=get_insights(keyword,timedelta)
            download_insights(keyword,insights)
        else:
            #use the insights in desired way.. #currently csv is downloaded and used in tableau
            print("We have got the results for you ! ")
            #download insights to the csv file
            download_insights(keyword,insights)
        print("Please Check the "+keyword+"_output.json file")
    else:
        #looking for a new keyword
        print("Seems you are looking for something new.. ! ")
        print("Hold On !! ")
        #google search and get related urls
        all_urls=keyword_search(keyword)
        #save the url log in the db
        save_urls(all_urls,keyword)
        all_urls=load_data()
        #use the urls and crawl the articles
        parse_articles(all_urls,keyword)
        #fetch articles and pass it on to analytics
        articles=fetch_articles(keyword,timedelta)
        analyse(articles)
        #fetch the analysed inputs and proceed further
        insights=get_insights(keyword,timedelta)
        #download insights to csv file
        download_insights(keyword,insights)
        print("We have got the results for you ! ")
        print("Please Check the "+keyword+"_output.json file")
start_process(keyword,timedelta)
