from rest_framework import serializers
from ManApi.models import UserActivity, User


class ActivityPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('start_time', 'end_time')
        model = UserActivity


class TaskSerializer(serializers.ModelSerializer):
    activity_periods = ActivityPeriodSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = ('u_id',
                  'real_name',
                  'tz',
                  'activity_periods')
