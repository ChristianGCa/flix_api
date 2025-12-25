#import json
#from django.http import JsonResponse
#from django.views.decorators.csrf import csrf_exempt
#from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission
from genres.models import Genre
from genres.serializers import GenreSerializer

class GenreCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class GenreRetrieveUpdateView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

# SEMPRE RETORNAR UM JSON RESPONSE NAS VIEWS
#@csrf_exempt
#def genre_create_list_view(request):
#    
#    if request.method == 'GET':
#    
#        genres = Genre.objects.all() # SELECT * FROM genres_genre;
#        data=[{'id': genre.id, 'name': genre.name} for genre in genres]
#        # é a mesma coisa que isso:
#        #data = []
#        #for genre in genres:
#        #    data.append({
#        #        'id': genre.id,
#        #        'name': genre.name
#        #    })
#        return JsonResponse(data, safe=False)
#
#    elif request.method == 'POST':
#
#        data = json.loads(request.body.decode('utf-8'))
#        new_genre = Genre(name=data['name'])
#        new_genre.save()  # INSERT INTO genres_genre (name) VALUES (data['name']);
#        return JsonResponse(
#            {'id': new_genre.id, 'name': new_genre.name},
#            status=201, # Created
#        )

#@csrf_exempt
#def genre_detail_view(request, pk):
#
#    # carrega o objeto ou retorna 404
#    genre = get_object_or_404(Genre, pk=pk)
#
#    if request.method == 'GET':
#        data = {'id': genre.id, 'name':genre.name}
#        return JsonResponse(data)
#    
#    elif request.method == 'PUT':
#        data = json.loads(request.body.decode('utf-8'))
#        genre.name = data['name']
#        genre.save()
#        return JsonResponse(
#            {'id': genre.id, 'name': genre.name},
#            status=201, # Created
#        )
#    
#    elif request.method == 'DELETE':
#        genre.delete()
#        return JsonResponse(
#            {'message': 'Genre deleted successfully.'},
#            status=204,
#        )