from pymongo import MongoClient
import pprint

client = MongoClient("mongodb://naomi:naomi28@ds151382.mlab.com:51382/conversation")

db = client['conversation']
messages_collection = db['messages']

def insert_message(json):
    if((json.get('user_name')==None and json.get('message')==None) or (json.get('user_name')==None)):
        print('no message')
    else:
        messages = {
            'from': json.get('user_name'),
            'message': json.get('message')
        }
        print(messages)
        message_id = messages_collection.insert_one(messages).inserted_id
        print('inserted')

all_messages = messages_collection.find()

def allMessages():
    messages = []
    for mes in messages_collection.find():
        print("Query")
        messages.append(mes)
    return messages
