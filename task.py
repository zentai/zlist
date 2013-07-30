import datetime
import cherrypy
import logging
import hashlib
# mongo db lib
from pymongo import Connection
MONGODB_PORT = 19701
username='walao81@gmail.com'
password='qwertyuiop.81'

class Tasklist:
    exposed = True
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        connection = Connection('localhost', MONGODB_PORT)
        self.db = connection.smallcase
        self.db.authenticate("admin", "zhijian.81")
        self.table = self.db.zlist
        self.logger.info("Zlist init: Connection('%s', %s)" % ('localhost', MONGODB_PORT) )

    def GET(self, id=None):
        if not id:
            cursor = self.table.find()
            return dict((record['_id'], record) for record in cursor)
        else:
            cursor = self.table.find({'tags': tag, 'active': True})
            return dict((record['_id'], record) for record in cursor)
