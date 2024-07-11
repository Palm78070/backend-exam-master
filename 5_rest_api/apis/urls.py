from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.v1.classroom import ClassroomViewSet
from .views.v1.teacher import TeacherViewSet
from .views.v1.student import StudentViewSet
from .views.v1.school import SchoolViewSet


router = DefaultRouter() #automatically generate URL patterns for your viewsets
router.register(r'classrooms', ClassroomViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'students', StudentViewSet)
router.register(r'schools', SchoolViewSet)

api_v1_urls = (router.urls, 'v1') #router.urls returns the list of URL patterns generated by the router. The second element of the tuple is the namespace of the URL patterns.

urlpatterns = [
    # path('v1/', include(api_v1_urls))
    path('', include(api_v1_urls))
]
