from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from ...models import School
from ...serializers import SchoolSerializer
from ...filters import SchoolFilter

class SchoolViewSet(viewsets.ModelViewSet):
	queryset = School.objects.all()
	serializer = SchoolSerializer
	filter_backends = [DjangoFilterBackend] #used to apply filtering to querysets based on URL parameters
	filterset_class = SchoolFilter


