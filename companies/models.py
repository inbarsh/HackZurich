from django.db import models


#class NewsItem(models.Model):
#    title = models.CharField(max_length=100)

#    def __str__(self):
#        return self.title


class Company(models.Model):
    name = models.CharField(max_length=255)
    score = models.FloatField(max_length=10, default=None)
    graph_image = models.ImageField(upload_to='images/', default='pic_folder/None/no-img.jpg')
    words_frequency_image = models.ImageField(upload_to='images/', default='pic_folder/None/no-img.jpg')
    #image = models.CharField(max_length=255, default=None)
    #news = models.ManyToManyField(NewsItem)
    #news = models.CharField(max_length=255, default=None)

    class Meta:
        verbose_name_plural = "companies"

    def __str__(self):
        return self.name
