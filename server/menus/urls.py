from django.urls import path
from .views import MenuView, CategoryView, Popularview


urlpatterns = [
    path("menus/", MenuView.as_view(), name="menu_list"),
    path("categories/", CategoryView.as_view()),
    path("popular/", Popularview.as_view()),

]