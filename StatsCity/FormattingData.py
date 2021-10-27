import psycopg2 
import json


#https://stackoverflow.com/questions/2733813/iterating-through-a-json-object


def insertIntoDatabase(CityName, Name ,ClassificationType, SubType, Hours,Lat,Long):
    conn = psycopg2.connect(host="localhost", port = 5432, database="suppliers", user="postgres", password="postgres")
    cur = conn.cursor()
    cur.execute()
    query_results = cur.fetchall()
    cur.close()
    conn.close()


def parseJson(textFile):
    f = open(textFile)
    data = json.load(f)
    for i in data:
        print("")
        print(i["position"])
        print(i["type"])
        restaurantType = i["type"]
        print(i["title"])
        
        title=i["title"]
        hours=i["hours"]
        gpsC = i["gps_coordinates"]
        latitude=gpsC["latitude"]
        longitude=gpsC["longitude"]

        restaurantClassification(restaurantType,title)
        try:
            print(i["hours"])
        except:
            print("No Hours")
        print("")
 

def restaurantClassification(RestaurantType,Title):
        wordstring = RestaurantType + ' '
        wordstring += Title

        wordlist = wordstring.split()

        wordfreq = []
        for w in wordlist:
            wordfreq.append(wordlist.count(w))

        print("String\n" + wordstring +"\n")
        print("List\n" + str(wordlist) + "\n")
        print("Frequencies\n" + str(wordfreq) + "\n")
        print("Pairs\n" + str(list(zip(wordlist, wordfreq))))



def nightLife(hours):

    if "closing" in hours.lower() or "closed" in hours.lower():    
        pass

    if nightLife == True:
        return True

    else:
        return False

def morningLife(hours):
    if "closing" in hours.lower() or "closed" in hours.lower():
        pass


    if hours == True:
        pass

    else:
        pass





if __name__ == "__main__":
    VictoriaRestaurant="victoria.txt"
    VancouverRestaurant="victoria.txt"
    parseJson(VictoriaRestaurant)
    #parseJson(VancouverRestaurant)







