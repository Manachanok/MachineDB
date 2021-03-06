from django import forms
from .models import *
import datetime

class MachineForm(forms.ModelForm):
    serial_id                   = forms.CharField(label='Serial ID : ',widget=forms.TextInput(attrs={"maxlength":50}))
    machine_code                = forms.CharField(label='Machine Code : ',widget=forms.TextInput(attrs={"placeholder":"","maxlength":20}))
    machine_name                = forms.CharField(label='Machine Name : ',required=False,widget=forms.TextInput(attrs={"placeholder":"","maxlength":50}))
    machine_brand               = forms.CharField(label='Machine brand : ',required=False,widget=forms.TextInput(attrs={"placeholder":"","maxlength":10}))
    machine_model               = forms.CharField(label='Machine model : ',required=False,widget=forms.TextInput(attrs={"placeholder":"","maxlength":10}))
    machine_supplier_code       = forms.CharField(label='Machine supplier code : ',required=False,widget=forms.TextInput(attrs={"placeholder":"","maxlength":10}))
    machine_location_id         = forms.CharField(label='Machine location id : ',required=False,widget=forms.TextInput(attrs={"placeholder":"","maxlength":10}))
    machine_emp_id_response     = forms.CharField(label='Machine emp id response : ',required=False,widget=forms.TextInput(attrs={"placeholder":"","maxlength":15}))
    machine_capacity_per_minute = forms.CharField(label='Machine capacity/min : ',required=False,widget=forms.TextInput(attrs={"placeholder":"","maxlength":10}))
    machine_capacity_measure_unit   = forms.CharField(label='Machine capacity measure unit : ',required=False,widget=forms.TextInput(attrs={"placeholder":"","maxlength":10}))
    machine_power_use_watt_per_hour = forms.CharField(label='Machine power use watt/hour : ',required=False,widget=forms.TextInput(attrs={"placeholder":"","maxlength":10}))
    machine_installed_datetime  = forms.DateField(required=False,widget=forms.DateInput(attrs={"type":"date"}))
    machine_start_use_datetime  = forms.DateField(required=False,widget=forms.DateInput(attrs={"type":"date"}))
    class Meta:
        model = Machine
        fields = [
            'serial_id',
            'machine_code',
            'machine_name',
            'machine_brand',
            'machine_model',
            'machine_supplier_code',
            'machine_location_id',
            'machine_emp_id_response',
            'machine_capacity_per_minute',
            'machine_capacity_measure_unit',
            'machine_power_use_watt_per_hour',
            'machine_installed_datetime',
            'machine_start_use_datetime',
            'machine_type',
            'line'
        ]

    def clean_machine_code(self,*args,**kwargs):
        machine_code = self.cleaned_data.get("machine_code")
        if "mch" not in machine_code:
            raise forms.ValidationError("This is not 'mch'")
        return machine_code

class ProductLineForm(forms.ModelForm):
    class Meta:
        model = Production_line
        fields = [
            'productionline_id',
            'location_site',
            'location_building',
            'location_floor',
            'production_line'
        ]

class UserForm(forms.ModelForm):
    username = forms.CharField(label='Username : ',widget=forms.TextInput(attrs={"maxlength":6}))
    firstname = forms.CharField(label='First name : ',widget=forms.TextInput(attrs={"maxlength":20}))
    lastname = forms.CharField(label='Last name : ',widget=forms.TextInput(attrs={"maxlength":20}))
    password = forms.CharField(label='password : ',widget=forms.TextInput(attrs={"maxlength":15,"type":"password"}))
    email = forms.CharField(label='Email : ',widget=forms.TextInput(attrs={"maxlength":30,"type":"email"}))
    start_date = forms.DateField(widget=forms.DateInput(attrs={"type":"date"}))
    con_password = forms.CharField(label='confirm password : ',widget=forms.TextInput(attrs={"maxlength":15,"type":"password"}))
    create_by = ""
    now = datetime.datetime.now()
    create_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"type":"datetime","value":now}))
    expired_date = forms.DateField(label='expired date : ',widget=forms.TextInput(attrs={"type":"date","value":(now - datetime.timedelta(1)).date()}))
    class Meta:
        model = User
        fields = [
            'username',
            'firstname',
            'lastname',
            'password',
            'email',
            'start_date',
            'create_by',
            'expired_date',
            'expired_day',
            'create_date',
            'role',
        ]
