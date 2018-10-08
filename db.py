from pymongo import MongoClient
import pprint

def connect():
    client = MongoClient("mongodb://naomi:naomi28@ds151382.mlab.com:51382/conversation")
    db = client['conversation']
    return db['messages']

def insert_message(json):
    messages_collection = connect()
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

def allMessages():
    messages_collection = connect()
    messages = []
    for mes in messages_collection.find():
        print("Query")
        messages.append(mes)
    return messages
