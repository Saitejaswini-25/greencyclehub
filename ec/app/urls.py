from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views
from django.urls import path, include

from .views import (
    add_to_cart, show_cart, update_plastic_quantity,
    update_cart, remove_cart_item
)
from .forms import (
    LoginForm, MyPasswordResetForm, MyPasswordChangeForm, MySetPasswordForm
)

urlpatterns = [
    # Home & Category
    path('', views.home, name="home"),
    path('category/<slug:val>/', views.CategoryView.as_view(), name="category"),
    path('category-title/<val>/', views.CategoryTitle.as_view(), name="category-title"),
    path('categoryplastic/<slug:val>/', views.CategoryPlasticView.as_view(), name="categoryplastic"),
    
    # Product Details
    path('productdetail/<int:pk>/', views.ProductDetail.as_view(), name="productdetail"),
    path('plasticitem/<int:pk>/', views.PlasticProductDetail.as_view(), name='plasticproductdetail'),
    
    # User Profile & Address
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name="address"),
    path('updateAddress/<int:pk>/', views.updateAddress.as_view(), name='updateAddress'),
    
    # Cart Management
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.show_cart, name='cart'),
    path('cart/update/<int:id>/', views.update_cart, name='update_cart'),
    path('cart/remove/<int:id>/', views.remove_cart_item, name='remove_cart_item'),
    
    # Plastic Item Quantity Management
    path('update-plastic-quantity/<int:item_id>/', views.update_plastic_quantity, name='update_plastic_quantity'),
    path('add_quantity/<int:item_id>/', views.add_quantity, name='add_quantity'),
    path('reduce_quantity/<int:item_id>/', views.reduce_quantity, name='reduce_quantity'),
    path('remove_item/<int:item_id>/', views.remove_item, name='remove_item'),
    path('add_plastic_quantity/<int:item_id>/', views.add_plastic_quantity, name='add_plastic_quantity'),
    path('reduce_plastic_quantity/<int:item_id>/', views.reduce_plastic_quantity, name='reduce_plastic_quantity'),
    path('remove_plastic_item/<int:item_id>/', views.remove_plastic_item, name='remove_plastic_item'),
    
    # Checkout
    path('checkout/', views.Checkout.as_view(), name='checkout'), 
    
    # User Authentication
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    path('login/', auth_views.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    
    # Password Management
    path('passwordchange/', auth_views.PasswordChangeView.as_view(
        template_name='app/changepassword.html', form_class=MyPasswordChangeForm, 
        success_url='/passwordchangedone'), name="passwordchange"),
    path('passwordchangedone/', auth_views.PasswordChangeDoneView.as_view(
        template_name='app/passwordchangedone.html'), name='passwordchangedone'),
    
    # Password Reset
    path("password-reset/", auth_views.PasswordResetView.as_view(
        template_name="app/password_reset.html", form_class=MyPasswordResetForm), name="password_reset"),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name="app/password_reset_done.html"), name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='app/password_reset_confirm.html', form_class=MySetPasswordForm), 
        name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='app/password_reset_complete.html'), name="password_reset_complete"),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
]

# Serve Media Files During Development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
