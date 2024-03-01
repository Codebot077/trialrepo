from flask import Flask, jsonify
from flask_cors import CORS
import random
import sqlite3

app = Flask(__name__)
CORS(app)

def get_data(id):
    

    if id==1: #speedometer
        conn = sqlite3.connect("statistics.sqlite")
        cursor = conn.cursor()
        cursor.execute("select speed from stats")
        data = cursor.fetchall()
        i = random.choice(data)
        return i[0] 
        
    elif id==2: #odometer
        conn = sqlite3.connect("statistics.sqlite")
        cursor = conn.cursor()
        cursor.execute("select distance from stats")
        data = cursor.fetchall()
        i = random.choice(data)
        return i[0]
        
    elif id==3: #temperature
        conn = sqlite3.connect("statistics.sqlite")
        cursor = conn.cursor()
        cursor.execute("select temperature from stats")
        data = cursor.fetchall()
        i = random.choice(data)
        return i[0] 
        
    # elif id ==4:    #Battery 
    #     cursor.execute("select battery from stats")
    #     for i in cursor:
    #         return i[0] 
    else:
        return "Invalid"

# @app.route("/")
# def index():
#     return "Hello World"

@app.route("/stats",methods =  ['GET'])
def data():
    # stat_id = int(stat_id)
    speed_dt = get_data(1)
    odo_dt = get_data(2)
    temp_dt = get_data(3)
    # speed_dt = get_data(stat_id)
    ans = {
        'speed': speed_dt,
        'temperature': temp_dt,
        'odometer': odo_dt
    }

    return jsonify(ans)


if __name__=='__main__':
    app.run(debug=True)