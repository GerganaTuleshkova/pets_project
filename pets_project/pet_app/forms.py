import datetime

from django import forms

from pets_project.pet_app.models import Profile, Pet, PetPhoto


class CreateProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'picture']
        labels = {
            'picture': 'Link to Profile Picture',
        }
        widgets = {
            'first_name': forms.TextInput(
                attrs={'placeholder': 'Enter first name'},
            ),
            'last_name': forms.TextInput(
                attrs={'placeholder': 'Enter last name'},
            ),
            'picture': forms.TextInput(
                attrs={
                    'placeholder': 'Enter URL',
                }
            ),
        }


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        self.instance.delete()
        pets = Pet.objects.filter(owner=self.instance).all()
        photos = PetPhoto.objects.filter(tagged_pets__in=pets)
        photos.delete()
        pets.delete()

        return self.instance

    class Meta:
        model = Profile
        # exclude = '__all__'
        fields = []


class EditProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'picture', 'date_of_birth', 'email', 'gender', 'description']
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'picture': 'Link to Profile Picture',
            'date_of_birth': 'Date of Birth',
        }
        widgets = {
            'description': forms.Textarea(
                attrs={'placeholder': 'Enter description', 'rows': 3},
            ),
            'email': forms.TextInput(
                attrs={'placeholder': 'Enter email'},
            ),
            'date_of_birth': forms.SelectDateWidget(years=range(1920, datetime.datetime.now().year)),
            'gender': forms.Select(choices=Profile.GENDERS, )
        }


class CreatePetForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Pet
        fields = ['name', 'type', 'date_of_birth']
        labels = {
            'name': 'Pet Name',
            'date_of_birth': 'Day of Birth',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={'placeholder': 'Enter pet name'},
            ),
            'date_of_birth': forms.SelectDateWidget(years=range(1920, datetime.datetime.now().year)),
        }


class EditPetForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Pet
        fields = ['name', 'type', 'date_of_birth']
        labels = {
            'name': 'Pet Name',
            'date_of_birth': 'Day of Birth',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={'placeholder': 'Enter pet name'},
            ),
            'date_of_birth': forms.SelectDateWidget(years=range(1920, datetime.datetime.now().year)),

        }


class DeletePetForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Pet
        fields = ['name', 'type', 'date_of_birth']
        labels = {
            'name': 'Pet Name',
            'date_of_birth': 'Day of Birth',
        }
        widgets = {
            'date_of_birth': forms.SelectDateWidget(years=range(1920, datetime.datetime.now().year)),
        }


class CreatePhotoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = PetPhoto
        fields = ['photo', 'description', 'tagged_pets']
        labels = {
            'photo': 'Pet Image',
            'tagged_pets': 'Tag Pets',
        }
        widgets = {
            'description': forms.TextInput(
                attrs={'placeholder': 'Enter description'})
        }


class EditPhotoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = PetPhoto
        fields = ['description', 'tagged_pets']
        labels = {
            'tagged_pets': 'Tag Pets',
        }
