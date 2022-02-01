""" View for handling CRUD operations """
import uuid
from django.http import JsonResponse
from myapp.models import Movie
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status
from myapp.serializers import MovieSerializer

# Create your views here.

@api_view(['GET', 'POST', 'DELETE'])
def MovieDetails(request):
    """ 
        GET: This method deals can get you all the values from database, 
             if specified id will fetch you specific records
        
        POST: This method creates a new entry and throws exception if already exists

        DELETE: This method will facilitate bulk and specific deletion if id is mentioned
    """

    if request.method == 'DELETE':
        idd = request.query_params.get('id', None)
        name = None
        if idd is not None:
            try:
                data = Movie.objects.get(id=idd)
            except Movie.DoesNotExist:
                return JsonResponse(
                    {
                        'message': 'The movie does not exist',
                        "id": idd
                    }, status=status.HTTP_404_NOT_FOUND
                )
            name = data.name
            count = data.delete()
            return JsonResponse(
                {
                    'message': f'{count[0]} movies were deleted successfully!',
                    "id": idd,
                    "name": name
                }, status=status.HTTP_200_OK
            )

        count = Movie.objects.all().delete()
        if count[0] == 0:
            return JsonResponse(
                {
                    'message': 'No movies exist'
                }, status=404
            )
        return JsonResponse(
            {
                'message': f'{count[0]} movies were deleted successfully!'
            }, status=200
        )

    elif request.method == 'POST':
        movie_data = JSONParser().parse(request)
        idd  = movie_data.get('id', None)
        if idd is None:
            movie_data['id'] = uuid.uuid1()
        movie_serializer = MovieSerializer(data=movie_data)
        if movie_serializer.is_valid():
            movie_serializer.save()
            return JsonResponse(
                {
                    'message': 'Movie was created successfully!',
                    "name": movie_data.get('name'), 
                    "id": movie_data.get('id')
                }, status=status.HTTP_201_CREATED
            )
        return JsonResponse(movie_serializer.errors)

    elif request.method == 'GET':
        data = Movie.objects.all()
        idd = request.query_params.get('id', None)
        if idd is not None:
            try:
                data = Movie.objects.get(id=idd)
            except Movie.DoesNotExist:
                return JsonResponse(
                    {
                        "errorMsg": f"Invalid movie id: {idd}",
                        "id": idd
                    }, status=status.HTTP_404_NOT_FOUND
                )
            movie_serializer = MovieSerializer(data, many=False)
        else:
            movie_serializer = MovieSerializer(data, many=True)
        return JsonResponse(
            {"data": movie_serializer.data, "id": idd},
            safe=False, status=status.HTTP_200_OK
        )

@api_view(['PUT', 'DELETE', 'GET'])
def query_using_id(request, idd):

    try: 
        movie = Movie.objects.get(id=idd)
    except Movie.DoesNotExist: 
        return JsonResponse(
            {
                'message': 'The Movie does not exist',
                "id": idd
            }, status=status.HTTP_404_NOT_FOUND
        )

    if request.method == 'PUT':
        movie_data = JSONParser().parse(request)
        if movie_data['id'] != idd:
            return JsonResponse(
                {"forbidden": "id field is immutable"},
                status=status.HTTP_403_FORBIDDEN
            )
        movie_serializer = MovieSerializer(movie, data=movie_data)
        if movie_serializer.is_valid():
            movie_serializer.save()
            return JsonResponse(
                {
                    "message": 'Updated details successfully',
                    "id": idd,
                    "name": movie.name
                }, status=status.HTTP_200_OK
            )
        return JsonResponse(
            {"error":movie_serializer.errors, "id": idd},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    if request.method == 'GET':
        try:
            data = Movie.objects.get(id=idd)
        except Movie.DoesNotExist:
            return JsonResponse(
                {
                    "errorMsg": f"Invalid movie id: {idd}",
                    "id": idd
                }, status=status.HTTP_404_NOT_FOUND
            )
        movie_serializer = MovieSerializer(data, many=False)

        return JsonResponse(
            {
                "data": movie_serializer.data, 
                "id": idd
            },safe=False, status=status.HTTP_200_OK
        )
    
    if request.method == 'DELETE':
        try:
            data = Movie.objects.get(id=idd)
        except Movie.DoesNotExist:
            return JsonResponse(
                {
                    'message': 'The movie does not exist',
                    "id": idd
                }, status=status.HTTP_404_NOT_FOUND
            )
        name = data.name
        data.delete()
        return JsonResponse(
            {
                'message': 'Movie deleted successfully!',
                "id": idd,
                "name": name
            }, status=status.HTTP_200_OK
        )
