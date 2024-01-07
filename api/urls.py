from django.urls import path
from . import views


urlpatterns = [
    path("", views.student_list),
    path("student_list/", views.StudentCreate.as_view()),
    path("<int:pk>/", views.student_detail),
    path("add_student/", views.add_student),
    path("<int:pk>/update/", views.update_student),
    path("<int:pk>/delete/", views.delete_student),
]
