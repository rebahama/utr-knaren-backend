from rest_framework import serializers
from . models import Post


class PostSerializer(serializers.ModelSerializer):
    is_owner = serializers.SerializerMethodField()
    name = serializers.ReadOnlyField(source='owner.username')
    calculate_name = serializers.ReadOnlyField(source='calculate.price')

    def get_is_owner(self, obj):
        """ How to check for profile ownership"""
        request = self.context['request']
        return request.user == obj.owner

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    class Meta:
        model = Post
        fields = '__all__'