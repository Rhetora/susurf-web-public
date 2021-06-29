from django.db import models

class blog(models.Model):
    title = models.TextField()
    date = models.DateField(auto_now_add=True)
    author = models.CharField(max_length=50)

    text1 = models.TextField()
    pic1 = models.ImageField(upload_to="blog/", null=True, blank=True)
    text2 = models.TextField(blank=True)
    pic2 = models.ImageField(upload_to="blog/", null=True, blank=True)
    text3 = models.TextField(blank=True)
    pic3 = models.ImageField(upload_to="blog/", null=True, blank=True)
    text4 = models.TextField(blank=True)
    pic4 = models.ImageField(upload_to="blog/", null=True, blank=True)
    text5 = models.TextField(blank=True)
    pic5 = models.ImageField(upload_to="blog/", null=True, blank=True)

    def __str__(self):
        return self.title
