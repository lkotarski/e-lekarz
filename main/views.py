from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .tokens import account_activation_token
from django.template.loader import render_to_string
from django.core.mail import EmailMessage


from .models import Appointment, DoctorProfile, Comment, CustomUser
from .forms import UserRegistrationForm, DoctorProfileForm, CommentForm, UserEditForm, AppointmentFormAnonymous, AppointmentFormLogged, NewForm, UserDeleteForm
from .filters import DocFilterBySpec, DocFilterByCity
from datetime import datetime

def newRegister(request, mode='user'):
    if request.method == 'POST':
        form = NewForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False, mode=mode)
            user.is_active = False
            user.save(mode)
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            if mode!="doctor":
                message = render_to_string('registration/userConfirmation.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })

            else:
                message = render_to_string('registration/doctorConfirmation.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            

            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return render(request, 'registration/waitForActivate.html')
    else:
        form = NewForm()
    return render(request, 'registration/new.html', {'user_form': form, 'mode1':mode})


def oldRegister(request, mode='user'):
    if request.method == "POST":
        form = NewForm(request.POST)
        if form.is_valid():
            user = form.save(mode)
            login(request, user)
            messages.success(request, "Pomyślnie zarejestrowano konto." )
            if mode != "doctor":
                return redirect("main:home")
            else:
                return redirect("main:registerDoctor")
        messages.error(request, "Nie wszystkie pola zostały poprawnie uzupełnione.")
    else:
        form = NewForm()
    context = {"user_form":form, 'mode1':mode}
    return render(request, 'registration/new.html', context)

def activate_user(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        messages.success(request, "Pomyślnie aktywowano konto." )
        return redirect('main:home')
    else:
        return render(request, 'registration/invalidActivation.html')

def activate_doctor(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect("main:registerDoctor")
    else:
        return render(request, 'registration/invalidActivation.html')

@login_required
def logout_request(request):
    logout(request)
    messages.info(request, "Wylogowano z konta.") 
    return redirect("main:home")

def registerUser(request, mode):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save(mode)
            new_user = authenticate(username=user_form.cleaned_data['username'],
                                    password=user_form.cleaned_data['password'],
                                    )
            login(request, new_user)
            if mode != "doctor":
                return HttpResponseRedirect("/")
            else:
                return HttpResponseRedirect("/doctorRegister/")
    else:
        user_form = UserRegistrationForm()
    context = {'user_form':user_form, 'mode': mode}
    return render(request, 'registration/userRegister.html', context)

def registerDoctor(request):
    #request.user.id
    if request.method == "POST":
        doc = DoctorProfile.objects.create(user=request.user)
        doctor_profile_form = DoctorProfileForm(instance=doc, data=request.POST)
        if doctor_profile_form.is_valid():
            doctor_profile_form.save()
            return redirect("main:home")
    else:
        doctor_profile_form = DoctorProfileForm()
    context = {'doc_form': doctor_profile_form}
    return render(request, 'registration/doctorRegister.html', context)

def home(request):
    docs = DoctorProfile.objects.all()
    doc_filter = DocFilterBySpec(request.GET, queryset=docs)
    #city_filter = DocFilterByCity(request.GET, queryset=docs)
    context = {'docList':doc_filter}
    return render(request, 'homepage/home.html', context)

def docProfile(request, id):
    doc = get_object_or_404(DoctorProfile, user=id)
    comments = Comment.objects.filter(doctor=doc.user)
    #print(f"Doc id is {id}")

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.instance.doctor = doc.user
            form.save()
    else:
        form = CommentForm()

    context = {'doc': doc, 'comments': comments, 'comment_form':form}
    return render(request, 'docProfile/docProfile.html', context)

def search(request):
    docs = DoctorProfile.objects.all()
    doc_filter = DocFilterBySpec(request.GET, queryset=docs)
    city_filter = DocFilterByCity(request.GET, queryset=docs)
    context = {'docList':doc_filter, 'cityFilter':city_filter}
    return render(request, 'search.html', context)

def makeAppointment(request, id):
    doc = get_object_or_404(DoctorProfile, user=id)

    if request.method == 'POST':
        if request.user.is_anonymous:
            form = AppointmentFormAnonymous(request.POST)
        else:
            form = AppointmentFormLogged(request.POST)
            form.instance.first_name = request.user.first_name
            form.instance.last_name = request.user.last_name
            form.instance.phone_number = request.user.phone_number
        if form.is_valid():
            if not request.user.is_anonymous:
                form.instance.patient = request.user
            form.instance.doctor = doc.user
            form.save()
            messages.success(request, "Pomyślnie umówiono wizytę!") 
            return redirect("main:docProfile", id=id)
        else:
            messages.error(request, "Wypełnij poprawnie formularz, by umówić się na wizytę")
    else:
        if request.user.is_anonymous:
            form = AppointmentFormAnonymous()
        else:
            form = AppointmentFormLogged()
    context = {'doc': doc, 'form': form}
    return render(request, 'docProfile/appointment.html', context)
    

@login_required
def profileView(request):
    today = datetime.now()
    dateNow = today.strftime("%Y-%m-%d")
    timeNow = today.strftime("%H:%M:%S")
    visits_old = Appointment.objects.filter(patient=request.user, date__lt = dateNow)
    visits_today_old = Appointment.objects.filter(patient=request.user, date = dateNow, hour__lt = timeNow)
    visits_today_next = Appointment.objects.filter(patient=request.user, date = dateNow, hour__gte = timeNow)
    visits_next = Appointment.objects.filter(patient=request.user, date__gt = dateNow)

    if request.user.isDoctor:
        doc = request.user
        patients_today = Appointment.objects.filter(doctor=doc, date = dateNow, hour__gte = timeNow)
        patients_future = Appointment.objects.filter(doctor=doc, date__gt = dateNow)
    else:
        patients_today = ""
        patients_future = ""




    context = {'visits_old':visits_old, 'visits_next':visits_next, 'today_old': visits_today_old, 'today_next': visits_today_next, 'patients_today':patients_today, 'patients_future':patients_future}
    return render(request, 'account/userProfile.html', context)

@login_required
def editProfile(request):
    if request.method == 'POST':
        form = UserEditForm(instance=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Pomyślnie edytowano profil użytkownika.")
    else:
        form = UserEditForm(instance=request.user)
    context = {'form':form}
    return render(request, 'account/editProfile.html', context)

@login_required
def editDocProfile(request):
    doc = get_object_or_404(DoctorProfile, user=request.user)
    if request.method == 'POST':
        form = DoctorProfileForm(instance=doc, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Pomyślnie edytowano profil doktora.")
    else:
        form = DoctorProfileForm(instance=doc)
    context = {'form':form, 'doc':doc}
    return render(request, 'account/editDocProfile.html', context)

@login_required
def deleteuser(request):
    if request.method == 'POST':
        delete_form = UserDeleteForm(request.POST, instance=request.user)
        user = request.user
        if user.isDoctor:
            doc = get_object_or_404(DoctorProfile, user=request.user)
            doc.delete()
        user.delete()
        messages.info(request, 'Konto zostało usunięte.')
        return redirect('main:home')
    else:
        delete_form = UserDeleteForm(instance=request.user)

    context = {'delete_form': delete_form}

    return render(request, 'registration/delete.html', context)