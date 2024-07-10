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

class ClassroomSerializer(serializers.ModelSerializer):
	#StringRelatedField is typically used when you want to represent a related model instance as a string (usually the __str__ representation of the related object).
	#many=True => there can be multiple related instances
	teachers = serializers.StringRelatedField(many=True, read_only=True)
	students = serializers.StringRelatedField(many=True, read_only=True)

	class Meta:
		model = Classroom
		fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):
	clossrooms = serializers.StringRelatedField(many=True, read_only=True)

	class Meta:
		model = Teacher
		fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
	classroom = serializers.StringRelatedField(read_only=True)

	class Meta:
		model = Student
		fields = '__all__'
