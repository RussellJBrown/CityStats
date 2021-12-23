from __future__ import print_function
import psycopg2 
import json
import sys
import Constants
import glob
from Constants import *
from pathlib import Path

#https://stackoverflow.com/questions/2733813/iterating-through-a-json-object


def insertIntoDatabase(CityName, Name ,ClassificationType, SubType, Hours,Lat,Long):
    conn = psycopg2.connect(host="localhost", port = 5432, database="suppliers", user="postgres", password="postgres")
    cur = conn.cursor()
    cur.execute()
    query_results = cur.fetchall()
    cur.close()
    conn.close()


def parseGoogleJson(textFile):
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

        serviceOptions = i["service_options"]
        dineIn = serviceOptions["dine_in"]
        takeOut = serviceOptions["takeout"]
        delivery = serviceOptions["delivery"]

        restaurantClassification(restaurantType,title)
        try:
            print(i["hours"])
            isNightLife = nightLife(hours)
            isMorningLife =  morningLife(hours)
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
        if "4:00 p.m." in hours.lower() or "5:00 p.m." in hours.lower() or "5:00 p.m." in hours.lower() or "6:00 p.m." in hours.lower() or "7:00 p.m." in hours.lower() or "8:00 p.m." in hours.lower() or "9:00 p.m." in hours.lower() or "10:00 p.m." in hours.lower() or "10:00 p.m." in hours.lower() or "10:00 p.m." in hours.lower() or "11:00 p.m." in hours.lower():   
            return False

        if "12:00 a.m." in hours.lower() or "1:00 a.m." in hours.lower() or "2:00 a.m." in hours.lower():
            return True

def morningLife(hours):
    if "opening" in hours.lower() or "opened" in hours.lower():
        if "6:00 a.m." in hours.lower() or "7:00 a.m." in hours.lower() or "8:00 a.m." in hours.lower() or "9:00 a.m." in hours.lower() or "10:00 a.m." in hours.lower():
            return True

    else:
        return False


def parseGeoJsonSchool(path):
    with open(path) as f:
        data = json.loads(f.read())
        for feature in data["features"]:
            props = feature["properties"]
            geom = feature["geometry"]

            print("New Property")
            print("Properties: ")
            print(props)
            schoolCategory=props["school_category"]
            schoolAddress=props["address"]
            schoolName=props["school_name"]
            local_area=props["geo_local_area"]

            geomType=geom["type"]
            geomCoor=geom["coordinates"]

def insertSchool(schoolCategory, schoolName):
    connection = psycopg2.connect(user="postgres",
                                    password="pynative@#29",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="VancouverSchool")

    insertStatement = '''Insert INTO VancouverSchool(schoolCategory,schoolName) VALUES(%s,%s)'''
    recordToInsert = (schoolCategory,schoolName)
    cursor = connection.cursor()
        # Executing a SQL query
    cursor.execute(insertStatement,recordToInsert)


def parseGeoJsonBus(data):
                
                GeometeryInput=""
                                                 
                try:
                    typeGeom=data["type"]
                    coordinates=data["coordinates"] 
                    coordinates = ' '.join([str(x) for x in coordinates])
                    GeometeryInput = "ST_GeomFromText('"+typeGeom +"("+coordinates+")', 4326)"

                except:
                    print("Exception in parsing Geojson")
                    sys.exit()
                                 

                return GeometeryInput
                


'''
These Methods
'''
def formattingBusiness(geometry,properties,CityName):  
    BusinessName = ""
    BusDescription = ""
    propertiesKeys = properties.keys()

    for key in Constants.BusNameTerms:
        if(key in propertiesKeys):
            BusinessName = properties[key]
            break
    
    for key in Constants.BusDescr:
        if(key in propertiesKeys):
            BusDescription = properties[key]
            break
    if "'" in BusinessName:
        BusinessName = BusinessName.replace("'","")

    if "'" in BusDescription:
        BusDescription = BusDescription.replace("'","")
    
    GeogData = parseGeoJsonBus(geometry)
    insertBusiness("BusinessesInCities",CityName,BusinessName,BusDescription,str(25),GeogData)
    return True


