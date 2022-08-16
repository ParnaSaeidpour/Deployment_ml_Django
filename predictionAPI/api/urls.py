from django.urls import path
from .views import Predictions

urlpatterns = [
    path('predict/', Predictions.as_view(), name='Predictions')
]



