from flask import Flask, request
from flask_restful import Resource, Api
import logging
import json
app=Flask(__name__)
api=Api(app)

'''
##############
This is my REST-API server upgrade using FLASK & JSON
Gilad 
##############
'''
#Create and configure logger.
logging.basicConfig(filename="ActivityLog.Log",
    level = logging.DEBUG,
    format='%(levelname)s--%(asctime)s -- %(message)s',
    filemode='w')
logger = logging.getLogger()
logger.info("#server is up - Using FLASK")

#Load from the  JSON D.B to a nested Dictionary (the file is in the same folder)
with open('animals.json') as f:
    animalsJSON=json.load(f)

## OOP ##
class Animals(Resource):
    #This function fetch the all animals (GET request)
    def get(self):
        logger.info("#GET req. url -- http://127.0.0.1:5000/animals -- fetching the all animals %s",
                    animalsJSON)
        return animalsJSON
    #This function is adding a new animal (POST request)
    def post(self):
        newJASON = request.get_json() #Get the JASON
        animalsJSON.update(newJASON) # insert the new data
        logger.info("#POST req. url -- http://127.0.0.1:5000/animals -- Insert a new animal : %s",
                    animalsJSON)
        updateDB() # Updating the DB - JASON file after insertion
        logger.info("#DB - JSON file is updated",
                    animalsJSON)
        return animalsJSON

#OOP#
class Animal(Resource):
    #This function fetch spacific animal by type (GET request)
    def get(self,name):
        logger.info("#GET req. url -- http://127.0.0.1:5000//animal/%s' -- Get all the animals from the chosen"
                    "type :%s ---%s",
                    name, animalsJSON[name])
        return animalsJSON[name]

#This function is used to updated our DB - JASON file
def updateDB():
    with open('animals.json', 'w') as outfile:
        json.dump(animalsJSON, outfile)
        logger.info("#Updating the DB JASON file------ : %s",
                animalsJSON)

api.add_resource(Animals,'/animals')
api.add_resource(Animal,'/animal/<string:name>')


if __name__ =='__main__':
    app.run(debug=True)
