from django.db import models
from django.db.models.constraints import UniqueConstraint

# Create your models here.
class School(models.Model):
	name = models.CharField(max_length=100)
	short_name = models.CharField(max_length=20)
	address = models.TextField()

	class Meta:
		constraints = [
			UniqueConstraint(fields=['name'], name='unique_school')
		]

	def __str__(self): #use to display name of the school object => print(str(school_instance)) name of the school
		return self.name

class Classroom(models.Model):
	year = models.IntegerField()
	room_number = models.IntegerField()
	school = models.ForeignKey(School, related_name='classrooms', on_delete=models.CASCADE)

	class Meta:
		constraints = [
			UniqueConstraint(fields=['year', 'room_number', 'school'], name='unique_classroom')
		]

	def __str__(self):
		return f"{self.year}/{self.room_number}"

class Teacher(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	gender = models.CharField(max_length=10)
	classrooms = models.ManyToManyField(Classroom, related_name='teachers')

	def __str__(self):
		return f"{self.first_name} {self.last_name}"

class Student(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	gender = models.CharField(max_length=10)
	classroom = models.ForeignKey(Classroom, related_name='students', on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.first_name} {self.last_name}"

