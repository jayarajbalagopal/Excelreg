from django.db import models


class venue(models.Model):
  
    class Meta:
        verbose_name = "venue"
        verbose_name_plural = "venues"

    FIELD1_CHOICES = ['201', '202', '301' ,'302']

    venue_id=models.CharField(max_length=3,primary_key=True,null=False,choices=[(item,item) for item in FIELD1_CHOICES])
    occupied=models.BooleanField(default=False)
    vm_1=models.CharField(max_length=100,null=False)
    vm_2=models.CharField(max_length=100,null=False)
    vm_num_1=models.CharField(max_length=10,null=True)
    vm_num_2=models.CharField(max_length=10,null=True)
    current_event=models.CharField(max_length=6,default='Nil')
    next_event=models.CharField(max_length=6)

    def __str__(self):
        return (self.venue_id)


class event(models.Model):
  
    class Meta:
        verbose_name = "event"
        verbose_name_plural = "events"

    FIELD1_CHOICES = ['201', '202', '301' ,'302']

    event_id=models.CharField(max_length=6,primary_key=True)
    event_name=models.CharField(max_length=100,null=False,default="Nil")
    venue_id=models.CharField(max_length=3,null=False,choices=[(item,item) for item in FIELD1_CHOICES])
    em_1=models.CharField(max_length=100,null=False)
    em_2=models.CharField(max_length=100,null=False)
    em_num_1=models.CharField(max_length=10,null=True)
    em_num_2=models.CharField(max_length=10,null=True)
    day=models.DateField(null=False)
    time=models.TimeField(null=False)
    status=models.IntegerField(null=False,default=0)
    winner1=models.CharField(max_length=10,default='nil')
    winner2=models.CharField(max_length=10,default='nil')
    winner3=models.CharField(max_length=10,default='nil')

    def __str__(self):
        return (self.event_id)