def formattingSchools(geometry,properties,CityName):
    SchoolName = ""
    SchoolType = ""
    FrenchSchool = False
    propertiesKeys = properties.keys()

    for key in Constants.Schools:
        if(key in propertiesKeys):
            SchoolName = propertiesKeys[key]
            break
            #insertSchools(tableName, city,SchoolName ,SchoolType, French, GeoData)
    for key in Constants.SchoolTypes:
        if(key in properties):
            SchoolType=propertiesKeys[key]
            if "french" in SchoolType.lower() or "francophone" in SchoolType.lower():
                FrenchSchool = True

    GeogData = parseGeoJsonBus(geometry)  
    insertSchools("SchoolsInCities", CityName,SchoolName ,SchoolType, FrenchSchool, GeogData)

    
def formattingParks(geometry,properties,CityName):
    ParkName = ""
    ParkInfo = ""
    DogPark = False
    for key in Constants.ParksNames:
        if key in properties:
            ParkName = properties[key]
            break
    
    for key in Constants.ParksInfo:
        if key in properties:
            ParkInfo = properties[key]

    if "dog" in ParkInfo.lower():
        DogPark = True


    GeogData = parseGeoJsonBus(geometry)
    insertParks("Parks",CityName,DogPark,GeogData)


def formattingBusStops(geometry,properties,CityName):   
    BusRouteName = ""
    BusType = ""
   
    for key in Constants.BusRouteNumber:
        if key in properties:
            BusRouteName = properties[key]

    for key in Constants.BusCategory:
        if key in properties:
            BusType = properties[key]

    GeogData = parseGeoJsonBus(geometry)   
    insertBusStops("BusStops", CityName, BusRouteName, BusType, GeogData)


def foramttingFireStations(geometry,properties,CityName):
    FireStationName = ""
    for key in Constants.FireStationName:
        if key in properties:
            FireStationName = properties[key]

    GeogData = parseGeoJsonBus(geometry)
    insertFireStations("FireStations", CityName, FireStationName, GeogData)


def formattingProperty(geometry,properties,CityName):
    PropertyPrice = ""
    PropertyNeighbourhood = ""
    PropertyAddressStreet = ""
    PropertyAddressNumber = ""
    PropertyType = ""


    for key in Constants.PropertyPrice:
        if key in properties:
            PropertyPrice = properties[key]
        
    for key in Constants.PropertyNeighbourhood:
        if key in properties:
            PropertyNeighbourhood = properties[key]

    for key in Constants.PropertyAddressNumber:
        if key in properties:
            PropertyAddressStreet = properties[key]
    
    for key in Constants.PropertyAddressStreet:
        if key in properties:
            PropertyAddressNumber = properties[key]

    for key in Constants.PropertyType:
        if key in properties:
            PropertyType = properties[key]
    
   


    GeogData = parseGeoJsonBus(geometry)
    insertProperty("PropertiesInCities",CityName,PropertyNeighbourhood,PropertyAddressStreet+PropertyAddressNumber,str(PropertyPrice),GeogData,PropertyType)


'''
Method will be used for Coffee/Restaurants/Businesses
'''
def insertBusiness(tableName, city,businessName, businessType,Hours,GeoData):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="VXVictRB#",
                                      host="localhost",
                                      port="5432",
                                      database="postgres")
         
        insertQuery = '''INSERT Into public."'''+ tableName+'''"("CityName", "BusinessName", "BusinessType", "BusinessHours", "GeoData") VALUES(''' +"'"+city+"', '" + businessName + "', '" + businessType + "', "+Hours+","+GeoData+");"
        cursor = connection.cursor()
        cursor.execute(insertQuery)
        connection.commit()

    except Exception as e:
        print("Error")
        print(e)
    finally:
        if(connection):
            cursor.close()
            connection.close()
            #print("PostgreSQL connection is closed")          

