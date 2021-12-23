from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from shapely.geometry import Point
from geoalchemy2 import Geometry
from models import *

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://postgres:VXVictRB#@localhost:5432/postgres"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)



#https://flask-admin.readthedocs.io/en/v1.0.9/db_geoa/ 
#Read Geometeries
class VancouverBus(db.Model):
    __tablename__ = 'VancouverBusiness'
    id = db.Column(db.Integer(), primary_key=True)
    cityName = db.Column(db.String())
    BusinessID = db.Column(db.String(),primary_key=True)
    BusinessName = db.Column(db.String())
    BusinessType = db.Column(db.String())
    BusinessHours = db.Column(db.Integer())
    Point = db.Column(Geometry("POINT"))
    CityID = db.Column(db.Integer())

    #def __init__(self, name, model, doors)
    def __init__(self,id,cityName,BusinessID,BusinessName,BusinessType,BusinessHours,Point,CityID):
        self.id = id
        self.cityName = cityName
        self.BusinessID = BusinessID
        self.BusinessName = BusinessName
        self.BusinessType = BusinessType
        self.BusinessHours = BusinessHours
        self.Point = Point
        self.CityID = CityID



def resultsBusiness(businesses):
    results = [
        {
            "id":  business.id,
            "cityName": business.cityName,
            "businessID": business.BusinessID,
            "businessName": business.BusinessName,
            "businessType": business.BusinessType,
            "businessHours": business.BusinessHours,
            "point": business.Point,
            "cityID": business.CityID
        } for business in businesses]

    return results

def resultsRestaurants():
    pass


def resultsParks():
    pass

def resultsSchool():
    pass


@app.route("/")
def Canada():
    return render_template("Canada.html")


@app.route("/Vancouver", methods=["Get"])
def Vancouver():
   VancouverBuss = VancouverBus.query.all()
   #VancouverRess = VancouverRes.query.all()

   return render_template("Vancouver/Vancouver.html")



@app.route("/Victoria")
def Victoria():
    return render_template("Victoria/Victoria.html")


@app.route("/Calgary")
def Calgary():
    return render_template("Calgary/Calgary.html")

@app.route("/Edmonton")
def Edmonton():
    return render_template("Edmonton/Edmonton.html")



if __name__=="__main__":
    app.run()