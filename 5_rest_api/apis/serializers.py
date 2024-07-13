from rest_framework import serializers

from .models import School, Classroom, Teacher, Student
# code here

# class SchoolField(serializers.RelatedField):
class SchoolSerializer(serializers.ModelSerializer):
	classrooms_count = serializers.SerializerMethodField()
	teachers_count = serializers.SerializerMethodField()
	students_count = serializers.SerializerMethodField()

	class Meta:
		#model and fields that we want to serialize
		model = School
		fields = '__all__'

	def validate(self, data):
		if School.objects.filter(name=data['name']).exists():
			raise serializers.ValidationError('School already exists!')
		return data

	def get_classrooms_count(self, obj):
		return obj.classrooms.count()
	def get_teachers_count(self, obj):
		return Teacher.objects.filter(classrooms__school=obj).distinct().count() #This method use a query to count distinct Teacher obj relate to School => Teacher is get from Classroom that related to School
	def get_students_count(self, obj):
		return Student.objects.filter(classroom__school=obj).distinct().count() #This method use a query to count distinct Student obj relate to School => Student is get from Classroom that related to School

class ClassroomSerializer(serializers.ModelSerializer):
	#StringRelatedField is typically used when you want to represent a related model instance as a string (usually the __str__ representation of the related object).
	#many=True => there can be multiple related instances
	teachers = serializers.StringRelatedField(many=True, read_only=True)
	students = serializers.StringRelatedField(many=True, read_only=True)
	# school_id = serializers.PrimaryKeyRelatedField(queryset=School.objects.all(), source='school')
	# school_name = serializers.CharField(write_only=True) # Add the school_name field for input
	# school = serializers.SerializerMethodField()
	school = serializers.SlugRelatedField(slug_field='name', queryset=School.objects.all())

	class Meta:
		model = Classroom
		fields = ['id', 'year', 'room_number', 'school', 'teachers', 'students']
		# fields = '__all__'

	def validate(self, data):
		#school__name have 2 underscore because school field is ForeignKey in Classroom model => __ use to traverse to school model and check name field
		# if Classroom.objects.filter(year=data['year'], room_number=data['room_number'], school__name=data['school_name']).exists():
		if Classroom.objects.filter(year=data['year'], room_number=data['room_number'], school=data['school']).exists():
			raise serializers.ValidationError('Classroom already exists!')
		return data

	# def create(self, validated_data):
	# 	school_name = validated_data.pop('school_name') ## Get the school name from the validated data
	# 	school = School.objects.get(name=school_name)
	# 	# if Classroom.objects.filter(year=validated_data['year'], room_number=validated_data['room_number'], school=school).exists():
	# 	# 	raise serializers.ValidationError('Classroom already exists!')
	# 	classroom = Classroom.objects.create(school=school, **validated_data)
	# 	return classroom

	# def get_school(self, obj):
	# 	return obj.school.name

class TeacherSerializer(serializers.ModelSerializer):
	clossrooms = serializers.StringRelatedField(many=True, read_only=True)

	class Meta:
		model = Teacher
		fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
	# classroom = serializers.StringRelatedField(read_only=True)
	classroom = serializers.PrimaryKeyRelatedField(queryset=Classroom.objects.all())

	class Meta:
		model = Student
		fields = '__all__'
