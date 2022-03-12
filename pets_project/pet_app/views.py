from django.shortcuts import render, redirect

from pets_project.pet_app.forms import CreateProfileForm, CreatePetForm, CreatePhotoForm, EditPhotoForm, EditPetForm, \
    DeletePetForm, EditProfileForm, DeleteProfileForm
from pets_project.pet_app.models import Profile, PetPhoto, Pet


def get_profile():
    profile = Profile.objects.all()
    if profile:
        return profile[0]
    return None


def home(request):
    profile = get_profile()
    context = {
        'profile': profile,
        'nav_hide_items': True,
        'not_logged': True,
    }

    return render(request, 'home_page.html', context)


def dashboard(request):
    profile = get_profile()
    if not profile:
        return redirect('not found')
    photos = PetPhoto.objects.prefetch_related('tagged_pets').filter(tagged_pets__owner=profile).distinct()
    pets = Pet.objects.all()

    context = {
        'photos': photos,
        'pets': pets,
        'profile': profile,
    }
    return render(request, 'dashboard.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateProfileForm()
    context = {
        'form': form,
    }
    return render(request, 'profile_create.html', context)


def profile_details(request):
    profile = get_profile()
    if not profile:
        return redirect('not found')
    pets = Pet.objects.filter(owner=profile)
    photos = PetPhoto.objects.filter(tagged_pets__in=pets).distinct()
    photos_count = len(photos)
    likes = sum([p.likes for p in photos])

    context = {
        'profile': profile,
        'photo_count': photos_count,
        'likes': likes,
        'pets': pets,
    }
    return render(request, 'profile_details.html', context)


def edit_profile(request):
    profile = get_profile()
    if not profile:
        return redirect('not found')
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')
    else:
        form = EditProfileForm(instance=profile)
    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'profile_edit.html', context)


def delete_profile(request):
    profile = get_profile()
    if not profile:
        return redirect('not found')
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')
    else:
        form = DeleteProfileForm(instance=profile)
    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'profile_delete.html', context)


def pet_add(request):
    profile = get_profile()
    if request.method == 'POST':
        form = CreatePetForm(request.POST, instance=Pet(owner=profile))
        if form.is_valid():
            form.save()
            return redirect('profile details')
    else:
        form = CreatePetForm()
    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'pet_create.html', context)


def pet_edit(request, pk):
    profile = get_profile()
    pet = Pet.objects.get(pk=pk)
    if not profile:
        return redirect('not found')
    if request.method == 'POST':
        form = EditPetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('profile details')
    else:
        form = EditPetForm(instance=pet)
    context = {
        'form': form,
        'profile': profile,
        'pet': pet,
    }
    return render(request, 'pet_edit.html', context)


def pet_delete(request, pk):
    profile = get_profile()
    pet = Pet.objects.get(pk=pk)
    if not profile:
        return redirect('not found')
    if request.method == 'POST':
        form = DeletePetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('profile details')
    else:
        form = DeletePetForm(instance=pet)
    context = {
        'form': form,
        'profile': profile,
        'pet': pet,
    }
    return render(request, 'pet_delete.html', context)


def photo_details(request, pk):
    profile = get_profile()
    photo = PetPhoto.objects.prefetch_related('tagged_pets').get(pk=pk)

    context = {
        'photo': photo,
        'profile': profile,
    }
    return render(request, 'photo_details.html', context)


def photo_add(request):
    profile = get_profile()
    if request.method == 'POST':
        form = CreatePhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = CreatePhotoForm()
    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'photo_create.html', context)


def photo_edit(request, pk):
    profile = get_profile()
    photo = PetPhoto.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditPhotoForm(request.POST, request.FILES, instance=photo)
        if form.is_valid():
            form.save()
            return redirect('photo details', pk)
    else:
        form = EditPhotoForm(instance=photo)
    context = {
        'form': form,
        'profile': profile,
        'photo': photo,
    }
    return render(request, 'photo_edit.html', context)


def photo_delete(request, pk):
    photo = PetPhoto.objects.get(pk=pk)
    photo.delete()
    return redirect('dashboard')


def like_pet_photo(request, pk):
    photo = PetPhoto.objects.get(pk=pk)
    photo.likes += 1
    photo.save()
    return redirect('photo details', pk)


def not_found(request):
    return render(request, '401_error.html')
