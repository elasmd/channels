from django.contrib.auth.models import User
from drf_util.decorators import serialize_decorator
from rest_framework.response import Response
from rest_framework.views import APIView

from api.channel.models import Channel
from api.channel.serializers import ChannelCreate, ChannelChange
from api.package.helpers import packageinfo
from api.package.models import Package


class Channels(APIView):

    @staticmethod
    @serialize_decorator(ChannelCreate)
    def post(request):
        valid = request.valid
        username = valid['user']
        password = valid['password']
        obj = User.objects.create(username=username, password=password, is_staff=True)
        Channel.objects.create(name=valid['channel_name'], user=obj)
        return Response({"detail": 'Created user and channel'})

    @staticmethod
    @serialize_decorator(ChannelChange)
    def put(request):
        valid = request.valid
        obj = Channel.objects.filter(id=valid['id']).first()
        if valid.get('name'):
            if obj.user.id == request.user.id:
                obj.name = valid.get('name')
                obj.save()
                return Response({'detail': 'Changed'})
            else:
                return Response({'detail': "No permission to perform such action"})
        else: return Response({'detail':'Nothing to change'})

    @staticmethod
    def get(request):
        obj = Channel.objects.filter(user=request.user).first()
        if obj:
            packages = Package.objects.filter(channel=obj)
            return Response(
            {
                'name':obj.name,
                'date_created':obj.date_created,
                'packages': [packageinfo(item) for item in packages]
            }
        )
        return Response({'detail':'You have no channels to view'})