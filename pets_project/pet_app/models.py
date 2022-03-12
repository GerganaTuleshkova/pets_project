import datetime

from django.core.validators import MinLengthValidator
from django.db import models

from pets_project.pet_app.helpers_functions import has_letters_only_validator, validate_file_size


class Profile(models.Model):
    MALE = 'male'
    FEMALE = 'female'
    DO_NOT_SHOW = 'do not show'
    GENDERS = [
        (MALE, 'male'),
        (FEMALE, 'female'),
        (DO_NOT_SHOW, 'do not show')]

    first_name = models.CharField(
        max_length=30,
        validators=[
            MinLengthValidator(2),
            has_letters_only_validator,
        ]
    )

    last_name = models.CharField(
        max_length=30,
        validators=[
            MinLengthValidator(2),
            has_letters_only_validator,
        ]
    )

    picture = models.URLField()
    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    email = models.EmailField(
        null=True,
        blank=True,
    )
    gender = models.CharField(
        max_length=max([len(g) for g, _ in GENDERS]),
        null=True,
        blank=True,
        choices=GENDERS,
        default=DO_NOT_SHOW,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Pet(models.Model):
    CAT = 'cat'
    DOG = 'dog'
    BUNNY = 'bunny'
    PARROT = 'parrot'
    FISH = 'fish'
    OTHER = 'other'
    TYPES = [(x, x) for x in (CAT, DOG, BUNNY, PARROT, FISH, OTHER)]
    name = models.CharField(max_length=30)
    type = models.CharField(
        max_length=max([len(p) for p, _ in TYPES]),
        choices=TYPES,
    )
    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )
    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )

    class Meta:
        unique_together = ('owner', 'name')

    @property
    def age(self):
        return datetime.datetime.now().year - self.date_of_birth.year

    def __str__(self):
        return self.name


class PetPhoto(models.Model):
    photo = models.ImageField(
        validators=[validate_file_size],
        upload_to='photos'

    )
    tagged_pets = models.ManyToManyField(
        Pet,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    created_on = models.DateTimeField(
        auto_now_add=True,
    )
    likes = models.IntegerField(
        default=0,
    )
