from http.client import responses
import webbrowser
import json
from urllib.request import urlopen

print("Let's find it!")
site = input("Type URL: ")
era = input("Type date: ")
url = "http://archive.org/wayback/available?url=%s&timestamp=%s" % (site, era)
response = urlopen(url)
contents = response.read()

text = contents.decode("utf-8")
data = json.loads(text)
try:
    old_site = data["archived_snapshots"]["closest"]["url"]
    print("Found this copy: ", old_site)
    print("It should appear in your brower now.")
    webbrowser.open(old_site)
except:
    print("Sorry, no luck finding", site)