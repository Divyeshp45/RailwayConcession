from django.contrib import messages
from django.shortcuts import render
from MyApp.forms import UserApplication,UploadFileForm
from .models import ContactU, StudentApplication,FileUpload
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
# Create your views here.
#USER PAGE:
def index(request):
    return render(request,'MyApp/index.html')

def app(request):
    if request.method=='POST':
        form=UserApplication(request.POST)
        if form.is_valid():
            new_first_name=form.cleaned_data['first_name']
            new_last_name=form.cleaned_data['last_name']
            new_app_type=form.cleaned_data['app_type']
            new_tenure=form.cleaned_data['tenure']
            new_reg_id=form.cleaned_data['reg_id']
            new_email_id=form.cleaned_data['email_id']
            new_aadhar_no=form.cleaned_data['aadhar_no']
            new_address=form.cleaned_data['address']
            new_station=form.cleaned_data['station']
            new_junction=form.cleaned_data['junction']     
            new_date=form.cleaned_data['date']
            new_mobile=form.cleaned_data['mobile']
            if new_email_id.split("@")[1]=='sakec.ac.in':
                if len(str(new_mobile))==10:
                    new_student=StudentApplication(first_name=new_first_name,last_name=new_last_name,app_type=new_app_type,tenure=new_tenure,reg_id=new_reg_id,email_id=new_email_id,aadhar_no=new_aadhar_no,address=new_address,station=new_station,junction=new_junction,date=new_date,mobile=new_mobile)
                    new_student.save()
                    return render(request,'MyApp/app.html',{
                                        'form':UserApplication(),
                                        'Success':True})
                else:
                    return    HttpResponse("You Entered Invalid Mobile Number")        
            else:
                return HttpResponse("Please Provide College Emailid Only")
        else:
            return HttpResponse("Invalid data Apply Again")            
        
    else:
        return render(request,'MyApp/app.html',{'form':UserApplication()}) 






def download(request):
    if request.method=="POST":
       reg_id=request.POST['reg_id']
       try:
           form=FileUpload.objects.get(reg_id=reg_id)
       except FileUpload.DoesNotExist:
           form=None
       if form is not None:
           if form.file:
               context={"file":form.file,"success":True}
           elif form.feedbacks:
               context={"feedback":form.feedbacks,"success":True}
           elif (form.file and form.feedbacks):    
               context={"feedback":form.feedbacks,"file":form.file,"success":True}
           else:
               context={"success":True}
           return render(request,'MyApp/download.html',context)
       else:
           return render(request,'MyApp/download.html',{"pending":True})
                 
    return render(request,'MyApp/download.html')
def contact(request):
      contact=ContactU.objects.all()
      context={"contacts":contact}
      return render(request,'MyApp/contact.html',context)


#Admin Page:
def adminindex(request):
    return render(request,'MyApp/adminindex.html',{
        'students':StudentApplication.objects.all()})


def view_student(request,id):
    student =StudentApplication.objects.get(pk=id)    
    return HttpResponseRedirect(reverse('adminindex'))



def adminfile(request):
    if request.method=='POST':
        Approvalform=UploadFileForm(request.POST,request.FILES)
        if Approvalform.is_valid():
            new_f_name=Approvalform.cleaned_data['f_name']
            new_l_name=Approvalform.cleaned_data['l_name']
            new_reg_id=Approvalform.cleaned_data['reg_id']
            new_file=Approvalform.cleaned_data['file']
            new_feedbacks=Approvalform.cleaned_data['feedbacks']
            
            new_Approval=FileUpload(f_name=new_f_name,l_name=new_l_name,reg_id=new_reg_id,file=new_file,feedbacks=new_feedbacks)
            new_Approval.save()
            messages.success(request,"Successfully Submitted")
            return render(request,'MyApp/adminfile.html',{'Approvalform':UploadFileForm(),'Success':True})
    return render(request,'MyApp/adminfile.html',{'Approvalform':UploadFileForm()})





'''Early PROJECT:
def index(request):
    return render(request,'student/index.html',{
        'students':Student.objects.all()})

def view_student(request,id):
    student =Student.objects.get(pk=id)    
    return HttpResponseRedirect(reverse('index'))


'''
'''new_student=StudentApplication(first_name=new_first_name,
                                                     last_name=new_last_name,
                                                     app_type=new_app_type , 
                                                     tenure=new_tenure,
                                                     reg_id=new_reg_id,
                                                      email_id=new_email_id,
                                                      aadhar_no=new_aadhar_no,
                                                        address=new_address,
                                                       station=new_station,
                                                        junction=new_junction,      
                                                       date=new_date,
                                                     mobile=new_mobile)
                                                     
                                                    return render(request,'MyApp/app.html',{
                          'form':UserApplication(),
                          'Success':True}) 
                                                     
                                                     '''