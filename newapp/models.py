from django.db import models

# Create your models here.
class Employee(models.Model):
    STANDARD = 'STD'
    MANAGER = 'MGR'
    SR_MANAGER = 'SRMGR'
    PRESIDENT = 'PRES'

    EMPLOYEE_TYPES = (
        (STANDARD, 'base employee'),
        (MANAGER, 'manager'),
        (SR_MANAGER, 'senior manager'),
        (PRESIDENT, 'president')
    )

    role = models.CharField(max_length=25, choices=EMPLOYEE_TYPES)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    manager = models.ForeignKey('self', null=True, blank=True, related_name='employee', on_delete=models.CASCADE)

    def __str__(self):
        return "<Employee: {} {}>".format(self.first_name, self.last_name)

    def __repr__(self):
        return self.__str__()

class Folder(models.Model):
    folder_name = models.CharField(max_length=255)
    creation_date = models.DateField()
    parent_folder = models.ForeignKey('self', null=True, blank=True, related_name="folder", on_delete=models.CASCADE)
    

    def __str__(self):
        return self.folder_name
    
    def __repr__(self):
        return self.__str__()