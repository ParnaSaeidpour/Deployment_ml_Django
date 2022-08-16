from json import encoder
from django.apps import AppConfig
import os
import joblib
from django.conf import settings


class ApiConfig(AppConfig):
    name = 'api'
    MODEL_ENCODER = os.path.join(settings.MODELS,"encoder.joblib")
    MODEL_FILE = os.path.join(settings.MODELS,"my_model.joblib")
    encoder = joblib.load(MODEL_ENCODER)
    model = joblib.load(MODEL_FILE)
