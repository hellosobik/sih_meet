from appwrite.client import Client
from appwrite.services.databases import Databases
from appwrite.id import ID
from appwrite.query import Query
import pprint
import json
client=Client()

client.set_endpoint("https://cloud.appwrite.io/v1")
client.set_project("65190e54854144c213e3")
client.set_key("dd0297f256aed3eb659e9100bf62af805ce7cfdd3bdae14fc7b01d415702a415fc62bb8089790c309bd3124f87f8bc52164e184e9f836c935cfa00bd468c0c54f788bc9f22a6f6cf1e052375da629c438f5e9e36ca86bf70453881fd12df0db0d5e57be3019b33c7e4deba50017d75a7035f3eaa98078fb38496bb2ace21e130")

db=Databases(client)

# Create operations-------------------------------------------------

# response=db.create(database_id="demo_db", name="demo_db")

# response=db.create_collection(database_id="demo_db", collection_id="demo_collection", name="demo_collection")

# response=db.create_string_attribute(database_id="demo_db", collection_id="demo_collection", key="user_id", size=50, required=True)

# response=db.create_string_attribute(database_id="demo_db", collection_id="demo_collection", key="name", size=50, required=True)

# response=db.create_string_attribute(database_id="demo_db", collection_id="demo_collection", key="password", size=50, required=True)

# response=db.create_document(
#     database_id="demo_db",
#     collection_id="demo_collection",
#     document_id=ID.unique(),
#     data={"user_id":"nitesh", "name":"nitesh kumar paswan", "password": "nitesh_k_paswan"}
# )

# Read operations---------------------------------------------------

# response=db.list()
# print(response)

# response=db.list_collections(database_id="demo_db")
# print(response)

# response=db.list_documents(database_id="demo_db", collection_id="demo_collection")
# print(response)

# Update operations--------------------------------------------------

# response=db.update(database_id="demo_db", name="demo_db_new")

# response=db.update_collection(database_id="demo_db", collection_id="demo_collection", name="demo_collection_new")

# response=db.update_string_attribute(
#     database_id="demo_db",
#     collection_id="demo_collection",
#     key="user_id",
#     required=False,
#     default=""
# )

#Using query-------------------------------------------------------------

# response=db.list_documents(
#     database_id="demo_db", 
#     collection_id="demo_collection", 
#     queries=[
#         Query.equal(attribute="user_id", value="sobik")
#     ]
# )
#
# pprint.pprint(response['documents'][0]['$id'])

