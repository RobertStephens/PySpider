#! /usr/bin/python

'''
@author: Robert Stephens
'''

import urllib2, BeautifulSoup, sys
from collections import defaultdict

if __name__ == "__main__":


    followed_links = defaultdict(int)

    no_follow_list = ["twitter", "facebook", "login"]

    def follow_link(link_out):

        html_doc = ""
        req = urllib2.Request(link_out)
        try:   
            html_doc = urllib2.urlopen(req)
            parse_links(html_doc)
        except Exception:
            print "exception" 
            sys.exc_clear()
        #except urllib2.URLError, e:
        #    print e.code
        #    print e.read()

    def parse_links(html_doc):
        soup = BeautifulSoup.BeautifulSoup(html_doc)
    
        sep_line = "=========================================" 
        
        for link in soup.findAll('a'):
            
            link_out = link.get('href')
            
            if new_link(link_out) and can_follow(link_out):
        
                count_string = " " + str( len(followed_links) ) + " "
                count_sep = ""
                for i in xrange( len(count_string) ):
                    count_sep += "="
                
                print sep_line + count_string + sep_line
                print link_out
                print sep_line + count_sep + sep_line 

                follow_link(link_out)

    def new_link(link_out):
        if followed_links[link_out] == 0: 
            followed_links[link_out] += 1
            return True
        else:
            followed_links[link_out] += 1
            return False
   
    def can_follow(link_out):
        for no_follow_link in no_follow_list:        
            if link_out.find(no_follow_link) != -1:
                print "can't follow: " + no_follow_link
                return False
        return True

    start_url = "http://www.reddit.com"
    if len(sys.argv) > 1:
        start_url = sys.argv[1]

    follow_link(start_url)    


