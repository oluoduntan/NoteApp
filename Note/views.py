from django.shortcuts import render
from Note.models import Note
from Note.serializers import NoteSerializer, UserSerializer
from django.http import Http404, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, permissions
from rest_framework.response import Response
from Note.permissions import IsOwnerOrReadOnly
from django.contrib.auth.models import User

from rest_framework.decorators import api_view
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'user': reverse('user', request=request, format=format),
        'notes': reverse('notes', request=request, format=format)
    })

class UserDetails(generics.ListAPIView):
    #queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(username=self.request.user)

# Create your views here.
def home(request):
    return render(request, "Note/index.html")

class NoteList(APIView):
    """
    List all notes, or create a new note.
    """
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, format=None):
        notes = self.request.user.note.all()
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)
    
class NoteDetail(APIView):
    """
    Retrieve, update or delete a note instance.
    """
    permission_classes = [permissions.IsAuthenticated]
    def get_object(self, pk):
        try:
            #return Note.objects.get(pk=pk, owner=self.request.user)
            return self.request.user.note.all().get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        note = self.get_object(pk)
        serializer = NoteSerializer(note)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        note = self.get_object(pk)
        serializer = NoteSerializer(note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        note = self.get_object(pk)
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)