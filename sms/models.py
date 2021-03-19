from django.db import models

class Order(models.Model):
    # Model has 2 attributes. Phone and a dict called data.
    phone = models.CharField(max_length=255, default='')
    data = models.JSONField()

    def handleInput(self, sInput):
        # this is called for each turn
        # self.data["state"] starts out as WELCOMING
        aReturn = []
        return aReturn

    def isDone(self):
        # this is also called for each turn
        if self.data["state"] == "DONE":
            return True
        else:
            return False

    class Meta:
        # this sets up a SQL index on the phone field
        indexes = [models.Index(fields=['phone'])]
