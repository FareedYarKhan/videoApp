from django.db import models
from django.db.models.fields import TextField
from django.db.models.fields.files import FileField, ImageField
from django.core.validators import FileExtensionValidator
from django.contrib.postgres.fields import JSONField

class video(models.Model):
    name=models.CharField(max_length=122)
    description=models.TextField()
    thumbnail=ImageField(upload_to='thumbnails/%y-%m-%d',default=None,blank=True,null=True,validators=[FileExtensionValidator(['jpg','jpeg','png','gif'] ) ])
    file=FileField(upload_to='videos/%y/%m/%d', validators=[FileExtensionValidator(['mp4','avi','flv','3gp','vob','wmv','m4p','mpg','mp2','mpeg','webm','mkv'] ) ] )

class processedFiles(models.Model):
	video=models.ForeignKey(video,on_delete=models.CASCADE)
	fileJson = TextField()