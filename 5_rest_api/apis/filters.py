from django_filters import FilterSet, filters
from .models import School, Classroom, Teacher, Student


# code here
class SchoolFilter(FilterSet):
	class Meta:
		model = School
		fields = ['name']

class ClassroomFilter(FilterSet):
	class Meta:
		model = Classroom
		fields = ['school']

class TeacherFilter(FilterSet):
	class Meta:
		model = Teacher
		fields = ['classrooms__school', 'classrooms', 'first_name', 'last_name', 'gender']

class StudentFilter(FilterSet):
	class Meta:
		model = Student
		fields = ['classroom__school', 'classroom', 'first_name', 'last_name', 'gender']
