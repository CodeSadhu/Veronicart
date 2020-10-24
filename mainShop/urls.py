from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="Homepage"),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="Contact"),
    path("tracker/", views.tracker, name="TrackingStatus"),
    path("checkout/", views.checkout, name="Checkout"),
    path("products/<int:myId>", views.prodView, name="ProductView"),
]