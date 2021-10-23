import psycopg2 



#https://stackoverflow.com/questions/2733813/iterating-through-a-json-object


def insertIntoDatabase(CityName, Name ,ClassificationType, SubType, Hours,Lat,Long):
    conn = psycopg2.connect(host="localhost", port = 5432, database="suppliers", user="postgres", password="postgres")
    cur = conn.cursor()
    cur.execute()
    query_results = cur.fetchall()
    cur.close()
    conn.close()


def parseJson():
    pass





