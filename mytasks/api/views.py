from rest_framework.generics import (ListAPIView, 
RetrieveAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView)
from rest_framework import viewsets

from mytasks.models import MyTasks
from .serializers import MyTasksSerializers

class MyTasksViewSet(viewsets.ModelViewSet):
	serializer_class = MyTasksSerializers
	queryset = MyTasks.objects.all()

class MyTasksListView(ListAPIView):
	queryset = MyTasks.objects.all()
	serializer_class = MyTasksSerializers

class MyTasksDetailView(RetrieveAPIView):
	queryset = MyTasks.objects.all()
	serializer_class = MyTasksSerializers

class MyTasksCreateView(CreateAPIView):
	queryset = MyTasks.objects.all()
	serializer_class = MyTasksSerializers

class MyTasksDeleteView(DestroyAPIView):
	queryset = MyTasks.objects.all()
	serializer_class = MyTasksSerializers

class MyTasksUpdateView(UpdateAPIView):
	queryset = MyTasks.objects.all()
	serializer_class = MyTasksSerializers