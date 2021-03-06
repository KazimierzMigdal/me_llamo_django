from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views
from users.forms import MyAuthForm


urlpatterns = [
    path('', include('memo_card.urls')),
    path('admin/', admin.site.urls),
    path('login/',
        user_views.MyLoginView.as_view(),
        name='login'),
    path('logout/',
        auth_views.LogoutView.as_view(template_name='users/logout.html'),
        name='logout'),
    path('password-reset/',
        user_views.MyPasswordResetView.as_view(template_name='users/password_reset.html'),
        name='password_reset'),
    path('password-reset/done',
        auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
        name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
        user_views.MyPasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
        name='password_reset_confirm'),
    path('password-reset-complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
        name='password_reset_complete'),
    path('profile-edit/',
        user_views.profile_edit,
        name='profile_edit'),
    path('register/',
        user_views.register,
        name='register'),
    path('statistics/', include('stats.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
