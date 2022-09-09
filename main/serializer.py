from rest_framework import serializers
from .models import Talent

  
class TalentSerializer(serializers.Serializer):
    bio = serializers.CharField(required =True)
    email = serializers.EmailField()
    gender = serializers.CharField(max_length=200)
    ethnicity = serializers.CharField(required=True)
    weight = serializers.FloatField()
    height = serializers.FloatField()
    age = serializers.CharField(max_length=2)
    ethnicity = serializers.CharField(required =True)
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
        instance.gender = validated_data.get('talent_gender', instance.gender)
        instance.ethnicity = validated_data.get('talent_ethnicity', instance.talent_ethnicity)
        instance.weight = validated_data.get('talent_weight', instance.weight)
        instance.height = validated_data.get('talent_height', instance.height)
        instance.save()
        return instance




