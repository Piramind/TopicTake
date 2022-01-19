from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['id', 'user_last_name', 'user_first_name', 'password']
		extra_kwargs = {
				'password': {'write-only': True}
		}

	def create(seld, validated_data):
		password = validated_data.pop('user_pwd', None)
		instance = self.Meta.model(**validated_data)
		if password is not None:
			instance.set_password(password)
		instance.save()
		return instance