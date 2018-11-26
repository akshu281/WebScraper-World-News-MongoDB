# from pymongo import MongoClient
# connection=MongoClient('ds119442.mlab.com',19442)
# db = connection['worldnews']
# db.authenticate('vk', 'starks4@nus')
# db.articles.update({},{'$set':{"parent_keyword":"singapore trump summit"}},multi=True)

# bytestring="People\\xe2\\x80\\x99s Republic of Korea (DPRK), a ruthless dictator, and the other the reality show host turned US President.'b'They shook hands and smiled. The handshake lasted 13 seconds and was without any of the vigorous antics other world leaders have endured from Mr Trump.'b'Nothing could ever be taken for granted or assumed, Mr Trump said \\xe2\\x80\\x94 but he had been a deal maker \\xe2\\x80\\x9cmy whole life\\xe2\\x80\\x9d and \\xe2\\x80\\x9cit\\xe2\\x80\\x99s my thing\\xe2\\x80\\x9d.'b'He added: \\xe2\\x80\\x9cYou can\\xe2\\x80\\x99t ensure anything. All I can say is that they want to make a deal. That\\xe2\\x80\\x99s what I do. My whole life has been deals. I\\xe2\\x80\\x99ve done great at it. That\\xe2\\x80\\x99s what I do. And I know when somebody wants to deal and I know when somebody doesn\\xe2\\x80\\x99t. A lot of politicians don\\xe2\\x80\\x99t.\\xe2\\x80\\x9d'b'There were plenty of sledges of former US presidents, from Bill Clinton \\xe2\\x80\\x94"
# print(bytestring.decode('utf16'))

import requests
from selenium import webdriver
from bs4 import BeautifulSoup as soup
import chardet
from  db_service import *
import datetime
import utils
from news_scraper import *
from analyser import *
# print(datetime.datetime.now()-datetime.timedelta(weeks=1))
#
#print(check_if_keyword_present("singapore trump summit","1D"))
#browser = webdriver.PhantomJS()
#
# browser.get("https://www.news.com.au/technology/science/space/nasa-poised-to-launch-first-sunskimming-spaceship/news-story/d0390f5ca020de85be2770787b13b3b4")
#
# #time.sleep(4)
# content=browser.page_source
#
# soup_content=soup(content,"html.parser")
# ps=soup_content.find_all("p")
# strnp=""
# for p in ps:
#     strnp+=str(p.get_text())
#
# print(strnp)



