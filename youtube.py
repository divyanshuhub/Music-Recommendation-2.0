import urllib.request
import re

def keyword(artist,song,year):
    '''artist ="Taylor swift"
    song="bad blood"
    year=2014'''

    search_keyword = ""
    for i in artist.split():
        search_keyword += i + "+"
    for i in song.split():
        search_keyword += i + "+"
    search_keyword += str(year)
    #print(search_keyword)
    return search_keyword

def searchyt(artist,song,year):
    link = "https://www.youtube.com/results?search_query="+keyword(artist,song,year)
    #print(link)
    html = urllib.request.urlopen(link)
    video_ids = re.search(r"watch\?v=(\S{11})", html.read().decode())
    video_link = "https://www.youtube.com/watch?v=" + video_ids.group()
    return video_link
