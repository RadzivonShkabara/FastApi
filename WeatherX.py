from pydantic import BaseModel

class WeatherX(BaseModel):
    precipitation: float
    temp_max: float
    temp_min: float
    wind: float