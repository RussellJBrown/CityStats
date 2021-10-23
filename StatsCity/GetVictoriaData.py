from serpapi import GoogleSearch

params = {
  "engine": "google_maps",
  "q": "restaurants",
  "ll": "@49.2432317,-123.1361494,13.04z",
  "google_domain": "google.com",
  "type": "search", 
  "hl": "en",
  "api_key": "c11e256649c534b8bb9f41d896caa9469abe983bc555dafaade4804e74890919"  
}

params2 = {
  "engine": "google_maps",
  "q": "restaurants",
  "ll": "@49.2432317,-123.1361494,13.04z",
  "google_domain": "google.com",
  "type": "search", 
  "hl": "en",
  "start": "20",
  "api_key": "c11e256649c534b8bb9f41d896caa9469abe983bc555dafaade4804e74890919" 
}


params3 = {
  "engine": "google_maps",
  "q": "restaurants",
  "ll": "@49.2432317,-123.1361494,13.04z",
  "google_domain": "google.com",
  "type": "search", 
  "hl": "en",
  "start": "20",
  "api_key": "c11e256649c534b8bb9f41d896caa9469abe983bc555dafaade4804e74890919" 
}

search = GoogleSearch(params)
results = search.get_dict()