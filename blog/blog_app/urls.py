from django.urls import path
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("", TemplateView.as_view(template_name="blog/home.html"), name="home"),
    path("createblog/", views.create_blog, name="create_blog"),
    path("blog/<int:id>/", views.blog, name="blog"),
    path("iframe/", views.iframe, name="iframe"),
    path("edit/<int:id>/", views.edit, name="edit"),
    path("delete/<int:id>/", views.delete, name="delete"),
]
