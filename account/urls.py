from django.urls import path


from .views import sign_in, register, logout_user, ajax_reg

urlpatterns = [
    path('login', sign_in, name='login-page'),
    path('register', register, name='register'),
    path('logout', logout_user, name='logout'),
    path('ajax_reg', ajax_reg, name='ajax_reg'),
]
