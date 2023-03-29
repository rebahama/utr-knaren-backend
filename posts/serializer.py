from rest_framework import serializers
from . models import Post


class PostSerializer(serializers.ModelSerializer):
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        """ How to check for profile ownership"""
        request = self.context['request']
        return request.user == obj.owner



    class Meta:
        model = Post
        fields = '__all__'