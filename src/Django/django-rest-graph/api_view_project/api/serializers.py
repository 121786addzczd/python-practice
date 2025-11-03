from rest_framework import serializers
from .models import Item

def check_divide_by_ten(value):
    if value % 10 != 0:
        raise serializers.ValidationError('10で割り切れる値にしてください')

class ItemsSerializer(serializers.Serializer):
    pk = serializers.ReadOnlyField()
    name = serializers.CharField(max_length=20)
    price = serializers.IntegerField(min_value=0)
    discounted_price = serializers.IntegerField(min_value=0, validators=[check_divide_by_ten,]) # 割引き価格

    def validate_name(self, value): # nameに対するバリデーション
        if self.partial and value is None: # patchの場合はスキップ
            return value
        print(f"name={value}")
        if value[0].islower():
            raise serializers.ValidationError('最初の文字は大文字にしてください')
        return value 

    def validate_price(self, value): # priceに対するバリデーション
        if self.partial and value is None: # patchの場合はスキップ
            return value
        print(f"price={value}")
        # 1桁目が0以外を弾く(11, 101, 1108など)
        if value % 10 !=0:
            raise serializers.ValidationError('1桁目は0にしてください')
        return value 
    
    # 複数のデータにまたがっててのバリデーション
    def validate(self, data):
        print(f"data: {data}")
        price = data.get('price', self.instance.price)
        discounted_price = data.get('discounted_price', self.instance.discounted_price) 
        if discounted_price>= price:
            raise serializers.ValidationError('割引き価格は通常価格よりも低く設定してください')
        return data
    
    def create(self, validated_data):
        print("create 実行")
        print(validated_data)
        return Item.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # print("update 実行")
        # print(instance)
        # print(validated_data)
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.discounted_price = validated_data.get('discounted_price', instance.discounted_price)
        instance.save()
        return instance
