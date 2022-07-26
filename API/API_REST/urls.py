from django.urls import path
from .views import CompanyViews

urlpatterns=[
    path('company/',CompanyViews.as_view(),name='company'),
    path('company/<int:id>',CompanyViews.as_view(),name='company_update')
]