from django.shortcuts import render
from rest_framework import generics
from .serializers import MemberActivityListSerializer
from .models import Member


class MemberActivityList(generics.ListAPIView):
    '''
    Activity list of all members
    '''
    serializer_class = MemberActivityListSerializer
    queryset = Member.objects.all()
