from django.urls import path
from .views import IndexView

app_name = 'helloworld'  # Важно для reverse-имен!

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]