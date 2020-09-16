from django.db import models


class homemsg(models.Model):
    homemessage = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.homemessage

class apps(models.Model):
    name = models.CharField(max_length=200)
    Domain = models.CharField(max_length=200)
    Image = models.ImageField(null=True, blank=True, upload_to="images")

    def __str__(self):
        return self.name

class aboutus(models.Model):
    aboutus = models.CharField(max_length=200)

    def __str__(self):
        return self.aboutus

class posts(models.Model):
    title = models.CharField(null=True, blank=True,max_length=200)
    Image = models.ImageField(null=True, blank=True, upload_to="postimages")
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
