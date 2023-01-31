



from django.urls import path,include

from django.conf.urls.static import static
from planetapp import views


urlpatterns = [
 
    path('display/',views.display),
   
    path('features/',views.features),
    path('addUser/',views.addUser,name='add-user'),
   

]


