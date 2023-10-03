from rest_framework import serializers
from api.models import MemberCard


class MemberCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberCard
        fields = "__all__"
