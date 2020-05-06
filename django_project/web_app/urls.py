from django.urls import path
from . import views
urlpatterns= [
    path('',views.apphome,name='app-home'),
    path('status/',views.status,name='status'),
    path('interns/',views.interns,name='interns'),
    path('appl/', views.appl, name='appl'),
]
