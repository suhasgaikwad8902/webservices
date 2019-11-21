from rest_framework.routers import SimpleRouter
from .views import OwnViewSet

routerInstance = SimpleRouter()
routerInstance.register('student',OwnViewSet)

urlpatterns = routerInstance.urls