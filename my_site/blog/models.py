from django.db import models

# Create your models here.
class Role(models.Model):
    id = models.AutoField(primary_key=True)
    name  = models.CharField(max_length=64, unique=True)

    class Meta:
        db_table = 'roles'

    def __str__(self) -> str:
        return self.name
class User(models.Model):
    
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=64,unique=True,db_index=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE,related_name='role',null=True,blank=True)
        
    class Meta:
        db_table = 'users'
    
    def __str__(self) -> str:
        return self.username

