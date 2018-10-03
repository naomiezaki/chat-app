from pymongo import MongoClient
import pprint

client = MongoClient("mongodb://naomi:naomi28@ds151382.mlab.com:51382/conversation")

db = client['conversation']
messages_collection = db['messages']

def insert_message(json):
    if(json.get('user_name')==None and json.get('message')==None):
        print('no message')
    else:
        messages = {
            'from': json.get('user_name'),
            'message': json.get('message')
        }
        # messages = {
        #     'from': str(json.get('user_name')),
        #     'message': str(json.get('message'))
        # }
        print(messages)
        message_id = messages_collection.insert_one(messages).inserted_id
        print('inserted')

# messages = {
#     "user_name": "celty",
#     "message": "Hello"
# }

# message_id = messages_collection.insert_one(messages).inserted_id

# pprint.pprint(messages_collection.find_one())
