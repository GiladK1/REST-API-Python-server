import logging
from bottle import run,get,post,request,delete

'''
################################################
Hello there,

#################################################
'''


#Create and configure logger.
logging.basicConfig(filename="D:\\ActivityLog.Log",
    level = logging.DEBUG,
    format='%(levelname)s--%(asctime)s -- %(message)s',
    filemode='w')
logger = logging.getLogger()
logger.info("#Our server is up")

#This is my selected data structure - a Dictionary.
animals = [{'name':'snake','number':'1'},{'name':'dog','number':"2"}]
logger.debug("#Dictionary data type was created")

#Define a Get request   - fetch the entire data .
@get('/animals')
def get():
    logger.debug("# Return the animels dictionary as JSON (get)")
    try:
        return {'animals':animals}
    except:
        logger.error("#An error occurred while retrun the data type !(get) ")

#Define a Post request - fetch a specific name .
@post('/animal/<name>')
def getOne(name):
    logger.info("#Looking for the specific animal")
    the_animal = [animal for animal in animals if animal['name'] == name]
    try:
        return {'animal' : the_animal[0]}
    except:
        looger.error("# Error while looking for the specific animal !")
        

#Define a Post request - add new animal.
@post('/animal')
def addOne():
    logger.debug("#Creates a new animal")
    new_animal ={ 'name':request.json.get('name'),'number':request.json.get('number')}
    logger.debug("# appending the new animal to the data type (post)")
    animals.append(new_animal)
    try:
        return {'animals':animals}
    except:
        logger.error("#An error occurred while appending the new animal ! (post)" )

#Define a Delete request - delete an animal.
@delete('/animal/<name>')
def removeOne(name):
    logger.info("#Looking for the animal")
    the_animal = [animal for animal in animals if animal['name'] == name]
    try:
        animals.remove(the_animal[0])
    except:
        logger.error("#An error occurred while remove the animal !")
    logger.debug("#animal successfully removed")
    try:
        return {'animals':animals}
    except:
         logger.error("#An error occurred while return the new animal data type after removing ! " )



run(reloader=True, debug=True)
