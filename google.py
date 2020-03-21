from googlesearch import *
import webbrowser
# to search, will ask search query at the time of execution
query = input("Input your query:")
#iexplorer_path = r'C:\Program Files (x86)\Internet Explorer\iexplore.exe %s'
chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
for url in search(query, tld="co.in", num=10, stop=7, pause=2):
    webbrowser.open("https://google.com/search?q=%s" % query)
