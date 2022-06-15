from django.urls import path
from . import views
app_name = "webapp"

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.login_request, name="login"),
    path('', views.homepage, name="homepage"),
    path("logout/", views.logout_request, name="logout"),
    path("feedback/",views.feedback_detail,name="feedback_detail"),
    path("question/<int:question_id>/", views.question_list,name="question"),
    path("question/<int:question_id>/submit/", views.question_submit, name="submit"),
    #127.0.0.1:8000/details/1/
    path("details/", views.question_detail, name="detail")
]