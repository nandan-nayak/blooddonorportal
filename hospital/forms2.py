
from django import forms


class DonorUpdate(forms.Form):
    qrcode=forms.FileField(widget=forms.FileInput(attrs={'id':'qrcode','name':'qrcode'}))
    class Meta:
        fields=('qrcode',)




class DonorReport(forms.Form):
    donor_name=forms.CharField(max_length=30,required=False)
    donor_address=forms.CharField(max_length=30,required=False)
    donor_contact=forms.IntegerField(required=False)
    blood_group=forms.ChoiceField(choices=(("1","name"),),label="",
                                initial='',
                                widget=forms.Select(),
                                required=True)
    bloodreport=forms.FileField(widget=forms.FileInput(attrs={'id':'report','name':'report'}))
    class Meta:
        fields=('donor_name','donor_address','donor_contact','donor_group','bloodreport',)