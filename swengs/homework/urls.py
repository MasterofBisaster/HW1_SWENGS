from django.urls import path
from swengs.homework import views


urlpatterns = [
    path('oem/', views.oem_list),
    path('oem/<int:pk>', views.oem_detail),
]