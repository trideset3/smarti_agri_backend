from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
#from .serializers import SeasonsSerializer
from .models import Seasons, Fields
from django.http import HttpResponse
from django.core.serializers import serialize
from django.db import connection
import json


def getFields(request):
    data=Fields.objects.all().order_by('-season')
    data_json = serialize('geojson', data, geometry_field='geom')
    return HttpResponse(data_json)

def getSeasons(request):
    data=Seasons.objects.all().order_by('-season_start')
    data_json = serialize('json', data)
    return HttpResponse(data_json)

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def getFieldDetails(request):
    field_code = request.GET.get("field_code")
    with connection.cursor() as cursor:
        cursor.execute("""SELECT 
	season_name,
	culture_name,
	sort_name,
	eco_production,
	yield_amount
FROM 
	_V_fields_details
WHERE 
	field_code = %s
ORDER BY
	season_start desc""", [field_code])
        data = dictfetchall(cursor)

    return HttpResponse(json.dumps(data))

# class SeasonsViews(APIView):
#     def post(self, request):
#         serializer = SeasonsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
#         else:
#             return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
