from rest_framework import serializers

from shops.models import Shop, Visit
from users.models import User


class AddUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('name', 'phone')


class UserShopSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('phone', )


class AddShopSerializer(serializers.ModelSerializer):
    phone = serializers.CharField()

    class Meta:
        model = Shop
        fields = ('name', 'phone')


class ListShopSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shop
        fields = ('pk', 'name')


class VisitShopRequestSerializer(serializers.ModelSerializer):
    shop = serializers.PrimaryKeyRelatedField(read_only=True)
    phone = serializers.CharField()

    class Meta:
        model = Visit
        fields = ('shop', 'longitude', 'latitude', 'phone')


class VisitShopResponseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Visit
        fields = ('pk', 'date')
