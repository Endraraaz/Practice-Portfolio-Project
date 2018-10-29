from django.db import models

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to='images/')
    summary=models.TextField()
    pub_date=models.DateTimeField()

    def body(self):
        return self.summary[:50]

    def __str__(self):
        return self.title


    
