from django.urls import path


from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('<pk>', views.RoomDetailView.as_view(), name="room_detail"),


]

