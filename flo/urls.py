from django.urls import path
from .views import test
app_name = 'flo'

urlpatterns = [
    path('test2/', test ),
]