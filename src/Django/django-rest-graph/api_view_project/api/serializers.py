from rest_framework import serializers

class ItemsSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    price = serializers.IntegerField(min_value=0)
    