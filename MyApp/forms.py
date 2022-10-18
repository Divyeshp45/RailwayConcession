from django import forms
from  .models import StudentApplication

TENURE=  [('monthly','Monthly'),
        ('quaterly','Quarterly')]

APP_TYPE=[('fresh','Fresh'),('renewal','Renewal')]
                            
class UserApplication(forms.ModelForm):
    tenure=forms.ChoiceField(widget=forms.RadioSelect, choices=TENURE)
    app_type=forms.ChoiceField(widget=forms.RadioSelect, choices=APP_TYPE)
    junction=forms.CharField(required=False,widget=forms.TextInput(attrs={'class': 'forms-control'}))
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
        
        widgets={'first_name':forms.TextInput(attrs={'class':'forms-control'}),
                  'last_name':forms.TextInput(attrs={'class':'forms-control'}),
                 
                  'reg_id':forms.NumberInput(attrs={'class':'form-control'}),
                  'email_id':forms.EmailInput(attrs={'class':'form-control'}),
                  'aadhar_no':forms.NumberInput(attrs={'class':'form-control'}),
                  'address':forms.Textarea(attrs={'class':'forms-control'}),
                  'station':forms.TextInput(attrs={'class':'forms-control'}),
                  'junction':forms.TextInput(attrs={'class':'forms-control'}),      
                  'date':forms.DateInput(attrs={'class':'forms-control'}),
                  'mobile':forms.NumberInput(attrs={'class':'forms-control'}),}
        
  