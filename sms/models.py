from django.db import models

# Create your models here.

class Order(models.Model):
    phone = models.CharField(max_length=255, default='')
    data = models.JSONField()
    def handleInput(self, sInput):
        # self.data["state"] starts out as WELCOMING
        aReturn = []
        return aReturn
    def isDone(self):
        if self.data["state"] == "DONE":
            return True
        else:
            return False
    class Meta:
       indexes = [models.Index(fields=['phone'])]