
from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from home.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from home.models import Contact

def home(request):
    return render(request,'home/home.html')

def about(request):
    return render(request,'home/about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request, "Please fill up the field correctly!")

        else:
            messages.success(request, "Please fill up the field correctly!")
            contact = Contact( name=name, email=email, phone=phone, content=content)
            contact.save()
    return render(request, 'home/contact.html')

def register(request):
    if request.method =='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'home/register.html', {'form': form})

@login_required
def profile(request):
    if request.method =='POST':
        u_form  = UserUpdateForm(request.POST, instance=request.user)
        p_form  = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form  = UserUpdateForm(instance=request.user)
        p_form  = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request, 'home/profile.html', context)







