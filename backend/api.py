# from __future__ import absolute_import

import json
from sqlite3 import Cursor
from types import SimpleNamespace
from flask import Flask
from flask import jsonify
from flask_cors import CORS, cross_origin
from flask_socketio import SocketIO,send
import mysql.connector

from pymaze.src.maze_manager import MazeManager
from pymaze.src.maze import Maze


app = Flask(__name__)
app.config["SECRET"] = "I'm a secret"
socket_io = SocketIO(app, cors_allowed_origin = "*")
# CORS(app, support_credentials=True)




@app.route('/')
@cross_origin(supports_credentials=True)
def hello():
    value = "no database"

    # cnx = mysql.connector.connect(user='root', password='root',host='database',database ="test")
    
    # cursor:Cursor = cnx.cursor()
    # cursor.execute("SELECT name FROM NAMES where id=1")

    # value=cursor.fetchone()

    # cursor.close()
    # cnx.close()

    manager = MazeManager()
    maze : Maze = manager.add_maze(5, 5)

    return maze.toJSON()
    return jsonify({"name":value})

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True,port=8080)