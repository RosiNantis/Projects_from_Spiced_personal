import time
from faker import Faker

import pymongo

fake = Faker()

# establish connection to client
# if only one client is running:
client = pymongo.MongoClient()

# if you want to specify a certain one:
#  client = pymongo.MongoClient('localhost', port=27017) # pointer to the client

# instead of 'localhost' you can also use the even more general IP of the client. To determine the IP: 
# 1.) docker ps --> docker container name
# 2a.) docker inspect <container name or ID> and then scroll and search, or:
# 2b.) docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' <container name or ID>

# define db 
db = client.my_db # 'my_db' is name of db

# empty the database
client.drop_database('my_db')

# define collection
dbcoll = db.my_collection # includes database and collection name


# 20 seconds long loop to save fake tweets as documents to database
    
t_end = time.time() + 20
while time.time() < t_end: # infinitively long loop with: while True:
    
    time.sleep(3) # pause for 3 seconds
    fake_doc = {'found_tweet' : {'time':time.asctime(),'tweet':fake.text()}}

    dbcoll.insert_one(fake_doc) # fake_doc is document


# print the fake twitter news
for my_doc in db.my_collection.find():
  print(my_doc, end='\n\n') 


# when was the last tweet sent?
my_doc['found_tweet']
my_doc['found_tweet']['time']



# in subsequent encounters you will learn to do ETL on such mongodb documents.