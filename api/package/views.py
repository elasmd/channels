from drf_util.decorators import serialize_decorator
from rest_framework.response import Response
from rest_framework.views import APIView

from api.channel.models import Channel
from api.package.helpers import packageinfo
from api.package.models import Package
from api.package.serializers import PackageCreate, PackageId, PackageUpdate


class Packages(APIView):

    @staticmethod
    @serialize_decorator(PackageCreate)
    def post(request):
        valid = request.valid
        obj = Channel.objects.filter(id=valid['channel']).first()
        if obj.user.id == request.user.id:
            Package.objects.create(name=valid['name'],channel=obj,price=valid['price'])
            return Response({'detail':'Created'})
        else: return Response({'detail':"No permission to perform such action"})

    @staticmethod
    @serialize_decorator(PackageId)
    def delete(request):
        valid = request.valid
        package = Package.objects.filter(id=valid['id']).first()
        obj = Channel.objects.filter(id=package.channel_id).first()
        if obj.user.id == request.user.id:
            package.delete()
            return Response({'detail': 'Deleted'})
        else:
            return Response({'detail': "No permission to perform such action"})

    @staticmethod
    @serialize_decorator(PackageUpdate)
    def put(request):
        valid = request.valid
        package = Package.objects.filter(id=valid['id'])
        if valid.get('name') or valid.get('price'):
            obj = Channel.objects.filter(id=package.first().channel_id).first()
            valid.pop('id')
            if obj.user.id == request.user.id:
                package.update(**valid)
                return Response({'detail':'Changed'})
            else: return Response({'detail':"No permission to perform such action"})
        else: return Response({'detail': 'Nothing to change'})

    @staticmethod
    @serialize_decorator(PackageId)
    def get(request):
        valid = request.valid
        package = Package.objects.filter(id=valid['id']).first()
        obj = Channel.objects.filter(id=package.channel_id).first()
        if obj.user.id == request.user.id:
            return Response(packageinfo(package))
        else: return Response({'detail': "No permission to perform such action"})
