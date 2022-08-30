from rest_framework import serializers
from .models import Talent

  
class TalentSerializer(serializers.Serializer):
    bio = serializers.CharField(required =True)
    email = serializers.EmailField()
    talent_gender = serializers.CharField(max_length=200)
    talent_ethnicity = serializers.CharField(required=True)
    talent_weight = serializers.DecimalField(required=True, max_digits=4, decimal_places=2)
    talent_height = serializers.DecimalField(required=True,  max_digits=4, decimal_places=2)
    age = serializers.IntegerField(required =True)
    ethnicity = serializers.CharField(required =True)
    gender = serializers.CharField(required =True)
    phone_number = serializers.CharField(required =True)

    def validate_age(self, age):
        if age < (age-2) or age > (age+2):
            return False

    def create(self, validated_data):
        if self.validate_age() != False:
            return Talent.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.bio = validated_data.get('bio', instance.bio)
        instance.age = validated_data.get('age', instance.age)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.email = validated_data.get('email', instance.email)
        instance.talent_gender = validated_data.get('talent_gender', instance.talent_gender)
        instance.talent_ethnicity = validated_data.get('talent_ethnicity', instance.talent_ethnicity)
        instance.talent_weight = validated_data.get('talent_weight', instance.talent_weight)
        instance.talent_height = validated_data.get('talent_height', instance.talent_height)
        instance.save()
        return instance




