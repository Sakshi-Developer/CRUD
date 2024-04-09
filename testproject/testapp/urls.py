from django.urls import path
from.import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('signup/',views.SignUp),
    path('login/',views.Login, name="login"),
    path('update/',views.update),
    path('delete/<int:id>', views.deleteData),
    path('edit/<int:id>', views.edit),
    path('logout/', views.logoutuser),



    
]+ static(settings.MEDIA_URL, 
          document_root=settings.MEDIA_ROOT)