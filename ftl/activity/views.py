from django.shortcuts import render
from rest_framework import generics, response

from .models import Member
from .serializers import MemberActivityListSerializer


class MemberActivityList(generics.ListAPIView):
    '''
    Activity list of all members
    '''
    serializer_class = MemberActivityListSerializer

    def list(self, request):
        queryset = Member.objects.all()
        serializer = self.get_serializer(queryset, many=True)

        response_list = serializer.data
        custom_dict = {
            "ok": True,
            "members": response_list,
        }
        return response.Response(data=custom_dict)
