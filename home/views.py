from django.shortcuts import render
from product.models import Product

def HomePage(request):
    return render(request, 'home.html')

def ProductPage(request):
    return render(request, 'products.html')

def CartPage(request):
    return render(request, 'cart.html')

def CheckoutPage(request):
    return render(request, 'checkout.html')

def ProductDetail(request):
    return render(request, 'product-details.html')

def WishlistPage(request):
    return render(request, 'wishlist.html')

def BMIPage(request):
    return render(request, 'bmi.html')

def ReminderPage(request):
    return render(request, 'set-reminder.html')

def UserProfilePage(request):
    return render(request, 'user-profile.html')

def FamilyProfilePage(request):
    return render(request, 'family-profile.html')
