from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Note



class UserSerializer(serializers.HyperlinkedModelSerializer):
    # note = serializers.PrimaryKeyRelatedField(many=True, queryset=Note.objects.all())
    note = serializers.HyperlinkedRelatedField(many=True, view_name='note', read_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'note')


class NoteSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Note
        fields = ("title", "content", "owner")