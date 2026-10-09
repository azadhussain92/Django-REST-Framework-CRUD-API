from rest_framework import serializers
from Statusapp.models import status,userdata

class UserDataSerializer(serializers.ModelSerializer):
    class Meta :
        model = userdata
        fields = "__all__"
        
class StatusSerializer(serializers.ModelSerializer):
    user = UserDataSerializer(read_only=True)
    class Meta:
        model = status
        fields = "__all__"
