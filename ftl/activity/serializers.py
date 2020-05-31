from rest_framework import serializers
from .models import Member, ActivityPeriod


class ActivitySerializer(serializers.Serializer):
    start_time = serializers.DateTimeField()
    end_time = serializers.DateTimeField()

    class Meta:
        fields = ('start_time', 'end_time')


class MemberActivityListSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='hash_id')
    tz = serializers.CharField(source='get_tz_display')
    activity_periods = ActivitySerializer(many=True)

    class Meta:
        model = Member
        fields = ('id', 'real_name', 'tz', 'activity_periods')
