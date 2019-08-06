from django.db import models


# Create your models here.
class Timestamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class FileCategory(Timestamp):
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)

    def __str__(self):
        return '%s' % self.name


class FileUpload(Timestamp):
    name = models.CharField(max_length=200, null=False, blank=False)
    category = models.OneToOneField(FileCategory, related_name='files', on_delete=models.CASCADE)
    uploaded_file = models.FileField(upload_to='files/')

    def __str__(self):
        return '%s - %s' % (self.name, self.category)
