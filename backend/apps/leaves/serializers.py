from ast import Or
from apps.users.serializers import UserInfoSerializer
from .models import Leave
from ..users .models import User
from rest_framework import serializers

class LeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leave
        fields = '__all__'
class AddLeaveSerializer(serializers.ModelSerializer):
    class Meta:  
        model = Leave
        fields = [
            'user',
            'leave_type',
            'from_date',
            'to_date',
            'duration',
            'created_at',
            'updated_at',
            'description',
            'leave_status',
            'leave_balance',
        ]

    # def create(self, validated_data):
    #     request = self.context['request']
    #     data = validated_data 
    #     data['leave_status'] = 'applied' 


class LeaveUpdateSerializer(serializers.ModelSerializer): 
    class Meta:  
        model = Leave
        fields = [
            'user',
            'leave_type',
            'from_date',
            'to_date',
            'duration',
            'created_at',
            'updated_at',
            'description',
            'leave_status',
            'leave_balance',
        ]
        
class LeaveListSerializer(serializers.ModelSerializer):
    user = UserInfoSerializer()
    
    class Meta:
        model = Leave
        fields = [
            'user',
            'leave_type',
            'from_date',
            'to_date',
            'duration',
            'created_at',
            'updated_at',
            'description',
            'leave_status',
            'leave_balance',
        ]
   
class LeaveFindSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leave
        fields = '__all__'

