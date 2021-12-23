import psycopg2 

BusNameTerms = ["TRADENAME","BUSINESSNAME","business_c","TRADE_NAME","businesstradename","businessname"]

BusDescr = ["trade_description", "businesstype","licencetypes"]

GEOGData = ["coordinates"]

Schools = ["SCHOOLNAME","school_name","name"]

SchoolTypes = ["High","Middle","Elementary","French","Francophone"]

FireStationName = ["name"]

BusStopName = ["stop_name"]

BusRouteNumber = ["route_short_name"]

BusCategory = ["route_category"]

ParksNames = ["Parks_and_Open_Space","name","common_name","site_name"]

ParksInfo = ["maint_info"]

PropertyPrice = ["assessed_value"]
PropertyNeighbourhood = ["neighbourhood"]
PropertyAddressStreet = ["street_name","address"]
PropertyAddressNumber = ["house_number"]
PropertyType = ["assessment_class_description"]

VictoriaBusiness = "VictoriaBusiness"
VancouverBusiness = "VancouverBusiness"
CalgaryBusiness = "CalgaryBusiness"
EdmontonBusiness = "EdmontonBusiness"

VictoriaParks = "VictoriaParks"
VancouverParks = "VancouverParks"
CalgaryParks = "CalgaryParks"
EdmontonParks = "EdmontonParks"

VictoriaSchools = "VictoriaSchools"
VancouverSchools = "VancouverSchools"
CalgaryParks = "CalgarySchools"
EdmontonParks = "EdmontonSchools"



connection = psycopg2.connect(user="postgres",
                                      password="VXVictRB#",
                                      host="localhost",
                                      port="5432",
                                      database="postgres")

