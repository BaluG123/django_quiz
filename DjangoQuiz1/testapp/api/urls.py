from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()

router.register('sixapi',views.Six_View,basename="six")
router.register('sevenapi',views.Seven_View,basename="seven")
router.register('eightapi',views.Eight_View,basename="eight")
router.register('nineapi',views.Nine_View,basename="nine")
router.register('tenapi',views.Ten_View,basename="ten")
router.register('Currentapi',views.Current_View,basename="current")
router.register('generalapi',views.General_View,basename="general")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls))    
]
