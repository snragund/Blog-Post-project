from django.db import models

# Create Pay roll model in Database    
class Payroll(models.Model):
    class Meta:
        verbose_name_plural = 'Pay_rolls'
        
    Type_of_employee = models.CharField(max_length=20)

    def __str__(self):
        return self.Type_of_employee

# Create Team Leader model in Database
class Team(models.Model):
    class Meta:
        verbose_name_plural = 'Team_Leaders'
        
    Team_Leader = models.CharField(max_length=20)

    def __str__(self):
        return self.Team_Leader

# Create employee model in Database
class Employee(models.Model):
    Name = models.CharField(max_length=60)
    Employee_Id = models.CharField(max_length=60)
    Teams =  models.CharField(max_length=60)
    Hourly_rate = models.IntegerField()
    Month = models.CharField(max_length=20, default=1)
    Year = models.IntegerField(default=1)
    Monthly_salary = models.IntegerField(default=1)
    Team_Leader = models.ForeignKey(Team, on_delete=models.CASCADE, default=1)
    Type_of_employee = models.ForeignKey(Payroll,on_delete=models.CASCADE, default=1 )




