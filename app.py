from pymongo import MongoClient
import time
from datetime import datetime

print("[ Pymongo ][ Opening connection ]")

# TODO Encrypt
client = MongoClient("mongodb+srv://connectString")

the_db = client.get_database('the_db')

timestamp = int(time.time()*1000.0)
new_echo = {
    'milliseconds': timestamp,
    'datetime': datetime.now(),
    'readed': 0
}

updated_tail = {
    'milliseconds': new_echo['milliseconds'],
    'datetime':  new_echo['datetime'],  
    'readed':  new_echo['readed'],
}

the_db.echo.insert_one(new_echo)
the_db.echo2.update_one({'unique': 1}, {'$set': updated_tail})

client.close()
print("[ Pymongo ][ Closing connection ]")
