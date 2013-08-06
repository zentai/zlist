import datetime
import cherrypy
import logging
import hashlib
from settings import db
from pymongo import MongoClient

class Tasklist:
    exposed = True
    def __init__(self):
        client = MongoClient(db.get("MONGODB_IP"), db.get("MONGODB_PORT"))
        client.admin.authenticate(db.get("USER"), db.get("PASS"))
        self.table = client.zlist.tasklist

    def GET(self):
        self.logger = logging.getLogger(__name__)
        cursor = self.table.find()
        self.logger.info("[GET] Tasklist: %s items" % cursor.count())
        return [ str(record) for record in cursor]
