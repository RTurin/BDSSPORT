from django.http import JsonResponse
from django.shortcuts import render
import requests
# Create your views here.

# third party imports 11-feb 
from rest_framework.response import Response
from rest_framework.views import APIView


class Home(APIView):
    def get(self, request , *args, **kwargs):

        result = requests.get("https://api.opendota.com/api/players/107828036/matches")

        res = result.json()
        testVar = {}
        for r in res:
            testVar[r['match_id']] ={}
            for k in r.keys():
                if k == 'match_id': continue
                testVar[r['match_id']] [k] =r[k]

        playerKill = testVar[5619291363]['kills']
        
        print(playerKill)

        return Response(testVar)
    
# def Home(request):
#     context ={
#         'id':'100',
#         'name': 'Jhon'
#     }
#     # return render(request,"index.html",context)
#     return JsonResponse(context)
