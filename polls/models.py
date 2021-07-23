import datetime

from django.db import models
from django.utils import timezone


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
        
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'



class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text


class Testing(models.Model):
    char2 = models.CharField(max_length=2)
    char30 = models.CharField(max_length=30)
    auto_counter = models.AutoField(primary_key=True)
    bin_f = models.BinaryField()
    is_test = models.BooleanField()
    date = models.DateField()
    date_time = models.DateTimeField()
    time = models.TimeField()
    dec53 = models.DecimalField(max_digits = 5, decimal_places = 3)
    dec33 = models.DecimalField(max_digits = 3, decimal_places = 3)
    duration = models.DurationField()
    email = models.EmailField()
    file = models.FileField()
    floating = models.FloatField()
    img = models.ImageField() 
    json = models.JSONField()
    #n_bool = models.NullBooleanField()  ## deprecated
    n_bool2 = models.BooleanField(null = True)
    slug = models.SlugField()
    url_d = models.URLField()
    uuid = models.UUIDField()
    question = models.OneToOneField(Question, on_delete=models.CASCADE)
    choices = models.ManyToManyField(Choice)