def insertParks(tableName,city,parkName,DogPark,geoData):
    try:
        connection = Constants.connection
        insertQuery = '''INSERT Into public."'''+tableName+'''"("CityName","ParkName","DogPark","GeoData) VALUES('''+"'"+city+"', '"+parkName+"', '"+DogPark+"'," + geoData+");"
        cursor = connection.cursor()
        cursor.execute(insertQuery)
        cursor.commit()

    except Exception as e:
        print("Error")
        print(e)
        
    finally:
        if (connection):
            cursor.close()
            connection.close()
            print("PostgresSQL connection is closed")

def insertSchools(tableName, city,SchoolName ,SchoolType, French, GeoData):

    try:
        connection = Constants.connection
        insertQuery =  '''INSERT Into public."'''+tableName+'''"("CityName","SchoolName","SchoolType","FrenchSchool","GeoData") VALUES('''+"'"+city+"', '"+SchoolType+"', '"+French+"'," + GeoData+");"
        cursor = connection.cursor()
        cursor.execute(insertQuery)
        cursor.commit()

    except Exception as e:
        print("Error")
        print(e)
        
    finally:
        if (connection):
            cursor.close()
            connection.close()
            print("PostgresSQL connection is closed")

def insertFireStations(tableName, city, Name, GeoData):
    try:
        connection = Constants.connection
        insertQuery = '''INSERT Into public."'''+tableName+'''"("CityName","Name") VALUES('''+"'"+city+"', '"+Name+"','" + GeoData+");"
        cursor= connection.cursor()
        cursor.execute(insertQuery)
        cursor.commit()
    
    
    except Exception as e:
        print("Error")
        print(e)
        
    finally:
        if (connection):
            cursor.close()
            connection.close()
            print("PostgresSQL connection is closed")

def insertBusStops(tableName, city, busRoute, busType, GeoData):
    try:
        connection = Constants.connection
        insertQuery = '''INSERT Into public."'''+tableName+'''"("CityName","BusRoute","BusType","GeoData") Values('''+"'"+city+"', '"+busRoute+"', '"+busType+"," + GeoData+");"
        cursor = connection.cursor()
        cursor.execute(insertQuery)
        cursor.commit()
    except Exception as e:
        print("Error")
        print(e)
    finally:
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def insertProperty(tableName, city, Neighbourhood ,Address, Price ,GeoData,PropertyType):
    try:
        connection = Constants.connection 
        #insertQuery = '''INSERT Into public."'''+ tableName+'''"("CityName", "BusinessName", "BusinessType", "BusinessHours", "GeoData") VALUES(''' +"'"+city+"', '" + businessName + "', '" + businessType + "', "+Hours+","+GeoData+");"                      
        insertQuery = '''Insert Into public."'''+tableName+'''"("Cities","Neighbourhood","Address","Price","PropertyType","GeogData")    Values(''' +"'"+city+"', '" +Neighbourhood + "', '" + Address+ "', '"+ Price +"', '"+PropertyType +"', "+GeoData +");"
        print(insertQuery)
        sys.exit()
        cursor = connection.cursor()
        cursor.execute(insertQuery)
        cursor.commit()
    except Exception as e:
        print("Error")
        print(e)
        sys.exit()
    finally:
        sys.exit()
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


def insertGeometry(RecordID,type,coordiantes,tableName):
   print("Inserting Geometery")
   insertSQL = "Insert into " + tableName + "(RecordID,GeometeryType,Geometery) Values(" +RecordID+" ," +  type + " ,"
   #https://stackoverflow.com/questions/38937455/creating-a-table-for-polygon-values-in-postgis-and-inserting
   geometeryString=""
   if type=="Point":
       geometeryString+="ST_GeometryFromText( Point("
        
   elif type=="Linestring":
       geometeryString+="ST_GeometryFromText( Linestring("
   
   elif type=="Polygon":
        geometeryString+="ST_GeometryFromText( Polygon(("
   
   elif type=="PolygonWithHole":
       geometeryString+="ST_GeometryFromText( Polygon(("
       pass 
   
   elif type=="Collection":
       pass

   even=False
   print("Coordinates Length")
   print(len(coordiantes))
   i=1
   for points in coordiantes:
        print("Points")
        print(points) 
        if even==False:
            geometeryString+=str(points) +" "
            even=True
        
        elif i==len(coordiantes):
            geometeryString+=str(points)
            even=False

        else:
            geometeryString+=str(points)+","
            even=False
        i+=1

   if type=="Point" or type=="Linestring":
       insertSQL+=geometeryString
       insertSQL+=")))"
   if type=="Polygon" or type=="PolygonWithHole":
       insertSQL+=geometeryString
       insertSQL+="))))"
   
   SQL = insertSQL.rstrip(',')



