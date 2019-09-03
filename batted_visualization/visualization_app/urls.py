from django.urls import path
from . import views

app_name= 'visualization_app'

urlpatterns=[
    path('batter/<id>',views.batter_info,name='batterinfo'),
    path('pitcher/<id>',views.pitcher_info,name='pitcherinfo'),
]