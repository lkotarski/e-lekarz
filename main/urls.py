from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),

    path('new/<mode>/', views.newRegister, name='new'),

    path('register/<mode>', views.registerUser, name='register'),
    path('doctorRegister/', views.registerDoctor, name='registerDoctor'),

    path('activate_user/<uidb64>/<token>', views.activate_user, name='activate_user'),
    path('activate_doctor/<uidb64>/<token>', views.activate_doctor, name='activate_doctor'),

    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_request, name='logout'),
    path('delete/', views.deleteuser, name='delete'),

    path('password_change/', auth_views.PasswordChangeView.as_view(), name="password_change"),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name="password_change_done"),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),


    path('edit/', views.editProfile, name='editProfile'),
    path('editDoc/', views.editDocProfile, name='editDocProfile'),
    path('profile/', views.profileView, name='profileView'),

    path('doctor/<int:id>/', views.docProfile, name='docProfile'),
    #path('search', views.search, name='search'),
    re_path(r'^search/$', views.search, name='search'),

    path('appointment/<int:id>', views.makeAppointment, name='appointment'),
]