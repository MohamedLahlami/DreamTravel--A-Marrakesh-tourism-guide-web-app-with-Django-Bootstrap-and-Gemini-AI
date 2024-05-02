from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("register/", views.register_user, name="register"),
    path("chatbot/<str:query>", views.chatbot , name="chatbot"),
    path("chatbot/", views.chatbot , name="chatbot"),
    path("attractions/", views.attractions, name="attractions"),
    path("restaurants/", views.restaurants, name="restaurants"),
    path("hotels/", views.hotels, name="hotels"),
    path("attractions/<int:id>", views.attractionDetail, name="attractionDetail"),
    path("hotels/<int:id>", views.hotelDetail, name="hotelDetail"),
    path("restaurants/<int:id>", views.restaurantDetail, name="restaurantDetail"),
]