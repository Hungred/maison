from django.contrib import admin
from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetConfirmView


password_reset_params = {
    'template_name': 'password_reset.html',
    'email_template_name': 'password_reset/email.html',
    'subject_template_name': 'password_reset/subject.txt',
    'success_url': reverse_lazy('login:index'),
}
password_set_params = {
    'template_name': 'password_set.html',
    'post_reset_login': True,
    'success_url': reverse_lazy('login:index'),
}

app_name = 'login'
urlpatterns = [

    path('register', views.sign_up, name='register'),
    path('', views.sign_in, name='index'),
    path('logout', views.log_out, name='logout'),
    path('change_pwd', views.change_password, name='change'),
    path('profile/<str:username>', views.profile, name='profile'),
    path('profile/<str:username>/update', views.update_pf, name='update_profile'),
    path('emp_list', views.emp_list, name='emp_list'),
    path('act_emp', views.active_emp, name='active_emp'),
    path('update_emp/<int:pk>/', views.update_emp, name='update_emp'),
    path('delete_emp/<int:pk>/', views.delete_emp, name='delete_emp'),
    path(
        'password-reset/',
        PasswordResetView.as_view(**password_reset_params),
        name='password_reset'),
    path(
        'password-set/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(**password_set_params),
        name='password_set',
    ),
]

