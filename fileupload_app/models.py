from django.db import models

# Create your models here.

# Defining a model named uploaded file to store information about uploaded file

class UploadedFile(models.Model): 
    file = models.FileField(upload_to = 'uploads/')   # the 'upload_to' parameter specifies that up;paded files will be saved in dir. named 'uploads
    uploaded_at = models.DateTimeField(auto_now_add = True)  # 'auto_now_add' automatically sets this field to the current date and time

