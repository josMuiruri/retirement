from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . models import Profiles
from . forms import ProfilesForm

# view profile
@login_required
def view_profile(request):
    profile = Profiles.objects.get(user=request.user)
    return render(request, 'profile/profile.html', {'profile': profile})

# edit profile
@login_required
def edit_profile(request):
    profile = Profiles.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfilesForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('view_profile')
        else:
            form = ProfilesForm(instance=profile)
        return render(request, 'profile/edit_profile.html', {'form': form})
