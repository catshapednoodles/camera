import os.path
from flask import Flask
from flask.ext.autoindex import AutoIndex

HOST = "0.0.0.0"             # host ip adress do not change
PORT = 8080                  # only for debug and test environment. will change to 80 if product is released
DebugMode = True             # set to false if server is deployed
server = Flask(__name__)     # main server variable

AutoIndex(server, browse_root=os.path.curdir)

server.run(debug=DebugMode,host=HOST,port=PORT)