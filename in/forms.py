from django import forms

class CompanyInfoForm(forms.Form):
    name = forms.CharField(max_length=70, widget=forms.TextInput(attrs={ 'placeholder' : 'Firmanavn' }))
    address = forms.CharField(widget=forms.TextInput(attrs={ 'placeholder' : 'Addresse' }))
    postnr = forms.IntegerField(widget=forms.TextInput(attrs={ 'placeholder' : 'Postnr'}))
    by = forms.CharField(max_length=15, widget=forms.TextInput(attrs={ 'placeholder' : 'By'}))
    tlf = forms.CharField(max_length=15, widget=forms.TextInput(attrs={ 'placeholder' : 'Tlf'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={ 'placeholder' : 'Email'}))
    bank = forms.CharField(max_length=50, widget=forms.TextInput(attrs={ 'placeholder' : 'Bank'}))
    regnr = forms.IntegerField(widget=forms.TextInput(attrs={ 'placeholder' : 'Regnr'}))
    kontonr = forms.CharField(max_length=15, widget=forms.TextInput(attrs={ 'placeholder' : 'Kontonr'}))