#
# strn="""For Donald Trump, ratings, approval and support are a big deal. The US President has frequently disputed that his election opponent won more votes than he did and his predecessor drew a bigger inauguration crowd. He has taken time out from the biggest job on the planet to feud on Twitter with Arnold Schwarzenegger over ratings for The Apprentice. During a speech to Congress, his idea of offering comfort to a dead Navy Seal's widow after she received a standing ovation was to say her husband was \"very happy, because I think he just broke a record\". So, weeks of job approval ratings, chronically low for a new US president, must have been hard to stomach. Gallup figures showing Trump at 37 and 38 per cent approval have been widely shared among politicos on the President's social media of choice, Twitter. And polls showed sliding support among groups of voters for Trump and his policies. When combined with daily doses of bad news about the Russia investigation, stalled healthcare reform, legal blocks to immigration moves, insider leaking and Trump Administration chaos, it was clear change was required. Unpopularity makes it harder for a president to push through programmes and easier for opponents to obstruct. The story of the Trump campaign's ties to Russia, illustrated in ever-widening web lines in graphics, has become the President's own email server saga millstone. What could shift it? On Friday, as US cruise missiles punched holes in hangars on the Syria regime's Shayrat base, a widely-shared Trump tweet from October 9, 2012 hinted at a possible parallel playing out: \"Now that Obama's poll numbers are in tailspin - watch for him to launch a strike in Libya or Iran. He is desperate.\" Trump's cruise missile strikes days after an apparent chemical weapons attack in the town of Khan Sheikhoun need to be seen in the context of his domestic political woes and his background on the Syrian civil war. Eleven weeks into his presidency, Trump is attempting a reset, trying to boost his popularity and control the agenda. He wants to change the conversation from the Russia probe and the allegation he is President Vladimir Putin's puppet. The strikes are part of it, so is generally creating a perception of 'winning', being decisive, being taken more seriously, presenting messages more competently and having the right advisers. So far, in the past few days, it is working. REACTION TO THE RETALIATION Although the speed of the retaliation was a surprise, the action wasn't to pundits who have seen it all before from previous leaders. Harvard professor Stephen Walt tweeted on Thursday: \"I don't know what Trump will do re Syria. But I'm betting it will be some loud, well-publicised, and strategically meaningless airstrikes.\" With the missile strikes, Trump has had the best couple of days of his presidency. On the face of it, he has taken unusually quick, decisive action on an issue that gives him a chance to show empathy and people generally agree on. The taboo on chemcal weapons is worth upholding, right? Both the Washington establishment and mainstream US media have largely been sympathetic. A poll boost is sure to follow. Foreign leaders have expressed support. His former opponent Hillary Clinton in an interview on Friday called for strikes against Syrian airfields. The Republican Senate Majority Leader Mitch McConnell said \"the era of American passivity is over\". Democrat leader in the House Nancy Pelosi called Trump's strikes a \"proportional response\". Former Obama Administration ambassador to Israel, Dan Shapiro, called them \"correct and well executed\". The New York Times and Guardian ran story-behind-the-story articles which bolstered Trump's assertion that he was spurred into action by footage of Syria's suffering people and depicted him as a man of action. The New York Times: \"Trump was already shaken by photos his staff had shown him of children dying ... so the President did not need a lot of convincing ... aides say the images from Syria - especially those showing the suffering of small children and babies - weigh on him ... The first public evidence of the President's concern about the chemical attack comes ... Trump says his horror at the images of 'innocent children, innocent babies' choked by poison gas in the attack has led him to reassess his approach to Syria.\" The Guardian: \"The images had a profound effect on the US President ... 'I will tell you that attack on children yesterday had a big impact on me - big impact,' Trump told reporters ... Trump had criticised Obama for vacillation and weakness. Would he act differently? Within 24 hours Trump's flexibility had translated into direct action ... After weeks in which his Administration had seemed consumed by leaks, in fighting, drift and ineptitude, Trump was moving at speed.\" CNN ran a report with the extremely Trump-friendly headline: \"These are the images that moved President Trump to act in Syria\". Daily Beast and CNN commentator Matt Lewis tweeted: \"Trump can punish Assad, deter future use of chemical weapons, send a message to the world, & still avoid the mess of regime change.\" Presenter with Britain's Channel 4 Matt Frei tweeted: \"With Syria strikes @realDonaldTrump showed 1he can act decisively 2not Russia's puppet 3not Obama 4has humanitarian reflex5 unpredictable.\" As MSNBC host Chris Hayes noted: \"Tonight Trump is getting praise from the very same Establishment he ran against and whose approval he desperately seeks.\" The circumstances surrounding the President's crisis point were significant.Trump dealt with the Syria issue while hosting the Chinese President Xi Jinping. He received a major Congressional victory with the Senate confirming Neil Gorsuch as a Supreme Court justice. And various reports emerged of a staff shake-up, with chief of staff Reince Priebus and strategist Stephen Bannon said to be in trouble. The staffing reports had Trump ordering his aides to sort it out. The message being, man in charge is putting that infighting behind him. TRUMP'S BIG U-TURN ON SYRIA According to the Daily Beast, there had been nine previous suspected chemical weapons attacks in Syria this year, with toxic chlorine gas, as reported by the Syrian Observatory for Human Rights. The Trump Administration had shown no previous desire to take retalitory action. And what about deaths caused by conventional weapons? Remember the agonising fall of Aleppo late last year? Trump's team has been trying hard to get a ban on Syrian refugees - fleeing their brutal dictator - from entering the US. Before he became president, Trump said numerous times in 2013 and 2014 that the US should not bomb Syria. In 2013 former President Barack Obama declared chemical weapon use a red line and then backed down from taking military action in the face of popular and Congressional opposition. In August 2013, chemical weapons were used against people in Ghouta, killing about 1300. Trump tweeted: \"What will we get for bombing Syria besides more debt and a possible long-term conflict?\" And: \"President Obama, do not attack Syria. There is no upside and tremendous downside. Save your 'powder' for another (and more important) day!\" Acting on the latest atrocity - thought to involve sarin gas - gave Trump a chance to shape up in comparison to Obama. Yesterday, press secretary Sean Spicer tweeted a photo of Trump and team at a briefing in what was clearly meant to mirror the famous picture of Obama and officials during the Osama bin Laden raid. Washington Post blogger Paul Waldman tweeted: \"In these foreign policy crises, almost impossible to overestimate the role Trump's desire 2B tougher than Obama will play in his decisions\". Trump called it a \"targeted\" strike \"on the airfield in Syria from where the chemical attack was launched. It is in the vital national security interest of the United States to prevent and deter the spread of chemical weapons\". Syria denies using nerve gas. Trump's speech sounded very much like something George W. Bush could have delivered. \"My fellow Americans\", \"no child of God\", \"end the slaughter\", \"we pray for God's wisdom\", \"America stands for justice\". The only Trumpian note in it was \"beautiful babies\". Trump's sudden concern for Syrians is problematic whether taken at face value or not. Firstly, it is a convenient phenomenon that we can only take his word for. Secondly, it only seems to apply to Syrians killed by chemical weapons. Thirdly, it goes against his background statements and actions towards Syrian refugees. Fourthly, is it a good thing that the President can suddenly change course based on an emotional, gut reaction? Also, as Micah Zenko of the Council of Foreign Relations tweeted: \"That Trump was moved by graphic images to OK the attack won't be lost on all threatened groups seeking US intervention on their behalf.\" WHAT DID THE STRIKES ACHIEVE? For many people hoping for progress in ending the Syrian civil war, none of that will matter. The war is a gaping wound in the world which has destabilised the region and wider Europe. It is a complex conflict seemingly without end that has left people for years looking on feeling frustrated and helpless, or angry at the displaced millions. In reactions to the US strikes, a lot of people commenting on media and social media seemed to be uploading their own emotional projections about the war onto Trump's actions. Some people saw it as appropriate, limited, punishment for the Khan Sheikhoun attack. There was relief from Syrians that the Assad regime had finally taken a hit from the US. Perhaps more would follow. Long-time Syria watchers believed it was strategically good that Trump had demonstrated that military force was on the table. Obama's unwillingness to battle Bashar al-Assad as well as Isis had been seen as prolonging the war. Perhaps this has opened the door to intervention against the regime after the quarantined approach. Some saw Trump as refilling the Rubicon to deter future use of chemical weapons.Other people focused on whether the strikes were legal, or whether they sent a wider warning to North Korea and China, or whether the US was just repeating ineffective history. Some right-wing supporters of Trump were disappointed that he was not the isolationist they had believed in. It was quickly clear that the strikes were limited in scope and largely symbolic: A mini shock and awe. By Friday night NZT Reuters and AFP were reporting that planes were already using the base to take off on bombing raids in the countryside. By yesterday Khan Sheikhoun was being bombed again. Reports quickly surfaced on Friday from the BBC and ABC that Russians and Syrians were evacuated from the airbase before the strike. The Pentagon confirmed that Russia was notified in advance. Al Jazeera America producer Tony Karon tweeted: \"For anyone who thinks this is start of a war to topple Assad, note the care taken to minimise risk to his forces at target site\". Moscow has promised to strengthen Syria's anti-aircraft defences. It is also suspending a hotline with the US designed to avoid collisions between their planes in Syria. Today Russia sent a warship to boost its battlegroup off the Syrian coast. Considering how both Trump and Putin would benefit from more perceived independence from each other, just how coordinated were the strikes? It is impossible to know just yet. Eurasia Group political scientist Ian Bremmer tweeted: \"Assad gas attack vigorously denied by Kremlin & makes Putin looks weak v Assad (Iran matters..). US-Russia heading for trouble\". Guardian columnist Jonathan Freedland smells a scam. \"How convenient that Trump, under fire for being Vladimir Putin's poodle, now stands up to him in Syria. How neatly this blows away all those allegations of secret links and election hacking. Yes, there have been ample statements of condemnation from Moscow, but those don't cost either side anything. The US appears to have given Russia sufficient warning to ensure their men weren't hit, and Russia used none of its ample capacity to hit back. It all worked out very nicely.\" HOW MUCH WEIGHT DO THEY CARRY? There has been a lot of debate on how much weight these strikes carry. If it is too obviously organised military theatre then can it really enforce a warning to the Syrian regime? Is Trump almost guaranteed to have to go further at some stage? And should Trump suddenly be seen as a 'strong' leader, having dropped 59 cruise missiles worth US$59 million, after decades of war. Zenko tweeted: \"US dropped 26,172 bombs in 2016. How does 59 more suddenly demonstrate US 'resolve,' 'credibility,' + 'leadership?'\" New York Times journalist Max Fisher wrote in a series of tweets: \"Still confused by argument that the US established anti-CW deterrence by demonstrating it will retaliate with negligibly damaging strikes. If this was executed competently and Russia given warnings, then strikes appear largely symbolic. Little impact on regime or its calculus. How exactly did these US strikes establish deterrence? Is this 'punishment' sufficient to change anything?\" Josh Barro of Business Insider asked: \"If you openly signal that the attack was symbolic, doesn't that undermine the symbolism?\" Naval War College professor Tom Nichols tweeted: \"This looks like a pinprick. It pops the balloon of thinking Syria is untouchable, but whether it deters anything is less clear.\" Former US Treasury terror finance analyst Jonathan Schanzer tweeted: \"FWIW, I think a limited, proportional response is a good first move. Doesn't solve Syria, but lets Assad/Iran know we are watching.\" Clifford May of the Foundation for Defence of Democracies tweeted: \"Also let's Russia know we're back in the game. N Korea, too, can no longer bank on US inaction, 'soft power' and talking as only responses.\" WHAT HAPPENS NEXT? For many experts the 'what's next' question is key. University of Maryland professor Shibley Telhami tweeted: \"Within days, Trump's strike will look more and more ineffective, forcing a decision: escalate or live with perception of failure.\" Writer Max Boot tweeted: \"Now what? Is message that US will tolerate Assad as long as he doesn't use CW? Or is this prelude to larger strategy in Syria? If so what?\" Former US ambassador to Russia Michael McFaul said that \"Trump biggest worry now; what if Assad defies him and uses chemical weapons again?\" Head of Foreign Policy Group, David Rothkopf, tweeted: \"Problem re: Trump & mil action is - he's impulsive and not strategic. Taking such action absent clear policies is where biggest risks arise. The 'what's next' component of Syria strike will reveal much about effectiveness & thinking of Mattis, Tillerson, McMaster, Pompeo team.\" Zenko said a 'rosy scenario' could see Assad deterred without the US being drawn further into the civil war. But he said \"I looked at 36 cases of limited US strikes: They achieve military goals 1/2 the time; political goals less than 10%.\" A Middle East veteran writer, Sam Dagher, tweeted: \"Without plan to remove Assad from power US strikes strengthen him as leader confronting Trump aggression.\" The editor of the Atlantic, Jeffrey Goldberg, compared the President with his predecessor: \"Obama was known for an overly cerebral commitment to the notion of strategic patience. Trump seems more committed to a policy of glandular, non-strategic impatience. Obama may have been paralysed by a phobic reaction to the threat posed by the slippery slope. Donald Trump now finds himself dancing at the edge of the slippery slope his predecessor so assiduously avoided.\""""
#
# print(strn)



