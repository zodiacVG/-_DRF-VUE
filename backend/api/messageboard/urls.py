from django.urls import path,include
from . import views
from rest_framework import routers

router=routers.DefaultRouter()
router.register('notes',views.NoteView)
router.register('updownvote',views.updowmvote,basename='')
urlpatterns = [
    path('',include(router.urls))
]