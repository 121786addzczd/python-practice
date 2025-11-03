from rest_framework import serializers
from api.models import Item

def check_divide_by_ten(value):
    if value % 10 != 0:
        raise serializers.ValidationError('10で割り切れる値にしてください')

class ItemModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item 
        fields = '__all__'

    def validate_name(self, value): # nameに対するバリデーション
        if self.partial and value is None: # patchの場合はスキップ
            return value
        if value[0].islower():
            raise serializers.ValidationError('最初の文字は大文字にしてください')
        return value 

    def validate_price(self, value): # priceに対するバリデーション
        if self.partial and value is None: # patchの場合はスキップ
            return value
        # 1桁目が0以外を弾く(11, 101, 1108など)
        if value % 10 !=0:
            raise serializers.ValidationError('1桁目は0にしてください')
        return value 
    
    # 複数のデータにまたがっててのバリデーション
    def validate(self, data):
        price = data.get('price', self.instance.price if self.instance else None)
        discounted_price = data.get('discounted_price', self.instance.discounted_price if self.instance else None) 
        if discounted_price>= price:
            raise serializers.ValidationError('割引き価格は通常価格よりも低く設定してください')
        return data
    