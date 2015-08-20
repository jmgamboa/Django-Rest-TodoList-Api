from django.db import models

class TodoList(models.Model):
	owner = models.ForeignKey('auth.User', related_name='todolists')
	created = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=100, blank=True, default='')
	
	class Meta:
		unique_together = ("title", "owner")
		ordering = ['-created']

	def __unicode__(self):
		return self.title

class TodoItem(models.Model):
	owner = models.ForeignKey('auth.User', related_name='todoitems')
	list_name = models.ForeignKey(TodoList, related_name='todoitems')
	title = models.CharField(max_length=100, blank=True, default='')
	created = models.DateTimeField(auto_now_add=True)
	done = models.BooleanField(default=False)
	trash = models.BooleanField(default=False)

	class Meta:
		unique_together = ("title", "list_name")
		ordering = ['-created']

	def __unicode__(self):
		return self.title
