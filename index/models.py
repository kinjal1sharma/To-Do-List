from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)# to keep the data of the user if deleted then on_delete=models.SET_NULL
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    create = models.DateTimeField(auto_now_add=True) #automatically takes the screenshot when we create the item

    #String representation of the model(Set the default value to title )
    def __str__(self):
        return self.title

    # Default ordering , order the model by complete status, if the task is complete that will automatically go to the bottom of the list
    class Meta:
        ordering =['complete']

        #Super user : kinjal sharma, Vaidik123@