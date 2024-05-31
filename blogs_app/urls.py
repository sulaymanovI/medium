
from rest_framework import routers
from .views import BlogViewSet

router=routers.SimpleRouter()
router.register(r'blog' , BlogViewSet)

urlpatterns = [
    
] + router.urls