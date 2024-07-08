#here se seek to customize registration form toremove default cluttering details

from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreateForm,self).__init__(*args,**kwargs)
        for field in ['username', 'password1','password2']:
            self.fields[field].help_text=None
            self.fields[field].widget.attrs.update({'class':'form-control'})



