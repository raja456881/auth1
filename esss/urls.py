from django.urls import path
from.import views
urlpatterns = [
   path("home/", views.index, name="login"),
   path("sigup/", views.register, name="sigin"),
   path("login/", views.handlelogin, name="login"),
    path("sighand", views.handlesignup, name="sigin1"),
    path("logout", views.handlelogout, name="logout"),
    path("", views.home, name="home")

]
