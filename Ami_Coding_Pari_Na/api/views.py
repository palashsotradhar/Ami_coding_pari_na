from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from khoj_the_search.models import khojm
from .serializers import apis
# Create your views here.

#This function is used for proper use of drf. and by this i can create a JSON output by take some JSON input.
@api_view(['GET','POST'])
def api(request):
    if request.method == 'GET':
        return Response({})
    if request.method == 'POST':
        start = request.data['start_time']
        end = request.data['end_time']
        uid = request.data['id']
        idd = khojm.objects.filter(user_id = uid,timestamp__range=(start, end))
        sr = apis(idd,many=True)
        print(sr.data)
        return Response({'status':'succes','user_id':uid,'payload':sr.data})
