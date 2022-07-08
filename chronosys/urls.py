from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.CustomerPage, name="CustomerPage"),   
    path('Feedback/',views.Feedback, name="Feedback"),
    path('Summary/',views.Summary, name="Summary"),
    path('delete/<int:id>', views.delete, name='delete'),
    path('Delete1/<int:id>', views.Delete1, name='Delete1'),
    path('edit/<int:id>', views.edit, name='edit'),
]