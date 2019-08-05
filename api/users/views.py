from django.core.paginator import Paginator
from django.utils import timezone

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from drf_util.decorators import serialize_decorator
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from api.channel.models import Channel
from api.package.helpers import packageinfo
from api.package.models import Package
from api.users.models import Subscriptions
from api.users.serializers import SubscriptionAdd, SubscriptionId, PaginationSerializer


class UserSub(APIView):

    @staticmethod
    @serialize_decorator(SubscriptionAdd)
    def post(request):
        valid = request.valid
        obj = Package.objects.filter(id=valid['package']).first()
        if obj:
            Subscriptions.objects.create(package=obj,user=request.user)
            return Response({'detail':'Cretead'})
        return Response({'detail':'Nothing Created'})

    @staticmethod
    @serialize_decorator(SubscriptionId)
    def delete(request):
        valid = request.valid
        obj = Subscriptions.objects.filter(id=valid['id']).first()
        if obj and obj.active:
            today = timezone.now()
            time_passed =today-obj.date_subbed
            money_back = obj.package.price * ((time_passed.days/30)+1) *0.2
            obj.active=False
            obj.save()
            return Response({'money': money_back})
        return Response({'detail':'No such subscription or inactive'})

    @staticmethod
    def get(request):
        obj = Subscriptions.objects.filter(user=request.user)
        return Response({'data':[packageinfo(item.package) for item in obj]})

class AllChannels(APIView):

    @staticmethod
    @serialize_decorator(PaginationSerializer)
    def get(request):
        valid = request.valid
        obj = Channel.objects.all()
        response = []
        for items in obj:
            response.append({
                'name': items.name,
                'date_created': items.date_created,
                'packages': [packageinfo(item) for item in Package.objects.filter(channel=items)]
            })
        page = Paginator(response,valid['per_page'])
        return Response({
            "data":page.page(valid['page']).object_list,
            "pages":page.num_pages,
            "total":page.count
        })

@csrf_exempt
@require_POST
def authenticate(request):
    """
       @api {post} /api/auth Api login
       @apiName Login
       @apiGroup Authentication
        @apiParamExample {json} Request-Example: filters
                {
                  "username": "Username",
                  "password": "Password"
                }
        @apiParam {String} username  Username
        @apiParam {String} password Password
        @apiUse BAD_REQUEST
        @apiSampleRequest /api/auth
    """
    response = obtain_auth_token(request)

    if response.status_code != 200:
        return response
    else: return Response({"detail":'Failed'},status=400)


"""
  @api {post} /api/auth/reset Reset password
  @apiName Reset password
  @apiGroup Authentication
   @apiParamExample {json} Request-Example: filters
           {
             "email": "Email address"
           }
   @apiParam {String} email  Email address
   @apiUse BAD_REQUEST
   @apiSampleRequest /api/auth/reset
"""

"""
  @api {post} /api/auth/reset/confirm Reset password confirm
  @apiName Reset password confirm
  @apiGroup Authentication
   @apiParamExample {json} Request-Example: filters
           {
             "uid": "Uid"
             "token": "Token"
             "new_password1": "New password"
             "new_password2": "Repeat new password"
           }
   @apiParam {String} uid  Uid
   @apiParam {String} token  Token
   @apiParam {String} new_password1  New password
   @apiParam {String} new_password2  Repeat new password
   @apiUse BAD_REQUEST
   @apiSampleRequest /api/auth/reset/confirm
"""


@api_view(['GET'])
def logout(request):
    """
      @api {post} /api/logout Logout
      @apiName Logout
      @apiHeader Authorization Basic Access Authentication token.
      @apiGroup Authentication
      @apiUse BAD_REQUEST
      @apiSampleRequest /api/logout
    """
    request.user.auth_token.delete()
    return Response(status=200)

