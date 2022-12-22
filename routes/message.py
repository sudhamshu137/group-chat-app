from fastapi import APIRouter

from models.message import Message
from config.db import db
from schemas.message import serializeDict, serializeList
from bson import ObjectId

mes = APIRouter()

@mes.get("/")
def welcome():
    return {"message": "Welcome to group chat server"}

@mes.get("/message")
def getMessage():
    #message = db.message.find_one("message")
    #sender = db.message.find_one("sender")
    #info = {"message":message, "sender":sender}
    #return dict(info)
    #return dict(db.message.find({'_id':ObjectId("63a30aff82307c1f21e427b6")}))
    return serializeDict(db.message.find_one({'_id':ObjectId("63a30aff82307c1f21e427b6")}))

@mes.post("/message")
def postMessage(message : Message):
    #db.message.delete_many({})
    #db.message.insert_one(dict(message))
    #db.message.find_one_and_update({"_id": dict(ObjectId(oid="63a30aff82307c1f21e427b6"))}, {"$set": dict(message)})
    #filter = {'_id':ObjectId(oid="63a30aff82307c1f21e427b6")}
    db.message.update_one({'_id':ObjectId(oid="63a30aff82307c1f21e427b6")}, {"$set":{"message":message.message, "sender":message.sender}})
    #db.users.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(user)})

#63a30aff82307c1f21e427b6
