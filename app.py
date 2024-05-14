import uvicorn
from fastapi import FastAPI
from WeatherX import WeatherX
import pickle

app = FastAPI()
pickle_in = open("prediktor.pkl", "rb")
cv = pickle.load(pickle_in)


@app.get('/')
def index():
    return {'message': 'Hello, World'}


@app.post('/predict')
def predict_weather(data: WeatherX):
    data = data.dict()
    precipitation = data['precipitation']
    temp_max = data['temp_max']
    temp_min = data['temp_min']
    wind = data['wind']

    prediction = cv.predict([[precipitation, temp_max, temp_min, wind]])

    if prediction == 0:
        weather_condition = "Drizzle"
    elif prediction == 1:
        weather_condition = "Fog"
    elif prediction == 2:
        weather_condition = "Rain"
    elif prediction == 3:
        weather_condition = "Snow"
    else:
        weather_condition = "Sun"

    return {'prediction': weather_condition}


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
