from django import forms

class virkomshedinfo(forms.Form):
    firm_name = forms.CharField(max_length=40,
                widget=forms.TextInput(attrs={ 'placeholder': 'Firmanavn' }))
    address = forms.CharField(
              widget=forms.TextInput(attrs={ 'placeholder' : 'Addresse' }))
    postnr = forms.IntegerField(
             widget=forms.TextInput(attrs={ 'placeholder' : 'Postnr' }))
    by = forms.CharField(widget=forms.TextInput(attrs={ 'placeholder' : 'By' }))
    tlf = forms.CharField(widget=forms.TextInput(attrs={ 'placeholder' : 'Tlf.' }))
    email = forms.EmailField(widget=forms.TextInput(attrs={ 'placeholder' : 'Email' }))
    bank = forms.CharField(widget=forms.TextInput(attrs={ 'placeholder' : 'Bank' }))
    regnr = forms.CharField(widget=forms.TextInput(attrs={ 'placeholder' : 'Regnr' }))
    kontonr = forms.CharField(widget=forms.TextInput(attrs={ 'placeholder' : 'Kontonr' }))
