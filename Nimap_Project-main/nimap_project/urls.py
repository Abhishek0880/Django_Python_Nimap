from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from api import views
from client.views import ClientList,ClientDetail,ProjectList,ProjectDetail
from api.views import ClientViewSet,ProjectViewSet
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'client', ClientViewSet)
router.register(r'project',ProjectViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(('client.urls', 'client'), namespace="api")),
]
