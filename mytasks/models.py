from django.db import models

class MyTasks(models.Model):
	task_content = models.CharField(max_length=200)
	date_created = models.DateField(auto_now=True)
	task_due_date = models.DateField()

	def __str__(self):
		return self.task_content