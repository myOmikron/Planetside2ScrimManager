from django.urls import path
from dashboard.views import *


urlpatterns = [
    path('', IndexView.as_view()),
]
