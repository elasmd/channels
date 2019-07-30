from drf_util.decorators import serialize_decorator
from rest_framework.response import Response
from rest_framework.views import APIView

from api.package.models import Package
from api.program.models import Program
from api.program.serializers import ProgramCreate, ProgramEdit, ProgramId
from api.program.permissions import IsSuperUser


class Programs(APIView):
    permission_classes = IsSuperUser,

    @staticmethod
    @serialize_decorator(ProgramCreate)
    def post(request):
        valid = request.valid
        Program.objects.create(name=valid['name'])
        return Response({'detail': 'Created'})

    @staticmethod
    @serialize_decorator(ProgramEdit)
    def put(request):
        valid = request.valid
        obj = Program.objects.filter(id=valid['id'])
        if valid.get('name') or valid.get('package'):
            if valid.get('name'):
                obj.update(name=valid.get('name'))
            if valid.get('package'):
                package = Package.objects.filter(id=valid.get('package')).first()
                obj.first().package.add(package)
            return Response({'detail':'Changed'})
        return Response({'detail':'No changes'})

    @staticmethod
    @serialize_decorator(ProgramId)
    def delete(request):
        valid = request.valid
        Program.objects.filter(id=valid['id']).delete()
        return Response({'detail':'Deleted'})

    @staticmethod
    @serialize_decorator(ProgramId)
    def get(request):
        valid = request.valid
        obj = Program.objects.filter(id=valid['id']).first()
        if obj:
            return Response({
            'name': obj.name,
            'date_created': obj.date_created
        })
        else: return Response({"detail":'No such object'})
