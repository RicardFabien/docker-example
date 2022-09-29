# from __future__ import absolute_import

from sqlite3 import Cursor
from flask import Flask
from flask import jsonify
from flask_cors import CORS, cross_origin
import mysql.connector

from pymaze.src.maze_manager import MazeManager
from pymaze.src.maze import Maze


app = Flask(__name__)
CORS(app, support_credentials=True)

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
    maze : Maze = manager.add_maze(10, 10)

    


    return jsonify({"name":value, "data": maze.grid})

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True,port=8080)