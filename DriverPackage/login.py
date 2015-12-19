import requests

# r = requests.get("http://172.16.23.230", auth = ('admin','password'))
r = requests.get("http://www.google.com")

print r.status_code
print r.encoding
print r

print r.content

print r.text

try:
    print r.json()
except:
    print "Errors are seen for json()"