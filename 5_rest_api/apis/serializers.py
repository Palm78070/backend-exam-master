from rest_framework import serializers

from .models import School, Classroom, Teacher, Student
# code here

class SchoolSerializer(serializers.ModelSerializer):
	#source specifies where the serializer should look to retrieve data for the field
	classroom_count = serializers.IntegerField(source='classrooms.count', read_only=True) #classrooms is the related name in the School model .count() method from Django ORM
	teacher_count = serializers.IntegerField(source='classrooms__teachers.count', read_only=True)
	student_count = serializers.IntegerField(source='classrooms__students.count', read_only=True)

	class Meta:
		#model and fields that we want to serialize
		model = School
		fields = '__all__'
