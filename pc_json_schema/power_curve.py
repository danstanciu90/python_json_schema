from pydantic import BaseModel, Field
from enum import Enum
import json

class WindSpeed(BaseModel):
    min: int = Field(..., description="Minimum wind speed in m/s")
    max: int = Field(..., description="Maximum wind speed in m/s")

class PowerCurveMode(str, Enum):
    default = "default"
    custom = "custom"
    low_noise = "low_noise"
    low_speed = "low_speed"
    high_speed = "high_speed"

class PowerCurve(BaseModel):
    wind_speed: WindSpeed = Field(description="Wind speed range in m/s")
    power: int = Field(description="Power in kW", examples=[100, 200, 300])
    modes: PowerCurveMode = Field(description="Power curve mode", default="low_noise")


schema = PowerCurve.model_json_schema()
print(json.dumps(schema, indent=2))

with open('json_schemas/power_curve_schema.json', 'w', encoding='utf-8') as out_file:
    json.dump(schema, out_file, indent=2)