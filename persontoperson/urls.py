from django.urls import path
from . import views

urlpatterns = [
    path("", views.p2pform, name="p2phome"),
    path("p1form/", views.p1form, name="p1home"),
    path("p1xp2exform/", views.p1xp2exactform, name="p1xp2exform"),
    path("axreportform/", views.ax_report_form, name="axhome"),
]