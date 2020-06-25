from rest_framework import serializers

from mytasks.models import MyTasks

class MyTasksSerializers(serializers.ModelSerializer):
	class Meta:
		model = MyTasks
		fields = ('task_id','task_content', 'date_created', 'task_due_date')