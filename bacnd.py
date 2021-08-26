import feedparser
import dbf


def parser(table,url,limit):
    feed = feedparser.parse(url)
    dbf.delete_tables(table)
    dbf.text_in(table)
    for i in range(0,limit):
        entry = feed.entries[i]
        z=str(entry.title)
        l=str(entry.link)
        dbf.insert_title_into_table(table,z,l)
    return ("insertion done")

def main():
    climate_change()
   # privacy_focus()


def climate_change():
    result= parser("NASAclimate","https://climate.nasa.gov/blog/rss.xml",20)
    print(result)

    result= parser("thegaurdian","https://www.theguardian.com/uk/environment/rss",20)
    print(result)
    
    result= parser("greenpeace","https://www.greenpeace.org/international/feed",10)
    print(result)



"""
def privacy_focus():
    result=parser("eff","https://www.eff.org/rss/updates.xml",10)
    print(result)
"""

if __name__=='__main__':
    parser("eff","https://www.eff.org/rss/updates.xml")
    
