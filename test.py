import urllib.request

print(urllib.request.urlopen("https://WWW.eXample.com").read().decode('utf-8'))
