from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="Homepage"),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="Contact"),
    path("search/", views.search, name="Search"),
    path("tracker/", views.tracker, name="TrackingStatus"),
    path("productview/", views.prodView, name="ProductView"),
]