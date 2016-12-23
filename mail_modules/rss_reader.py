import feedparser
from bs4 import BeautifulSoup
import re
import datetime
time=datetime.date.today()

f=open('python_news'+str(time)+'.txt','w')
d = feedparser.parse('http://www.reddit.com/r/python/.rss')
f.write('Feed title is:  {0}\n'.format(d.feed.title))
f.write('Feed link is:  {0} \n'.format(d.feed.link))
f.write('Feed description is:  {0}\n\n'.format(d.feed.description))

for i in range(len(d.entries)):
    f.write('{0} topic is:  {1}\n'.format(i+1,d.entries[i].title))
    f.write("Related links are mentioned below: \n")
    soup=BeautifulSoup(d.entries[i].content[0]['value'],'html.parser')
    all_links=soup.find_all('a')
    for link in all_links:
        if re.search('reddit',str(link)):
            f.write('reddit internal link: {0}\n'.format(link.get('href')))
        else:
            f.write('External link:  {0}\n'.format(link.get('href')))
    f.write("-------------End of topic--------------")
    f.write('\n\n')

f.close()