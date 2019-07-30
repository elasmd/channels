from rest_framework import serializers

class SubscriptionAdd(serializers.Serializer):
    package = serializers.IntegerField()

class SubscriptionId(serializers.Serializer):
    id = serializers.IntegerField()