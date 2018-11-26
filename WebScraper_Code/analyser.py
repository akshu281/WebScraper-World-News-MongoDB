from textblob import TextBlob
from gensim.summarization.summarizer import summarize
from gensim.summarization import keywords
import rake_nltk as rake
import operator
from utils import get_region_for_url
from db_service import *
import datetime

#filter articles for certain size of content.. 200 words or 7 new lines , or 10 sentences
def filter_content(articles):
    filtered=[]
    for article in articles:
        if(len(article['content'].split(" "))>200 or len(article['content'].split("\n"))>7 or len(article['content'].split("."))>10 ):
            filtered.append(article)
    return filtered

#extract the keywords from the passed text
def keyword_extraction(text):
    stoppath = 'data/stoplists/SmartStoplist.txt'
    rake_object = rake.Rake(stoppath,5,3,4)
    keywords = rake_object.run(text)
    final_list = list()
    for key in keywords:
        if(key[1]>=4.5):
            final_list.append(key[0])
            print(key[0])
        else:
            break
    return final_list

#summarize the passed text
def summarize_and_extract_keywords(text):
     print(summarize(text, ratio=0.1))
     return summarize(str(text),ratio=0.1),keywords(str(text), ratio=0.01)

#find polarity and subjectivity of the passed text
def find_polarity_and_subjectivity(article_content):
    blob=TextBlob(article_content)
    return blob.sentiment

def analyse(articles):
    #filter articles
    print("Found "+str(len(articles))+" articles")
    print("Starting the Analysis Process..\n  It might take some time.. \n Have a cup of coffee and be back.. \n You wont be disappointed !")
    filtered=filter_content(articles)
    #analyse
    analysis_results=[]
    for article in filtered:
        try:
             analysed_content={"url":article['url'],"parent_keyword":article['parent_keyword'],"processed_time":datetime.datetime.now(),"region":get_region_for_url(article['url']),"keywords":"","subjectivity":"","polarity":"","summary":""}
             summary,keywords=summarize_and_extract_keywords(str(article['content']))
             polarity, subjectivity = find_polarity_and_subjectivity(str(article['content']))
             analysed_content['summary']=summary if summary!=None or summary!="" else article['content']
             analysed_content['keywords']=keywords.split("\n")
             analysed_content['polarity']=polarity
             analysed_content['subjectivity']=subjectivity
             #save the insights to db. 
             save_insights_to_db(analysed_content)
        except Exception as e:
            print(e)
