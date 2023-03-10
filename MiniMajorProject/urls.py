"""MiniMajorProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from MiniMajorProject import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.NoticeBoardhomepage,name="homepage"),
    # path('NoticeBoardhomepage/',views.NoticeBoardhomepage),
    
    path('Notice_Homepage/',views.NoticeHomepage,name="Notice_Homepage"),
    path('Department_Notice/',views.DepartmentNotice,name="Department_Notice"),
    path('Placementrelated_Notice/',views.PlacementrelatedNotice,name="Placementrelated_Notice"),
    path('Placementresult_Notice/',views.PlacementresultNotice,name="Placementresult_Notice"),
    
    path('Circular_Homepage/',views.CircularHomeinterface,name="Circular_Homepage"),
    
    path('CourseAllotment_Homepage/',views.CourseallotmentHomepage,name="CourseAllotment_Homepage"),
    path('Courseallotment2yr/',views.Courseallotment2yr,name="Courseallotment2yr"),
    path('Courseallotment3yr/',views.Courseallotment3yr,name="Courseallotment3yr"),
    path('Courseallotment4yr/',views.Courseallotment4yr,name="Courseallotment4yr"),
    
    path('TimeTable_Homepage/',views.TimeTableHomepage,name="TimeTable_Homepage"),
    path('TimeTable_2Yr/',views.TimeTable2ndyr,name="TimeTable_2Yr"),
    path('TimeTable_3Yr/',views.TimeTable3rdyr,name="TimeTable_3Yr"),
    path('TimeTable_4Yr/',views.TimeTable4thyr,name="TimeTable_4Yr"),
]


if settings.DEBUG:
      urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)