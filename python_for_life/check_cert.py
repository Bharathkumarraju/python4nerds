try:
    import urllib3
except:
    import urllib.request as urllib3
import sys
req = urllib3.Request(sys.argv[1], headers={'User-Agent':'Mozilla/5.0'})
urllib3.urlopen(req)
