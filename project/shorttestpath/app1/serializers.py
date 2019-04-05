from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers
from app1.models import Sales
class SalesSerializer(ModelSerializer):
	class Meta:
		model=Sales
		fields = ['customer',"description","products"]#"__all__"
	def validate_description(self,value):
		if not value.isalnum():
			raise serializers.ValidationError("exepcting alphanumeric")
		return value

'''
class SalesSerilizer(Serializer):
	pass
'''
