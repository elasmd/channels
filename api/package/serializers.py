from rest_framework import serializers

class PackageCreate(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    price = serializers.IntegerField()
    channel = serializers.IntegerField()

class PackageId(serializers.Serializer):
    id = serializers.IntegerField()

class PackageUpdate(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100,required=False)
    price = serializers.IntegerField(required=False)

