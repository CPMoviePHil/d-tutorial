import json
from urllib import request

url = 'https://www.xtube.com/webmaster/api/getcategorylist/'
data = request.urlopen(url).read().decode("utf-8")

print (json.loads(data))