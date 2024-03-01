from flask import Flask, jsonify
import random
import sqlite3

conn = sqlite3.connect("statistics.sqlite")
app = Flask(__name__)

def get_data(id):
    cursor = conn.cursor()

    if id==1: #speedometer
        cursor.execute("select speed from stats")
        for i in cursor:
        
            return i[0] 
        
    elif id==2: #odometer
        cursor.execute("select distance from stats")
        for i in cursor:
        
            return i[0] 
        
    elif id==3: #temperature
        cursor.execute("select temperature from stats")
        for i in cursor:
            return i[0] 
        
    elif id ==4:    #Battery 
        cursor.execute("select battery from stats")
        for i in cursor:
            return i[0] 
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
    if stat_id ==1:
        return jsonify({"Current Speed": dt, "Unit": "Kmph"})
    elif stat_id ==2:
        return jsonify({"Distance Covered:": dt,"Unit":"Km"})
    elif stat_id ==3:
        return jsonify({"Current Temperature of the engine:":round(dt,2),"Unit":"°C"})
        # return "Current Temperature of the engine: {} °C".format(round(dt,2))
    elif stat_id == 4:
        return jsonify({"Battery left ":dt,"Unit":"%"})
    else:
        return "Not Implemented Yet"
        


if __name__=='__main__':
    app.run(debug=True)