def checkFile(fileName, CityName):
    try:
        with open(fileName) as f:
                data = json.load(f)
                lengthJson = len(data['features'])
                
                # if "bus" in fileName.lower():                          
                #     i=0
                #     while i<lengthJson:
                #         try:
                #             geometry = data['features'][i]['geometry']
                #             properties = data['features'][i]['properties']                            
                #             if(geometry is not None):                               
                #                 formattingBusiness(geometry,properties,CityName)

                #         except Exception as ex:
                #             print("Failed Exception")
                #             sys.exit()
                                              
                #         i+=1
                                   
                if "property" in fileName.lower():
                    i=0
                    while i<lengthJson:
                        try:
                            geometry = data['features'][i]['geometry']
                            properties = data['features'][i]['properties']
                            if(geometry is not None):
                                formattingProperty(geometry,properties,CityName)
                        except:
                            print("Failed Exception")


                #         except Exception as ex:
                #             print("Failed Exception")
                #             print(ex)
                #             sys.exit()
                           
                # elif "parks" in  fileName.lower():
                #     i = 0
                #     while i<lengthJson:
                #         try:
                #             geometry = data['features'][i]['geometry']
                #             properties = data['features'][i]['properties']                            
                #             if(geometry is not None):
                #                 formattingParks(geometry,properties,CityName)

                #         except Exception as ex:
                #             print("Failed Exception")
                #             print(ex)
                #             sys.exit()
                #         i+=1

                # elif "schools" in fileName.lower():
                #     i=0
                #     while i<lengthJson:
                #         try:
                #             geometry = data['features'][i]['geometry']
                #             properties = data['features'][i]['properties']                            
                #             if(geometry is not None):
                #                 formattingSchools(geometry,properties,CityName)

                #         except Exception as ex:
                #             print("Failed Exception")
                #             print(ex)
                #             sys.exit()                     
                #         i+=1
                                          
                # elif "transit" in fileName.lower():
                #     i=0
                #     while i<lengthJson:
                #         try:
                #             geometry = data['features'][i]['geometry']
                #             properties = data['features'][i]['properties']                            
                #             if(geometry is not None):
                #                 formattingBusStops(geometry,properties,CityName)

                #         except Exception as ex:
                #             print("Failed Exception")
                #             print(ex)
                #             sys.exit()                     
                #         i+=1

                # elif "fire" in fileName.lower():
                #     i=0
                #     while i<lengthJson:
                #         try:
                #             geometry = data['features'][i]['geometry']
                #             properties = data['features'][i]['properties']                            
                #             if(geometry is not None):
                #                 foramttingFireStations(geometry,properties,CityName)

                #         except Exception as ex:
                #             print("Failed Exception")
                #             print(ex)
                #             sys.exit()                     
                #         i+=1

    except Exception as ex:
        print("Starting Exception")
        print(fileName)
        print(ex)
        print("Finished Exception")
        print("")

if __name__ == "__main__":

    filesVancouver = glob.glob("data/VancouverData/*Python.geojson")
    filesVictoria = glob.glob("data/VictoriaData/*Python.geojson")
    filesCalgary = glob.glob("data/CalgaryData/*Python.geojson")
    filesEdmonton = glob.glob("data/EdmontonData/*Python.geojson")


    for file in filesVancouver:
          print("Creating Data")
          print(file)
          checkFile(file,"Vancouver")
    for file in filesVictoria:
          print("Creating Data")
          print(file)
          checkFile(file,"Victoria")
    for file in filesCalgary:
          print("Creating Data")
          print(file)
          checkFile(file,"Calgary")
    for file in filesEdmonton:
          print("Creating Data")
          print(file)
          checkFile(file,"Edmonton")
    
  

    







