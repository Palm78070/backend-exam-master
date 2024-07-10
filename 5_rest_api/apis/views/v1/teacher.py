from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from ...models import Teacher
from ...serializers import TeacherSerializer
from ...filters import TeacherFilter

class TeacherViewSet(viewsets.ModelViewSet):
	queryset = Teacher.objects.all()
	serializer_class = TeacherSerializer
	filter_backends = [DjangoFilterBackend]
	filterset_class = TeacherFilter
