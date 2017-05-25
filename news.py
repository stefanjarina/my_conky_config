#!/usr/bin/env python3
import feedparser, sys

sites = {
	# cz sources
	'root_cz_clanky': "http://www.root.cz/rss/clanky/",
	'root_cz_zpravicky': "http://www.root.cz/rss/zpravicky/",
	'root_cz_diskuze': "http://forum.root.cz/index.php?action=.xml;type=rss2;limit=30;sa=news",
	'zive_cz': "http://www.zive.cz/rss/sc-47/",
	'linuxexpres_clanky': "http://www.linuxexpres.cz/rss/clanky",
	'linuxexpres_novinky': "http://www.linuxexpres.cz/rss/novinky",
	# en sources
	'archlinux_news': "https://www.archlinux.org/feeds/news/",
	'archlinux_packages': "https://www.archlinux.org/feeds/packages",
	'linuxjournal_com': "http://feeds.feedburner.com/linuxjournalcom",
	'omg_ubuntu_co_uk': "http://feeds.feedburner.com/d0od",
	'linux_com_all': "http://www.linux.com/feeds/all-content",
	'linuxsecurity_com_news': "http://www.linuxsecurity.com/static-content/linuxsecurity_articles.rss"
	}

if len(sys.argv) < 2:
	site = sites['root_cz_clanky']

candidate = sys.argv[1].lower()

if candidate in list(sites.keys()):
	site = sites[candidate]
else:
	site = sites['root_cz_clanky']

feed = feedparser.parse( site )
count =  len(feed['entries'])
for i in range(0, count):
	if (i>=5):break
	print('{1}'.format(' ', feed.entries[i].title[0:100]))
