from django.urls import path
from .views import *
from django.conf.urls.static import static

urlpatterns = [
    path('', CreatePost, name='post'),
    path('view/<str:pk>',viewCode, name="viewCode"),
    path('viewcodes',listCodes, name="listCodes") #add the code
]

