from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from ...models import Classroom
from ...serializers import ClassroomSerializer
from ...filters import ClassroomFilter

class ClassroomViewSet(viewsets.ModelViewSet):
	queryset = Classroom.objects.all()
	serializer_class = ClassroomSerializer
	filter_backends = [DjangoFilterBackend]
	filterset_class = ClassroomFilter
