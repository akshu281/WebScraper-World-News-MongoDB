import datetime
import json
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

#check if the urls is valid (http/https)
def validateURL(url):
    if(url.startswith("http")):
        return url
    else:
        return None

#get the date from which the availability has to be checked based on the timedelta Y/M/W/D
def get_check_date(timedelta):
    if(timedelta==None):
        return None
    today=datetime.datetime.now()
    check_date=None
    number=int(timedelta[:-1])
    timespan=timedelta[-1]
    #print(number)
    if(timespan=='Y'):
        check_date=today-datetime.timedelta(days=number*365)
    elif(timespan=='W'):
        check_date=today-datetime.timedelta(weeks=number)
    elif(timespan=='M'):
        check_date=today-datetime.timedelta(days=number*30)
    elif(timespan=='D'):
        check_date=today-datetime.timedelta(days=number)
    else:
        check_data=None
    #print(check_date)
    return check_date

#exclusion for "p" tag elements which are not the actual article content
def exclusions():
    return [r"screen-reader-text",
    r"media__body__label",
    r"util-bar-share-summary-description",
    r"small-12",
    r"linkro-darkred",
    r"mg-b-20",
    r"site-description",
    r"css-1cbhw1y",
    r"hidden",
    r"header-light",
    r"footer-p",
    r"imageCaption",
    r"meta",
    r"submit",
    r"css-12lb1tb",
    r"media__body__label--theme-science_technology",
    r"share-email-success-pane-description",
    r"ui-btn",
    r"e2kc3sl0",
    r"copyright",
    r"caption",
    r"css-1ft1ynw",
    r"util-bar-flyout-subtitle-share",
    r"sharing__text",
    r"nav",
    r"image-credit-wrap",
    r"css-1i0edl6",
    r"header-nav-dropdown-dark-btn",
    r"mol-style-caption",
    r"jp-relatedposts-post-date",
    r"footer__text",
    r"mastDate",
    r"vjs-modal-dialog-description",
    r"bold",
    r"video-item-title",
    r"weather-nav-location-cancel-btn",
    r"partner-scroll-message",
     r"weather-nav-location-name",
     r"c-social-share__title",
     r"appstext",
     r"weather-nav-settings-header",
     r"util-bar-flyout-subtitle-comments",
     r"link",
     r"css-1jp8k9w",
     r"site-nav-firefly-dropdown-text",
     r"weather-nav-location-set-btn",
     r"util-bar-success-description-facebook",
     r"copy",
     r"css-1u889ti",
     r"css-x1m1tm",
     r"mol-para-with-font",
     r"hidden-xs",
     r"media__body__label-programs-icons",
     r"link-newswire",
     r"column",
     r"media__body__label--theme-news",
     r"jp-relatedposts-post-excerpt",
     r"forgetmenot",
     r"author-text",
     r"e1x1pwtg1",
     r"jp-relatedposts-post-context",
     r"util-bar-success-description",
     r"util-bar-flyout-subtitle",
     r"vjs-control-text",
     r"upgrade_browser_msg",
     r"header-nav-dropdown-light-btn"]

#get the region which the url belongs to
def get_region_for_url(url):
    urls=get_regions_with_news_sites()
    for region in urls:
        homepages=region['homepages']
        for homepage in homepages:
            #checking without http or https
            if homepage.split("://")[1] in url.split("://")[1]:
                return region['region']

def download_insights(keyword,insights):
    output_array=[]
    for insight in insights:
        out=insight.copy()
        out['processed_time']=str(insight['processed_time'])
        output_array.append(out)
    fname=keyword+"_output.json"
    with open(fname,"w") as outfile:
        json.dump(output_array,outfile)
