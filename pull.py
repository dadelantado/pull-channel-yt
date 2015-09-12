#!/usr/bin/python
# -*- coding: utf-8 -*-


import urllib, json, subprocess, time, sys, getopt
#print "Channel?",
#author = str(sys.argv[1])
#author = 'dadelantado'
try:
    options, remainder = getopt.getopt(sys.argv[1:], 'u:i:h', ['user=', 'id=', 'help'])
except getopt.GetoptError as err:
    print(err) 
    print 'Use -i for id or -u for username' # will print something like "option -a not recognized"
    
        #usage()
        sys.exit(2)
print options
for opt, arg in options:
    if opt in ('-u', '--user'):
        types = 'forUsername'
        author = arg
        
    elif opt in ('-i', '--id'):
            types = 'id'
            author = arg
    elif opt in ('-h', '--help'):
        print 'Use -i for id or -u for username'
        sys.exit(2)
            

foundAll = False
ind = 0
#videos = []
apikey = 'AIzaSyA7s-mBPBU5snEKPZ7CAuLwIuvGa6hRGyc'

#1st Part: retreive uploads id, forUsername(with username) or id (channel id)

inp = urllib.urlopen(r'https://www.googleapis.com/youtube/v3/channels?part=contentDetails&{0}={1}&key={2}'.format( types, author, apikey ) )
resp = json.load(inp)
inp.close()
print "Generating playlist..."
uploadsid = resp['items'][0]['contentDetails']['relatedPlaylists']['uploads']
#print resp
#print uploadsid

#2nd Part: retreive list of videos
inp = urllib.urlopen(r'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId={0}&key={1}&maxResults=50'.format(uploadsid, apikey))
videolistresp = json.load(inp)
inp.close()
videolist = videolistresp['items']
#for videos in videolist:
 #print videolist[ind]['snippet']['title'],
 #print videolist[ind]['snippet']['resourceId']['videoId']
firstvideo = videolist[ind]['snippet']['resourceId']['videoId']
 #ind += 1

file = open(author+'.html', 'w')
file.write('<div class="responsive-video-list"><div class="featured-video"><iframe width="100%" height="100%" src="https://www.youtube.com/embed/'+firstvideo+'?autoplay=0&amp;rel=0&amp;showinfo=0&amp;modestbranding=1&amp;autohide=1" frameborder="0" allowfullscreen id="FeaturedVideoID"></iframe></div><ul>')
ind = 0
for videos in videolist:
 title = videolist[ind]['snippet']['title'].encode('ascii', 'replace')

 videoid = videolist[ind]['snippet']['resourceId']['videoId']
 file.write('<li><a onclick="switchVideo(\'www.youtube.com/embed/'+videoid+'?autoplay=1&amp;rel=0&amp;showinfo=0&amp;modestbranding=1&amp;autohide=1\');" href="javascript:void(0);"> <img src="http://img.youtube.com/vi/'+videoid+'/0.jpg">'+title+'</a></li>')
 ind += 1

file.write('</ul></div>')
time.sleep(3)
cmd = 'bbedit '+author+'.html'
procc = subprocess.Popen(cmd , shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
procc.wait()
