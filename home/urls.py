from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage, name='homepage'),
    path('products/', views.ProductPage, name='productpage'),
    path('cart/', views.CartPage, name='cartpage'),
    path('checkout/', views.CheckoutPage, name="checkoutpage"),
    path('product-details/', views.ProductDetail, name="productdetail"),
    path('bmi/', views.BMIPage, name="bmi"),
    path('user-profile/', views.UserProfilePage, name="user-profile"),
    path('family-profile/', views.FamilyProfilePage, name="family-profile"),
    path('wishlist/', views.WishlistPage, name="wishlist"),
]
