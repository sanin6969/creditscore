from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",include("credit_score.urls") ),
    path("auth/",include("auth_credit.urls") ),
]
