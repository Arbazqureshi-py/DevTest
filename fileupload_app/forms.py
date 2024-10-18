from django import forms
from .models import UploadedFile  # importing the uploadedfile model from the app


# define a form class for handling file uploads
class FileUploadForm(forms.ModelForm):
    class Meta:  # class meta define for  the form
        model = UploadedFile  #specifying that this form is associated with uplodedfile model
        fields = ['file']  # specifying that form will include only the 'file' field form
        widgets = {

            'file': forms.FileInput(attrs={'accept':'.csv,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet, application/vnd.ms-excel'})
        }
    

    # method for custom validation of uploaded file

    def clean_file(self):

        file = self.cleaned_data.get('file')
        if file:
            ext = file.name.split('.')[-1].lower()
            if ext not in ['csv','xlsx','xls']:
                raise forms.ValidationError("Only CSV and Excel file are allowed")
# Return the file if it passes the validation.
        return file