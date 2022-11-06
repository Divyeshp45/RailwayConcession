from cProfile import label
from django import forms
from  .models import StudentApplication,FileUpload

TENURE=  [('monthly','Monthly'),
        ('quaterly','Quarterly')]

APP_TYPE=[('fresh','Fresh'),('renewal','Renewal')]
                            
class UserApplication(forms.ModelForm):
    tenure=forms.ChoiceField(widget=forms.RadioSelect, choices=TENURE)
    app_type=forms.ChoiceField(widget=forms.RadioSelect, choices=APP_TYPE)
    junction=forms.CharField(required=False,widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model= StudentApplication
        fields =[ 'first_name',
                  'last_name',
                  'app_type', 
                  'tenure',
                  'reg_id',
                  'email_id',
                  'aadhar_no',
                  'address',
                  'station',
                  'junction',      
                  'date',
                  'mobile',]
        labels={
                  'first_name':'First Name:',
                  'last_name':'Last Name',
                  'app_type':'Application Type:', 
                  'tenure':'Tenure:',
                  'reg_id':'College Registered Id:',
                  'email_id':'College EmailId:',
                  'aadhar_no':'Aadhaar No:',
                  'address':'Address:',
                  'station':'From Station:',
                  'junction':'Junction Via:',      
                  'date':'From Date:',
                  'mobile':'Mobile No'}
        
        widgets={'first_name':forms.TextInput(attrs={'class':'form-control'}),
                  'last_name':forms.TextInput(attrs={'class':'form-control'}),
                 
                  'reg_id':forms.NumberInput(attrs={'class':'form-control'}),
                  'email_id':forms.EmailInput(attrs={'class':'form-control'}),
                  'aadhar_no':forms.NumberInput(attrs={'class':'form-control'}),
                  'address':forms.Textarea(attrs={'class':'form-control'}),
                  'station':forms.TextInput(attrs={'class':'form-control'}),
                  'junction':forms.TextInput(attrs={'class':'form-control'}),      
                  'date':forms.DateInput(attrs={'class':'form-control'}),
                  'mobile':forms.NumberInput(attrs={'class':'form-control'}),}
        
class UploadFileForm(forms.ModelForm):
   
    file=forms.FileField(required=False,max_length=40)
    
    class Meta:
        model= FileUpload  
        fields =[ 'f_name',
                  'l_name',
                  'reg_id',
                  'file',
                  'feedbacks',
                  ]
        
        labels={
                  'f_name':'First Name:',
                  'l_name':'Last Name',
                  'reg_id':'College Registered Id:',
                  'file':'Approval Letter',
                  'feedbacks':'Feedback',
                  'date':'Date'}
        widgets={'f_name':forms.TextInput(attrs={'class':'forms-control'}),
                  'l_name':forms.TextInput(attrs={'class':'forms-control'}),
                 
                  'reg_id':forms.NumberInput(attrs={'class':'form-control'}),
                  'feedbacks':forms.Textarea(attrs={'class':'forms-control'}),
                  }