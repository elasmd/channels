from rest_framework import serializers

class ProgramCreate(serializers.Serializer):
    name = serializers.CharField(max_length=100)

class ProgramEdit(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100,required=False)
    package = serializers.IntegerField(required=False)

class ProgramId(serializers.Serializer):
    id = serializers.IntegerField()