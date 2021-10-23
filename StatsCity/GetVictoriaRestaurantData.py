from serpapi import GoogleSearch
import json

def getVictoriaRestaurantData():
      params = {
        "engine": "google_maps",
        "q": "restaurants",
        "ll": "@49.2432317,-123.1361494,14.0z",
        "google_domain": "google.com",
        "type": "search", 
        "hl": "en",
        "api_key": "c11e256649c534b8bb9f41d896caa9469abe983bc555dafaade4804e74890919"  
      }

      params2 = {
        "engine": "google_maps",
        "q": "restaurants",
        "ll": "@49.2432317,-123.1361494,14.0z",
        "google_domain": "google.com",
        "type": "search", 
        "hl": "en",
        "start": "20",
        "api_key": "c11e256649c534b8bb9f41d896caa9469abe983bc555dafaade4804e74890919" 
      }


      params3 = {
        "engine": "google_maps",
        "q": "restaurants",
        "ll": "@49.2432317,-123.1361494,14.0z",
        "google_domain": "google.com",
        "type": "search", 
        "hl": "en",
        "start": "40",
        "api_key": "c11e256649c534b8bb9f41d896caa9469abe983bc555dafaade4804e74890919" 
      }

      params4 = {
        "engine": "google_maps",
        "q": "restaurants",
        "ll": "@49.2432317,-123.1361494,14.0z",
        "google_domain": "google.com",
        "type": "search", 
        "hl": "en",
        "start": "60",
        "api_key": "c11e256649c534b8bb9f41d896caa9469abe983bc555dafaade4804e74890919" 
      }

      params5 = {
        "engine": "google_maps",
        "q": "restaurants",
        "ll": "@49.2432317,-123.1361494,14.0z",
        "google_domain": "google.com",
        "type": "search", 
        "hl": "en",
        "start": "80",
        "api_key": "c11e256649c534b8bb9f41d896caa9469abe983bc555dafaade4804e74890919" 
      }

      params6 = {
        "engine": "google_maps",
        "q": "restaurants",
        "ll": "@49.2432317,-123.1361494,14.0z",
        "google_domain": "google.com",
        "type": "search", 
        "hl": "en",
        "start": "100",
        "api_key": "c11e256649c534b8bb9f41d896caa9469abe983bc555dafaade4804e74890919" 
      }

      search = GoogleSearch(params)
      results = search.get_dict()
      local_results = results['local_results']
      with open('VictoriaRestaurants.txt','w') as outfile:
          json.dump(local_results,outfile)


def getVictoriaOfficeData():
      params = {
        "engine": "google_maps",
        "q": "Offices",
        "ll": "@49.2432317,-123.1361494,14.0z",
        "google_domain": "google.com",
        "type": "search", 
        "hl": "en",
        "api_key": "c11e256649c534b8bb9f41d896caa9469abe983bc555dafaade4804e74890919"  
      }

      params2 = {
        "engine": "google_maps",
        "q": "restaurants",
        "ll": "@49.2432317,-123.1361494,14.0z",
        "google_domain": "google.com",
        "type": "search", 
        "hl": "en",
        "start": "40",
        "api_key": "c11e256649c534b8bb9f41d896caa9469abe983bc555dafaade4804e74890919" 
      }

      params3 = {
        "engine": "google_maps",
        "q": "restaurants",
        "ll": "@49.2432317,-123.1361494,14.0z",
        "google_domain": "google.com",
        "type": "search", 
        "hl": "en",
        "start": "40",
        "api_key": "c11e256649c534b8bb9f41d896caa9469abe983bc555dafaade4804e74890919" 
      }


def getSchools():
      params = {
        "engine": "google_maps",
        "q": "Schools",
        "ll": "@49.2432317,-123.1361494,14.0z",
        "google_domain": "google.com",
        "type": "search", 
        "hl": "en",
        "api_key": "c11e256649c534b8bb9f41d896caa9469abe983bc555dafaade4804e74890919" 
      }

      params2 = {
        "engine": "google_maps",
        "q": "restaurants",
        "ll": "@49.2432317,-123.1361494,14.0z",
        "google_domain": "google.com",
        "type": "search", 
        "hl": "en",
        "start": "20",
        "api_key": "c11e256649c534b8bb9f41d896caa9469abe983bc555dafaade4804e74890919" 
      }
def getArtsStudio():
      params = {
        "engine": "google_maps",
        "q": "Arts Studio",
        "ll": "@49.2432317,-123.1361494,14.0z",
        "google_domain": "google.com",
        "type": "search", 
        "hl": "en",
        "api_key": "c11e256649c534b8bb9f41d896caa9469abe983bc555dafaade4804e74890919" 
      }

      params2 = {
        "engine": "google_maps",
        "q": "Arts Studio",
        "ll": "@49.2432317,-123.1361494,14.0z",
        "google_domain": "google.com",
        "type": "search", 
        "hl": "en",
        "start": "20",
        "api_key": "c11e256649c534b8bb9f41d896caa9469abe983bc555dafaade4804e74890919" 
      }

