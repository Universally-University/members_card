from rest_framework import viewsets
from rest_framework import permissions
from api.serializers import MemberCardSerializer
from api.models import MemberCard


class MemberCardViewSet(viewsets.ModelViewSet):
    queryset = MemberCard.objects.all().order_by("-card_num")
    serializer_class = MemberCardSerializer
    # permission_classes = [permissions.AllowAny]
    search_fields = ["=user_id"]
    filterset_fields = ["user_id"]