# articles=fetch_articles("syria civil war")
# for article in articles:
#     print(article['content'])



# insights=[{
#     "_id": {
#         "$oid": "5b79201b4719c870adb627fe"
#     },
#     "url": "https://www.news.com.au/world/middle-east/hell-on-earth-jihadist-rebel-groups-see-fighting-as-the-only-option/news-story/f525bd0f6ab33df2a92cd6973a726ede",
#     "parent_keyword": "syria civil war",
#     "region": "ANZ",
#     "keywords": [
#         "peace",
#         "syrian",
#         "syrians"
#     ],
#     "subjectivity": 0.49955565353713516,
#     "polarity": 0.04099157358416618,
#     "summary": "The exceptions are the Kurdish YPG and the largely weakened Free Syrian Army.All along, Mr Assad\u2019s regime has been claiming it is fighting Islamic State, Al-Qaeda and other Salafi jihadist groups to keep Syria a modern secular state.\nHe may find he is out of his league when things get tough on the ground, forcing him out of Syria.The Syrian conflict will end only if the Russian-supported Assad regime wipes out all Salafi jihadist rebel groups and regains control of western Syria and its most important cities."
# },
# {
#     "_id": {
#         "$oid": "5b79201d4719c870adb62800"
#     },
#     "url": "https://www.news.com.au/world/10-simple-points-to-help-you-understand-the-syria-conflict/news-story/ab4bf33fed028d63990b8e09e6778ee7",
#     "parent_keyword": "syria civil war",
#     "region": "ANZ",
#     "keywords": [
#         "syrian",
#         "syrians",
#         "family",
#         "families",
#         "shanahan"
#     ],
#     "subjectivity": 0.4515239728654364,
#     "polarity": -0.03070000460244364,
#     "summary": "This won\u2019t make you an instant expert, but it\u2019ll sure help.A suicide attack claimed by Islamic State killed more than 40 people in the Kurdish-dominated city of Qamishli in Northern Syria early Wednesday.\nThe Civil War beginsRodger Shanahan says the catalyst was the jailing on March 6, 2011, of some children who painted anti-regime graffiti.\n\u201cLocal areas formed their own militias with the aim of toppling the government without any co-ordination or centralised command or control,\u201d he says.\u201cThe militias were a combination of local area tribal groups, deserters from the military [who had been conscripted despite holding anti-government beliefs] and disaffected locals.\u201dThen a combination of Jihadists, some from Syria and some from elsewhere, joined the FSA.\nAnd pretty soon, bad guys on both sides are killing civilians\u2026As Father Dave Smith says, \u201cthe way it\u2019s been depicted the last couple of years, you get the impression the rebels are Robin Hood and his band of merry men, and that all they want is freedom and justice for all.\nThere\u2019s no accurate confirmation, but it\u2019s a nasty horrible civil war with people on both sides getting killed.Dr Shanahan says there is evidence that opposition car bombs have killed countless civilians in the name of taking out a government target.\nThe story was soon removed from Vogue\u2019s website and the journalist who wrote it tried to cover her tracks by penning a separate story elsewhere entitled \u201cFirst Lady of Hell\u201d.Even as the Civil war rages, the Assad family remains popular with many middle class Syrians, especially urbanised Sunni Muslims, says Dr Rodger Shanahan.\nFather David Smith visited several camps across the border in Lebanon \u2013 a country whose population of 4.3 million is bulging with the influx of a total of nearly 2 million Palestinian and Syrian refugees.\u201cThe camps I saw were deeply impressive,\u201d Father Dave says."
# }]
#
#
# utils.download_insights(insights)
#assumption keyword from user
keyword = "brexit"
#assumption timedelta representing the relevance of the scraped data Y-Year, M-Month W-Week D-Day
timedelta = "1D"
all_urls=load_data()
#use the urls and crawl the articles
parse_articles(all_urls,keyword)
#fetch articles and pass it on to analytics
articles=fetch_articles(keyword,timedelta)
analyse(articles)
#fetch the analysed inputs and proceed further
insights=get_insights(keyword,timedelta)
#download insights to csv file
download_insights(insights)