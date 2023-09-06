from django.db import models

genres=(
    ('horror','HORROR'),
    ('drama','DRAMA'),
    ('fantasy','FANTASY'),
    ('action','ACTION'),
    ('science fiction','SCIENCE FICTION'),
    ('drama','DRAMA'),
    ('thriller','THRILLER'),
    ('western','WESTERN'),
    ('comedy','COMEDY'),
    ('educational','EDUCATIONAL'))

class Film(models.Model):
    caption=models.CharField(max_length=255)
    movie=models.FileField(upload_to='movies/%y')
    length=models.IntegerField()
    genre=models.CharField(max_length=20,choices=genres)
    description=models.TextField(max_length=255)
    def __str__(self):
        return self.caption[:90]
    
