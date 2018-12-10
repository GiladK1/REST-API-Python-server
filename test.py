import pytest
import requests
import json
import logging
'''
################################################
Hello there,
This is my test file (using Pytest) for the Amdocs interview task.
Hope you'll enjoy it,
Gilad Kameri.

www.GiladK.com
GiladKameri@gmail.com
#################################################
'''

#Create and configure logger.
logging.basicConfig(filename="D:\\TestingLog.Log",
    level = logging.DEBUG,
    format='%(levelname)s--%(asctime)s -- %(message)s',
    filemode='w')
logger = logging.getLogger()
logger.info("#Our server is up")


#This test is sending a post request to the server(insert data) and receive an update that the
# request worked correctly.
def insertDataTest(name,number):
    url = 'http://127.0.0.1:8080/animal'
    payload = {"name": name, "number":number} #Insert data as JSON
    headers = {'content-type': 'application/json'}
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    if (response.status_code == 200):
        print("Information entered successfully, Test successful(code:200)")
        logger.info("Information entered successfully, Test successful(code:200)")
    else:
        print("An error occurred - Test failed |"+"Error code: %d. " % response.status_code)
        logger.error("An error occurred - Test failed |"+"Error code: %d. " % response.status_code)
    #OR
    # assert(response.status_code) == 200 # OK


#This test will fetch the entire data
def fetchAll():
    r = requests.get("http://127.0.0.1:8080/animals")
    if (r.status_code == 200):
        print("Information fetch successfully, Test successful( code:200)")
        logger.info("Information fetch successfully, Test successful( code:200)")
    else:
        print("An error occurred - Test failed |" + "Error code: %d. " % r.status_code)
        logger.error("An error occurred - Test failed |" + "Error code: %d. " % r.status_code)
    #OR
    #assert (r.status_code) == 200 #OK

#This test will fetch a specific type
def fetchOne(name):
    r = requests.post("http://127.0.0.1:8080/animal/"+name)
    if (r.status_code == 200):
        print("Information fetch successfully for one animal, Test successful(code:200)")
        logger.info("Information fetch successfully for one animal, Test successful(code:200)")
    else:
        print("An error occurred - Test failed | " + "Error code: %d. " % r.status_code)
        logger.error("An error occurred - Test failed | " + "Error code: %d. " % r.status_code)
    #OR
    #assert (r.status_code) == 200 #OK




insertDataTest("fish","3")
fetchAll()
fetchOne("fish")
fetchOne("noSuchAnimal") # Negative test with will respond back that an item haven’t been found  .

