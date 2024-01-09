from Note.models import Note
from Note.serializers import NoteSerializer, UserSerializer
from django.http import Http404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, permissions, authentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'login': reverse('login', request=request, format=format),
        'logout': reverse('logout', request=request, format=format),
        'user': reverse('user', request=request, format=format),
        'notes': reverse('notes', request=request, format=format),
        'register_user': reverse('register', request=request, format=format)
    })

@api_view(['POST'])
def login_view(request):
    username = request.data['username']
    password = request.data['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return Response({"message":"Login successful"},status=status.HTTP_200_OK)
    else:
        return Response({"message":"Login failed"},status=status.HTTP_401_UNAUTHORIZED)
    
@api_view(['POST'])
@authentication_classes([authentication.SessionAuthentication])
@permission_classes([permissions.IsAuthenticated])
def logout_view(request):
    logout(request)
    return Response({"message":"Logout Successful"},status=status.HTTP_200_OK)
    
class RegisterUser(generics.CreateAPIView):
    """
    Register a new user.
    """
    #permission_classes = []
    serializer_class = UserSerializer

    def create(self, request):
        if request.user.is_authenticated():
            return Response
        return 

@api_view(['POST'])
def register_user(request):
    if request.user.is_authenticated:
        return Response({"message": "Not allowed while logged in"}, status=status.HTTP_400_BAD_REQUEST)
    
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserDetail(generics.ListAPIView):
    """
    View authenticated user details.
    """
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.SessionAuthentication]
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(username=self.request.user)

class NoteList(APIView):
    """
    List all notes, or create a new note.
    """
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.SessionAuthentication]

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
    authentication_classes = [authentication.SessionAuthentication]

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