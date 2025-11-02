from rest_framework import serializers

class ItemsSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    price = serializers.IntegerField(min_value=0)
    discounted_price = serializers.IntegerField(min_value=0) # 割引き価格

    def validate_name(self, value): # nameに対するバリデーション
        print(f"name={value}")
        if value[0].islower():
            raise serializers.ValidationError('最初の文字は大文字にしてください')
        return value 

    def validate_price(self, value): # priceに対するバリデーション
        print(f"price={value}")
        # 1桁目が0以外を弾く(11, 101, 1108など)
        if value % 10 !=0:
            raise serializers.ValidationError('1桁目は0にしてください')
        return value 
    
    # 複数のデータにまたがっててのバリデーション
    def validate(self, data):
        print(f"data: {data}")
        price = data.get('price')
        discounted_price = data.get('discounted_price') 
        if discounted_price>= price:
            raise serializers.ValidationError('割引き価格は通常価格よりも低く設定してください')
        return data