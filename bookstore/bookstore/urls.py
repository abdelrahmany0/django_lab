"""bookstore URL Configuration

The `urlpatterns` list routes URLs to book. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function book
    1. Add an import:  from my_app import book
    2. Add a URL to urlpatterns:  path('', book.home, name='home')
Class-based book
    1. Add an import:  from other_app.book import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("", include("accounts.urls")),
    path("admin/", admin.site.urls),
    path("book/", include('book.urls')),
    path("api/", include('book.api.urls')),
]
