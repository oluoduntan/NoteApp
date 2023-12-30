from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Note



class UserSerializer(serializers.ModelSerializer):
    note = serializers.PrimaryKeyRelatedField(many=True, queryset=Note.objects.all())
    class Meta:
        model = User
        fields = ('id', 'username', 'note')


class NoteSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Note
        fields = ("title", "content", "owner")