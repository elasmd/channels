from rest_framework import serializers


class SubscriptionAdd(serializers.Serializer):
    package = serializers.IntegerField()


class SubscriptionId(serializers.Serializer):
    id = serializers.IntegerField()


class PaginationSerializer(serializers.Serializer):
    page = serializers.IntegerField(required=False, default=1)
    per_page = serializers.IntegerField(required=False, default=25, max_value=100)
    search = serializers.CharField(max_length=30, required=False, min_length=2)
