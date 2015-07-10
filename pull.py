#!/usr/bin/python
import urllib, json
print "Channel?",
author = raw_input()
 
foundAll = False
ind = 1
videos = []
while not foundAll:
    inp = urllib.urlopen(r'http://gdata.youtube.com/feeds/api/videos?start-index={0}&max-results=50&alt=json&orderby=published&author={1}'.format( ind, author ) )
    try:
        resp = json.load(inp)
        inp.close()
        returnedVideos = resp['feed']['entry']
        for video in returnedVideos:
            videos.append( video ) 
 
        ind += 50
        print len( videos )
        if ( len( returnedVideos ) < 50 ):
            foundAll = True
    except:
        #catch the case where the number of videos in the channel is a multiple of 50
        print "error"
        foundAll = True
f = open(author+'.html', 'w')
for video in videos:

    ##print video['title']['$t'] # video title
    ##print video['id']['$t']#url
    p = video['id']['$t']
    print video['title']['$t'] +' '+ p[len('http://gdata.youtube.com/feeds/api/videos/'):]
    f.write('<li><a onclick="switchVideo(\'www.youtube.com/embed/'+p[len('http://gdata.youtube.com/feeds/api/videos/'):]+'autoplay=1&amp;rel=0&amp;showinfo=0&amp;modestbranding=1&amp;autohide=1\');" href="javascript:void(0);"> <img src="http://img.youtube.com/vi/'+p[len('http://gdata.youtube.com/feeds/api/videos/'):]+'/0.jpg">'+video['title']['$t']+'</a></li>')



        ##video['title']['$t'] +' '+ p[len('http://gdata.youtube.com/feeds/api/videos/'):]+'\n')
