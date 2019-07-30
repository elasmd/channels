from rest_framework import serializers

class ChannelCreate(serializers.Serializer):
    user = serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=100)
    channel_name = serializers.CharField(max_length=200)

class ChannelChange(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=200,required=False)