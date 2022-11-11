import urllib.request as req
import json 
url3="https://data.taipei/api/v1/dataset/36847f3f-deff-4183-a5bb-800737591de5?scope=resourceAquire"

with req.urlopen(url3) as res3:
  data3=json.load(res3)

clist_3=data3["result"]["results"]
print(clist_3)