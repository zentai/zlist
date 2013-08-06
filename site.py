#!/usr/local/bin/python2.7
import cherrypy
import yaml
import logging.config
import os 
from task import Tasklist

def setup_logging(default_level=logging.INFO, env_key='LOG_CFG'):
    logging.basicConfig(level=default_level)
    path = os.getenv(env_key, 'logging.yaml')
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.load(f.read())
            logging.config.dictConfig(config)
    logging.getLogger(__name__).info("logging setup")
    
if __name__ == '__main__':
    cherrypy.config.update({
        # 'environment': 'production',
        'log.screen': False,
        'server.socket_host': '0.0.0.0',
        'server.socket_port': 20313,
    })

    cherrypy.tree.mount(
            Tasklist(), '/api/tasklist',
            {'/':
                {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
            }
    )
    setup_logging()
    cherrypy.engine.start()
    cherrypy.engine.block()
