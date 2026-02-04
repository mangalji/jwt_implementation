from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("",views.endpoints),
    
    # urls for advocates

    # path("advocates/",views.advocates_list,name='advocates'),
    path("advocates/",views.AdvocateList.as_view(),name="advocate_list"),
    # path("advocates/<str:username>",views.advocates_details),
    path("advocates/<str:username>/",views.AdvocateDetail.as_view(),name="advocate_detail"),

    # urls for companies
    path("companies/",views.company_list,name='company_list'),
    path("companies/<int:pk>/",views.company_detail,name="company_details"),

    # urls for jwt auth
    path('token/',TokenObtainPairView.as_view(),name='token_obtain_pair')

]
