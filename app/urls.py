from django.urls import path

from app import views
from django.conf import settings
#import static
from django.conf.urls.static import static
#import views
from django.contrib.auth import views as auth_view
#import loginForm
#import MypasswordChangeForm
from .forms import LoginForm, MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm

from .forms import LoginForm
urlpatterns = [
    # path('', views.home),
    path('', views.ProductView.as_view(), name='home'),
    path('product-detail/<int:pk>/',
         views.ProductDetailView.as_view(), name='product-detail'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    # path('changepassword/', views.change_password, name='changepassword'),
    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>/', views.mobile, name='mobiledata'),
    path('accounts/login/', auth_view.LoginView.as_view(template_name='app/login.html',
         authentication_form=LoginForm), name='login'),
    path('logout/', auth_view.LogoutView.as_view(next_page='login'), name='logout'),

    path('registration/', views.CustomRegistrationView.as_view(),
         name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
     path('paymentdone/', views.payment_done, name='paymentdone'),
    # passwordchange
    path('passwordchange/', auth_view.PasswordChangeView.as_view(template_name='app/passwordchange.html',
         form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'), name='passwordchange'),
    # passwordchange done
    path('passwordchangedone/', auth_view.PasswordChangeDoneView.as_view(
        template_name='app/passwordchangedone.html'), name='passwordchangedone'),
    path('password-reset/', auth_view.PasswordResetView.as_view(template_name='app/password_reset.html',
         form_class=MyPasswordResetForm), name='password_reset'),
    path('password-reset/done/', auth_view.PasswordResetDoneView.as_view(
        template_name='app/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(
        template_name='app/password_reset_confirm.html', form_class=MySetPasswordForm), name='password_reset_confirm'),
    path('password-reset-complete/', auth_view.PasswordResetCompleteView.as_view(
        template_name='app/password_reset_complete.html'), name='password_reset_complete'),
    #path cart
     path('cart/', views.show_cart, name='showcart'),
     path('pluscart', views.plus_cart, name='pluscart'),
     path('minuscart', views.minus_cart, name='minuscart'),
     path('removecart', views.remove_cart, name='removecart'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
