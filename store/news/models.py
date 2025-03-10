from django.db import models

class Articles(models.Model):
    title = models.CharField('Title',max_length=50)
    anons = models.CharField('Anons',max_length=150)
    full_text = models.TextField('Full content')
    date = models.DateTimeField('Date of publication')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f'/news/{self.id}'
    
    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'