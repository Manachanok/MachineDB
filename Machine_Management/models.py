from django.db import models

# Create your models here.


class Screen(models.Model):
    screen_id = models.CharField(max_length=15,primary_key=True)
    screen_name = models.CharField(max_length=20)
    file_py = models.CharField(max_length=30)
    file_html = models.CharField(max_length=20)
    def __str__(self):
        return self.screen_id
    class Meta:
        db_table = "Screen_management"

class Menu(models.Model):
    menu_id = models.CharField(max_length=30,primary_key=True)
    name = models.CharField(max_length=30)
    level = models.IntegerField()
    parent_menu = models.CharField(max_length=30,default=None,null=True)
    index = models.IntegerField()
    path_url = models.CharField(max_length=30,default=None,null=True)
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE)
    def __str__(self):
        return self.menu_id
    class Meta:
        db_table = "Menu_management"

class Role(models.Model):
    role_id = models.CharField(max_length=5,primary_key=True)
    role_name = models.CharField(max_length=15)
    members = models.ManyToManyField(Screen,through='Role_Screen')
    def __str__(self):
        return self.role_id
    class Meta:
        db_table = "Role_management"

class Role_Screen(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE)
    permission_insert = models.CharField(max_length=5)
    permission_update = models.CharField(max_length=5)
    permission_delete = models.CharField(max_length=5)
    class Meta:
        db_table = "Role_Screen"

class Production_line(models.Model):

    site = [('BC','บางชัน'),('CAD1','ลาดกระบัง1'),('CAD2','ลาดกระบัง2')]
    building = [('บางชัน1','บางชัน1'),('บางชัน2','บางชัน2'),('ลาดกระบัง1','ลาดกระบัง1'),('ลาดกระบัง2','ลาดกระบัง2')]
    floor = [('3','3'),('2','2'),('1','1')]

    productionline_id = models.AutoField(primary_key=True)
    location_site = models.CharField(choices=site,max_length=15,default='------')
    location_building = models.CharField(max_length=15,choices=building,default='-------')
    location_floor = models.CharField(max_length=10,choices=floor,default='1')
    production_line = models.IntegerField()

    def __str__(self):
        return str(self.production_line)
    class Meta:
        db_table = "Production_line"

class Organization(models.Model):
    org_id =  models.AutoField(primary_key=True)
    org_code = models.CharField(max_length=10)
    org_name = models.CharField(max_length=20)
    org_line = models.ManyToManyField(Production_line)
    def __str__(self):
        return self.org_code
    class Meta:
        db_table = "Organization"

class Machine_type(models.Model):
    mtype_id = models.AutoField(primary_key=True)
    mtype_code = models.CharField(max_length=20)
    mtype_name = models.CharField(max_length=50)
    create_by = models.CharField(max_length=20)
    create_date = models.DateField()
    last_update_by = models.CharField(max_length=20,default=None,null=True)
    last_update_date = models.DateField(default=None,null=True)
    def __str__(self):
        return self.mtype_code
    class Meta:
        db_table = "Machine_type"

class Machine(models.Model):
    machine_id = models.AutoField(primary_key=True)
    serial_id = models.CharField(max_length=50,default=None,null=True)
    machine_code = models.CharField(max_length=20,default=None,null=True)
    machine_name = models.CharField(max_length=50,default=None,null=True)
    machine_type = models.ManyToManyField(Machine_type)
    machine_brand = models.CharField(max_length=10,default=None,null=True)
    machine_model = models.CharField(max_length=10,default=None,null=True)
    machine_supplier_code = models.CharField(max_length=10,default=None,null=True)
    machine_location_id = models.CharField(max_length=10,default=None,null=True)
    machine_emp_id_response = models.CharField(max_length=15,default=None,null=True)
    machine_capacity_per_minute = models.CharField(max_length=10,default=None,null=True)
    machine_capacity_measure_unit = models.CharField(max_length=10,default=None,null=True)
    machine_power_use_watt_per_hour = models.CharField(max_length=10,default=None,null=True)
    machine_installed_datetime = models.DateField(default=None,null=True)
    machine_start_use_datetime = models.DateField(default=None,null=True)
    line = models.ForeignKey(Production_line,on_delete=models.CASCADE)
    class Meta:
        db_table = "Machine_master"

class User(models.Model):
    username = models.CharField(max_length=6,primary_key=True)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    password = models.CharField(max_length=15)
    email = models.CharField(max_length=30)
    create_by = models.CharField(max_length=6)
    create_date = models.DateTimeField()
    start_date = models.DateField()
    expired_date = models.DateField()
    expired_day = models.IntegerField(default=90)
    role = models.ForeignKey(Role,on_delete=models.CASCADE)
    update_by = models.CharField(max_length=6,default=None,null=True)
    update_date = models.DateTimeField(default=None,null=True)
    last_login_date = models.DateTimeField(default=None,null=True)
    org = models.ForeignKey(Organization,on_delete=models.CASCADE)
    class Meta:
        db_table = "User_management"






