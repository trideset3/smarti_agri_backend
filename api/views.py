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
    with connection.cursor() as cursor:
        cursor.execute("""WITH getFieldsCTE (field_id, field_code, field_name, mun_name, soil_type, area_ha, state, yield_amount, season_id, 
    season_name, season_start, culture_id, culture_name, sort_name, eco_production, geom) 
AS (
    SELECT 
        field_id, 
        field_code, 
        field_name, 
        mun_name, 
        soil_type, 
        area_ha, 
        state, 
        yield_amount, 
        season_id, 
        season_name, 
        season_start, 
        culture_id, 
        culture_name, 
        sort_name, 
        eco_production, 
        geom
    FROM 
        public._v_fields_details
    ORDER BY
        season_id DESC,
        field_name DESC
)

SELECT json_build_object(
    'type', 'FeatureCollection',
    'crs',  json_build_object(
        'type',      'name', 
        'properties', json_build_object(
            'name', 'EPSG:4326'  
        )
    ), 
    'features', json_agg(
        json_build_object(
            'type',       'Feature',
            'id',        field_id, -- the GeoJson spec includes an 'id' field, but it is optional, replace {id} with your id field
            'geometry',   ST_AsGeoJSON(geom)::json,
            'properties', json_build_object(
                -- list of fields
                'field_id', field_id,
                'field_code', field_code,
                'field_name', field_name,
                'mun_name', mun_name,
                'soil_type', soil_type,
                'area_ha', area_ha, 
                'state', state,
                'yield_amount', yield_amount,
                'season_id', season_id,
                'season_name', season_name,
                'season_start', season_start,
                'culture_id', culture_id,
                'culture_name', culture_name,
                'sort_name', sort_name,
                'eco_production', eco_production
            )
        )
    )
)
FROM 
    getFieldsCTE

""")
        data = dictfetchall(cursor)

    return HttpResponse(json.dumps(data))

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
