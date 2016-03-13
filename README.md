# my-conky-config
conky `1.9.x` config I use on my ArchLinux installation.
Very vel commented for simple extendibility

## Main config - Archlinux

Displays:
- DATE/TIME
- WEATHER
  - current
  - forecast
- SYSTEM information
  - kernel version, architecture
  - uptime
  - pacman (archlinux) available updates
  - unread emails (imap support [python script])
- MEMORY
- SWAP
- CPU (configurable - by default 4 cores)
- NETWORK (shows external address and ping)
  - ETHERNET
  - WIFI
- DISCS
- SYSLOG
- AUDIO (disabled by default)
- JACK BUFFER SIZE (disabled by default)
- MPD support (disabled by default)

#### Screenshot:
![archlinux](https://raw.githubusercontent.com/stefanjarina/my_conky_config/master/archlinux.png)

Some things are hardcoded (`network interfaces names`)

## News config

Easicly extendible, powered by simple python script

if you want to add resource, just add it in `news.py` to dictionary variable and copy/change lines in conky config.

```python
sites = {
	# cz sources
	'root_cz_clanky': "http://www.root.cz/rss/clanky/",
	'your_new_resource': "whatever url, best including http/https",  # <--- new
}
```

###CZ RSS sources

#### Screenshot:

![news_cz](https://raw.githubusercontent.com/stefanjarina/my_conky_config/master/news_cz.png)

### EN RSS sources

#### Screenshot:

![news_en](https://raw.githubusercontent.com/stefanjarina/my_conky_config/master/news_en.png)
