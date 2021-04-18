from django.urls import path
from .views import signup, login, account, opportunity, index, logout

urlpatterns = [
    path('signup', signup, name='signup'),
    path('login', login, name='login'),
    path('account', account, name='account'),
    path('opportunity', opportunity, name='opportunity'),
    path('opportunity/<int:account>', opportunity, name='opportunity'),
	path('', index, name='index'),

	path('logout', logout, name='logout'),
]