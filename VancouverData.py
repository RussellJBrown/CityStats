from serpapi import GoogleSearch
import json

params = {
  "engine": "google_maps",
  "q": "restaurants",
  "ll": "@49.2432317,-123.1361494,13.04z",
  "type": "search",
  "num": 1500,
  "api_key": "c11e256649c534b8bb9f41d896caa9469abe983bc555dafaade4804e74890919"
 
}

search = GoogleSearch(params)
results = search.get_dict()
local_results = results['local_results']
with open('vancouver.txt','w') as outfile:
    json.dump(local_results,outfile)
print("Got Vancouver Data")