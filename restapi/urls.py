from django.conf.urls.defaults import patterns, url, include
from rest_framework import routers

from restapi import views


router = routers.DefaultRouter()
router.register(r'projects', views.ProjectViewSet)
# router.register(r'tasks', TaskViewSet)


urlpatterns = patterns(
    '',

    url('^', include(router.urls)),
    url(r'^projects/(?P<project_pk>\d+)/tasks/$', views.TaskByProjectList.as_view()),
)
