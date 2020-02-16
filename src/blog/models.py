from django.db import models

# Create your models here.

class Blogpost(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    sub_category = models.CharField(max_length=50, default="")
    desc = models.CharField(max_length=1000)
    pub_date = models.DateField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to='blog/post/images', default="")
    # author = models.ForeignKey(User,default=None,on_delete = models.CASCADE)


    def __str__(self):
        return self.title
