from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from django.core.paginator import Paginator


# <------------------------Notices Board Related Querries ---------------------->

def NoticeBoardhomepage(request):
    return render(request,"index.html")




# <------------------------Notices Related Querries ---------------------->
def NoticeHomepage(request):
    return render(request,"Notice.html")

    #Department Related Notices 
def DepartmentNotice(request):
    return render(request,"Departmentrelatednotices.html")

    #Placement Related Notices 
def PlacementrelatedNotice(request):
    return render(request,"Placementrelatednotices.html")

    #Placement Result Related Notices 
def PlacementresultNotice(request):
    return render(request,"Placementresultnotices.html")





# <------------------------Circulars Related Querries ---------------------->
def CircularHomeinterface(request):
    return render(request,"CircularHomeinterface.html")




# <------------------------Course Allotment Related Querries ---------------------->
def CourseallotmentHomepage(request):
    return render(request,"CourseallotmentMain.html")
            #2nd Year
def Courseallotment2yr(request):
    return render (request,"Courseallotment2yr.html")
            #3rd Year
def Courseallotment3yr(request):
    return render (request,"Courseallotment3yr.html")
            #Final Year (4th Year)
def Courseallotment4yr(request):
    return render (request,"Courseallotment4yr.html")



#  <------------------- Time Table Related Querries --------------------->
def TimeTableHomepage(request):
    return render(request,"TimeTableMain.html")
            #2nd Year
def TimeTable2ndyr(request):
    return render(request,"TimeTable2yr.html")
            #3rd Year
def TimeTable3rdyr(request):
    return render(request,"TimeTable3yr.html")
            #Final Year (4th Year)
def TimeTable4thyr(request):
    return render(request,"TimeTable4yr.html")