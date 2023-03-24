from flask import Flask,request,jsonify
import pickle
import pandas as pd

app=Flask(__name__)

model = pickle.load(open('modelTrackIt.pkl','rb'))

@app.route('/')
def home():
    return jsonify({'greetings' : 'Hi! this is python'}) #returning key-value pair in json format

@app.route("/predict",methods=["GET"])
def predict():
    latitudeStart = request.args.get('LatitudeStart')
    print(latitudeStart)
    longitudeStart = request.args.get('LongitudeStart')
    print(longitudeStart)
    latitudeEnd = request.args.get('LatitudeEnd')
    print(latitudeEnd)
    longitudeEnd = request.args.get('LongitudeEnd')
    print(longitudeEnd)
    distance = request.args.get('Distance')
    print(distance)
    time_secs=request.args.get('time_secs')
    print(time_secs)
    makePrediction = model.predict([[latitudeStart,longitudeStart,latitudeEnd,longitudeEnd,distance,time_secs]])
    output =round(makePrediction[0],5)

    return jsonify({'The time is':output})


if __name__=="__main__":
    app.run(debug=True)


