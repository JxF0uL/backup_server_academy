from . import views
from django.contrib import admin
from django.urls import path, include
from App_dashboardGeral import views  # ✅ Import this

urlpatterns = [
    path('admin/', admin.site.urls),
    path('streamlit/', views.start_streamlit, name='start_streamlit'),
    
]

