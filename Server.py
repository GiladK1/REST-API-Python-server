import pytest
import requests
import json
import logging
'''
################################################
This is the test file
#################################################
'''

#Create and configure the test logger.
logging.basicConfig(filename="TestingLog.Log",
    level = logging.DEBUG,
    format='%(levelname)s--%(asctime)s -- %(message)s',
    filemode='w')
logger = logging.getLogger()
logger.info("#Our server is up")


#This test is sending a post request to the server(insert data) and receive an update that the
# request worked correctly.
def insertDataTest(type,id,name):
    url = 'http://127.0.0.1:5000/animals'
    payload = {type: {id:name}}
#Insert data as JSON
    headers = {'content-type': 'application/json'}
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    if (response.status_code == 200):
        print("(POST)http://127.0.0.1:5000/animals "
              " --Information entered successfully, Test successful(code:200)"
              "type: %s name: %s id: %s "% (type, name ,id))
        logger.info("(POST) http://127.0.0.1:5000/animals "
              "--Information entered successfully, Test successful(code:200)%s %s %s "%(type, name ,id))
    else:
        print("(POST) http://127.0.0.1:5000/animals-- An error occurred - Test failed |"+"Error code: %d."
                     % response.status_code)
        logger.error("(POST) http://127.0.0.1:5000/animals-- An error occurred - Test failed |"+"Error code: %d."
                     % response.status_code)
    #OR
    # assert(response.status_code) == 200 # OK


#This test will fetch the entire data
def fetchAll():
    r = requests.get("http://127.0.0.1:5000/animals")
    if (r.status_code == 200):
        print("(GET) http://127.0.0.1:5000/animals-- Information fetch successfully, "
                    "Test successful( code:200)")
        logger.info("(GET) http://127.0.0.1:5000/animals-- Information fetch successfully, "
                    "Test successful( code:200)")
    else:
        print("An error occurred - Test failed |" + "Error code: %d. " % r.status_code)
        logger.error("An error occurred - Test failed |" + "Error code: %d. " % r.status_code)
    #OR
    #assert (r.status_code) == 200 #OK

#This test will fetch a specific type
def fetchOne(name):
    r = requests.get("http://127.0.0.1:5000/animal/"+name)
    if (r.status_code == 200):
        print(" (GET) http://127.0.0.1:5000/animal/ --Information fetch successfully for one animal,"
              " Test successful(code:200) animal name: %s" %name)
        logger.info("(GET) http://127.0.0.1:5000/animal/Information fetch successfully for one animal,"
                    " Test successful(code:200) animal name: %s" % name)
    else:
        print("(GET) http://127.0.0.1:5000/animal/ An error occurred - Test failed  |"
              " " + "Error code: %d. " % r.status_code +"name: %s" %name)
        logger.error("(GET) http://127.0.0.1:5000/animal/ An error occurred - Test failed  |"
              " " + "Error code: %d. " % r.status_code +"name: %s" %name)
    #OR
    #assert (r.status_code) == 200 #OK



insertDataTest("dog","10","rafi")
fetchAll()
fetchOne("dog3")
fetchOne("noSuchAnimal") # Negative test with will respond back that an item haven’t been found  .

