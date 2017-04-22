from django.contrib.auth.models import User, Group
from .models import Todo
from rest_framework import serializers


class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Todo
        # fields = ('tid', 'todo','user', 'flag','priority','pubtime','lastdate')
        fields = ('tid', 'todo', 'flag','priority','pubtime','lastdate')

class UserSerializer(serializers.ModelSerializer ):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')




