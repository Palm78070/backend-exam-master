from rest_framework import serializers

from .models import School, Classroom, Teacher, Student
# code here

class SchoolSerializer(serializers.ModelSerializer):
	#source specifies where the serializer should look to retrieve data for the field
	# classrooms_count = serializers.IntegerField(source='classrooms.count', read_only=True) #classrooms is the related name in the School model .count() method from Django ORM
	# teachers_count = serializers.IntegerField(source='classrooms__teachers.count', read_only=True)
	# students_count = serializers.IntegerField(source='classrooms__students.count', read_only=True)

	classrooms_count = serializers.SerializerMethodField()
	teachers_count = serializers.SerializerMethodField()
	students_count = serializers.SerializerMethodField()

	class Meta:
		#model and fields that we want to serialize
		model = School
		fields = '__all__'

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
	school_name = serializers.CharField(write_only=True) # Add the school_name field for input
	school = serializers.SerializerMethodField()

	class Meta:
		model = Classroom
		fields = ['year', 'room_number', 'school_name', 'school', 'teachers', 'students']
		# fields = '__all__'

	def create(self, validated_data):
		school_name = validated_data.pop('school_name') ## Get the school name from the validated data
		school = School.objects.get(name=school_name)
		if Classroom.objects.filter(year=validated_data['year'], room_number=validated_data['room_number'], school=school).exists():
			raise serializers.ValidationError('Classroom already exists')
		classroom = Classroom.objects.create(school=school, **validated_data)
		return classroom

	def get_school(self, obj):
		return obj.school.name

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
