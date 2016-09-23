from rest_framework import serializers
from .models import *

class CampusSerializer(serializers.ModelSerializer):
	class Meta:
		model = campus_select
		fields = (
			'campus',
			)

class BranchSerializer(serializers.ModelSerializer):
	class Meta:
		model = branch_select
		fields = (
			'branch',
			)

class AlumnusSerializer(serializers.ModelSerializer):
	class Meta:
		model = Alumnus
		fields = (
			'enrollment_no',
			'name',
			'gender',
			'dob',
			'contactno',
			'image',
			'fblink',
			'linkedin',
			'email',
			'branch',
			'batch',
			)

class AnswerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Answer
		fields = (
			'answer',
			)
		
class SuggestSerializer(serializers.ModelSerializer):
	class Meta:
		model = Suggest
		fields=(
			'sname',
			'semail',
			'smessage',
			)

class ChangeSerializer(serializers.ModelSerializer):
	class Meta:
		fields=(
			'cname',
			'cbatch',
			'cemail',
			'ccontact',
			'cdetail',
		)