def getTheatre():
      params = {
        "engine": "google_maps",
        "q": "Theatre",
        "ll": "@49.2432317,-123.1361494,14.0z",
        "google_domain": "google.com",
        "type": "search", 
        "hl": "en",
        "api_key": "c11e256649c534b8bb9f41d896caa9469abe983bc555dafaade4804e74890919" 
      }

      params2 = {
        "engine": "google_maps",
        "q": "Theatre",
        "ll": "@49.2432317,-123.1361494,14.0z",
        "google_domain": "google.com",
        "type": "search", 
        "hl": "en",
        "start": "20",
        "api_key": "c11e256649c534b8bb9f41d896caa9469abe983bc555dafaade4804e74890919" 
      }


def GetMajorHospitals():
      params = {
        "engine": "google_maps",
        "q": "Major Hospitals",
        "ll": "@49.2432317,-123.1361494,14.0z",
        "google_domain": "google.com",
        "type": "search", 
        "hl": "en",
        "api_key": "c11e256649c534b8bb9f41d896caa9469abe983bc555dafaade4804e74890919" 
      }


def Airports():
      params = {
        "engine": "google_maps",
        "q": "Major Airports Victoria",
        "ll": "@49.2432317,-123.1361494,11.0z",
        "google_domain": "google.com",
        "type": "search", 
        "hl": "en",
        "api_key": "c11e256649c534b8bb9f41d896caa9469abe983bc555dafaade4804e74890919" 
      }



def Churches():
      params = {
        "engine": "google_maps",
        "q": "Major Churches",
        "ll": "@49.2432317,-123.1361494,14.0z",
        "google_domain": "google.com",
        "type": "search", 
        "hl": "en",
        "api_key": "c11e256649c534b8bb9f41d896caa9469abe983bc555dafaade4804e74890919" 
      }
      
      params2 = {
        "engine": "google_maps",
        "q": "Major Churches",
        "ll": "@49.2432317,-123.1361494,14.0z",
        "google_domain": "google.com",
        "type": "search", 
        "hl": "en",
        "start": "20",
        "api_key": "c11e256649c534b8bb9f41d896caa9469abe983bc555dafaade4804e74890919" 
      }

def RecCenters():
      params = {
        "engine": "google_maps",
        "q": "Rec Centers",
        "ll": "@49.2432317,-123.1361494,14.0z",
        "google_domain": "google.com",
        "type": "search", 
        "hl": "en",
        "api_key": "c11e256649c534b8bb9f41d896caa9469abe983bc555dafaade4804e74890919" 
      }


      params2 = {
        "engine": "google_maps",
        "q": "Rec Centers",
        "ll": "@49.2432317,-123.1361494,14.0z",
        "google_domain": "google.com",
        "type": "search", 
        "hl": "en",
        "start": "20",
        "api_key": "c11e256649c534b8bb9f41d896caa9469abe983bc555dafaade4804e74890919" 
      }

def HikingTrails():
  params = {
        "engine": "google_maps",
        "q": "Hiking Trails",
        "ll": "@49.2432317,-123.1361494,14.0z",
        "google_domain": "google.com",
        "type": "search", 
        "hl": "en",
        "api_key": "c11e256649c534b8bb9f41d896caa9469abe983bc555dafaade4804e74890919" 
  }

  params2 = {
        "engine": "google_maps",
        "q": "Hiking Trails",
        "ll": "@49.2432317,-123.1361494,14.0z",
        "google_domain": "google.com",
        "type": "search", 
        "hl": "en",
        "start": "20",
        "api_key": "c11e256649c534b8bb9f41d896caa9469abe983bc555dafaade4804e74890919" 
      }

  params3 = {
        "engine": "google_maps",
        "q": "Hiking Trails",
        "ll": "@49.2432317,-123.1361494,14.0z",
        "google_domain": "google.com",
        "type": "search", 
        "hl": "en",
        "start": "40",
        "api_key": "c11e256649c534b8bb9f41d896caa9469abe983bc555dafaade4804e74890919" 
  }

  params4 = {
        "engine": "google_maps",
        "q": "Hiking Trails",
        "ll": "@49.2432317,-123.1361494,14.0z",
        "google_domain": "google.com",
        "type": "search", 
        "hl": "en",
        "start": "60",
        "api_key": "c11e256649c534b8bb9f41d896caa9469abe983bc555dafaade4804e74890919" 
  }

def FarmersMarket():
    params = {
        "engine": "google_maps",
        "q": "Famers'",
        "ll": "@49.2432317,-123.1361494,14.0z",
        "google_domain": "google.com",
        "type": "search", 
        "hl": "en",
        "api_key": "c11e256649c534b8bb9f41d896caa9469abe983bc555dafaade4804e74890919" 
  }
  
  


#Measing importance of City

'''
1. Restaurants
2. Offices
3. Schools
4. Transportation(bike paths/Bus routes)
5. Arts/Culture (Theather/museums/live theather)
6. Governments
7. Hospitals
8. Crime Rates(If possible, maybe check Municpal government websites)
9.  Airports(May not need to include in map but good to have locations)
10. Pedestrian Friendly(More Analysis than Google)
11. Churches
12. Rec Centers
13. Private Transportation
14. Hiking Trails
15. Farmers Market(Fresh Food Sources)


//Weather
'''
