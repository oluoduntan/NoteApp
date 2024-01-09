from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Note



class UserSerializer(serializers.HyperlinkedModelSerializer):
    # note = serializers.PrimaryKeyRelatedField(many=True, queryset=Note.objects.all())
    note = serializers.HyperlinkedRelatedField(many=True, view_name='note', read_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password', 'note')
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        #user.set_password(validated_data['password'])
        #user.save()
        return validated_data
    
    def validate_email(self, email):
        email_exists = User.objects.filter(email__iexact=email).exists()
        if email_exists:
            raise serializers.ValidationError("A user with that email already exists.")
        if not email:
            raise serializers.ValidationError("Enter a valid email address.")
        return email
    
    def validate_username(self, username):
        username_exists = User.objects.filter(username__iexact=username).exists()
        if username_exists:
            raise serializers.ValidationError("A user with that username already exists.")
        try:
            username.encode('ascii')
        except UnicodeEncodeError:
            raise serializers.ValidationError('Enter a valid username. This value may contain only english letters, numbers, and @/./+/-/_ characters.')
        return username


class NoteSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Note
        fields = ("title", "content", "owner")