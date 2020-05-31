from rest_framework import serializers
from .models import Member


class MemberActivityListSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='hash_id')
    tz = serializers.DateTimeField(source='get_tz_display')

    class Meta:
        model = Member
        fields = ('id', 'real_name', 'tz')
