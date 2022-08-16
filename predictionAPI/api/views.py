from django.shortcuts import render
from.apps import ApiConfig
from rest_framework.views import APIView
from rest_framework.response import Response
import numpy as np

# Create your views here.

class Predictions(APIView):
    def post(self,request):
        data = request.data
        data_info =np.array(list(data.values())).reshape(1,-1)
        predict= ApiConfig.model.predict(data_info)

        return Response(predict)
        
