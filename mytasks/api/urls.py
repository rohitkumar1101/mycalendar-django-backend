from django.urls import path

from .views import (MyTasksListView, MyTasksDetailView, 
				MyTasksCreateView, MyTasksDeleteView, MyTasksUpdateView)

urlpatterns = [
	path('', MyTasksListView.as_view()),
	path('create/', MyTasksCreateView.as_view()),
	path('<pk>/', MyTasksDetailView.as_view()),
	path('<pk>/update/', MyTasksUpdateView.as_view()),
	path('<pk>/delete/', MyTasksDeleteView.as_view()),
]