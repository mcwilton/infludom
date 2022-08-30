from rest_framework import serializers
from .models import Talent


class TalentRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Talent
        fields = ['bio', 'phone_number', 'gender']

    def get_cleaned_data(self):
        data = super(TalentRegistrationSerializer, self).get_cleaned_data()
        extra_data = {
            'bio': self.validated_data.get('bio', ''),
        }
        data.update(extra_data)
        return data

    def save(self, request):
        user = super(TalentRegistrationSerializer, self).save(request)
        user.is_talent = True
        user.save()
        talent = Talent(talent=user, bio=self.cleaned_data.get('bio'))
        talent.save()
        return user


# class TalentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Talent
#         fields = '__all__'




