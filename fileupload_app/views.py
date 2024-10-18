from django.shortcuts import render, redirect
from .forms import FileUploadForm   # importing fileduploadform that handle the file  upload form
import pandas as pd     # importing pandas for reading and processing file
# Create your views here.

# view funcation to handle file uploads

def upload_file(request):

    if request.method == 'POST':  # checking if request method is post which means the user has submitted a form
        form = FileUploadForm(request.POST,request.FILES)  # creating a instance of the form with the submitted data and uploaded files
        if form.is_valid():
            upload_file = form.save()  # saving the form to store the uploaded file in database


            if upload_file.file.name.endswith('.csv'):
                df = pd.read_csv(upload_file.file.path)
            
            else:
                df = pd.read_excel(upload_file.file.path)
            
            columns = df.columns.tolist()
            return render(request,'upload_success.html',{'columns':columns})

          
    else:
        form = FileUploadForm()
    return render(request,'upload.html',{'form':form})

# view funcation to render the upload success page
def upload_success(request):
    return render(request,'upload_success.html')

