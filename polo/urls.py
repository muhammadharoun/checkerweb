from django.urls import path
from .views import test
app_name = 'polo'

urlpatterns = [
    path('test/', test ),
]