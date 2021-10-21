from django.db import models
from django.contrib.auth.models import User


class WorkingStatus(models.Model):
    status = models.CharField(max_length=255, verbose_name='status bekerja sekarang : ')

    def __str__(self):
        return self.status


class WorkZone(models.Model):
    buildings = models.CharField(max_length=255, verbose_name='Nama Gedung : ')
    tower_name = models.CharField(max_length=255, verbose_name='Nama Tower : ')
    ground_name = models.CharField(max_length=255, verbose_name='Nama Lantai : ')
    job_area = models.CharField(max_length=255, verbose_name='Zona Kerja : ')

    def __str__(self):
        return self.buildings


class EmployeeManagement(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nik = models.CharField(unique=True, verbose_name='NIK : ', max_length=255)
    is_employee = models.BooleanField(default=True)
    is_supervisor = models.BooleanField(default=False)
    zone = models.ForeignKey(WorkZone, on_delete=models.CASCADE)
    shift = models.IntegerField(default=0)
    status = models.ForeignKey(WorkingStatus, on_delete=models.CASCADE)

    def __str__(self):
        if self.is_employee and self.is_supervisor:
            return f"{self.user.name} is supervisor "
        elif self.is_employee and not self.is_supervisor:
            return f"{self.user.name} just employee "


class BarcodeQRPerZone(models.Model):
    unique_code = models.TextField(verbose_name='unique code : ')
    zone = models.ForeignKey(WorkZone, on_delete=models.CASCADE)

    def __str__(self):
        return f"barcode for {self.zone} - {self.zone.job_area}"
