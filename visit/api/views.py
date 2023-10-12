from datetime import datetime

from django.utils import timezone
from rest_framework import generics
from rest_framework.response import Response

from .serializers import (
    AddUserSerializer,
    UserShopSerializer,
    AddShopSerializer,
    ListShopSerializer,
    VisitShopRequestSerializer,
    VisitShopResponseSerializer,
)
from shops.models import Shop, Visit
from users.models import User


class AddUserAPIView(generics.CreateAPIView):
    serializer_class = AddUserSerializer

    def post(self, request):
        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class AddShopAPIView(generics.CreateAPIView):
    serializer_class = AddShopSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.filter(phone=serializer.data['phone']).first()
        if not user:
            return Response("Employee's phone not found")
        shop = Shop.objects.filter(
            name=serializer.data['name'], employee=user
        ).first()
        if shop:
            return Response('Employee is already working in shop')
        Shop.objects.create(name=serializer.data['name'], employee=user)
        return Response(serializer.data)


class EmployeeShopsAPIView(generics.CreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = UserShopSerializer

    def post(self, request):
        user = User.objects.filter(phone=request.data['phone']).first()
        if not user:
            return Response('Employee not found')
        queryset = self.get_queryset().filter(employee=user)
        serializer = ListShopSerializer(instance=queryset, many=True)
        return Response(serializer.data)


class VisitShopAPIView(generics.CreateAPIView):
    serializer_class = VisitShopRequestSerializer

    def post(self, request):
        shop = Shop.objects.filter(pk=request.data['shop'])
        if not shop.first():
            return Response('Shop not found')
        shop = shop.filter(
            employee__phone=request.data['phone']
        ).first()
        if not shop:
            return Response('Employee not found in shop')
        date = datetime.now()
        tz = timezone.get_current_timezone()
        timzone_datetime = timezone.make_aware(date, tz, True)
        visit = Visit.objects.create(
            date=timzone_datetime,
            shop=shop,
            latitude=request.data['latitude'],
            longitude=request.data['longitude']
        )
        serializer = VisitShopResponseSerializer(instance=visit)
        return Response(serializer.data)
