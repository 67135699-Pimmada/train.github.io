from django.db import models

# Create your models here.

class Train(models.Model):
    name = models.CharField(max_length=100)   # ชื่อ
    last = models.CharField(max_length=100)   # นามสกุล
    job = models.CharField(max_length=100)    # ตำแหน่งงาน
    section = models.CharField(max_length=100) # หัวข้อการอบรม
    email = models.EmailField(max_length=100)  # อีเมล
    phone = models.CharField(max_length=15)   # เบอร์โทร
    date = models.DateField(auto_now_add=True) # วันที่เพิ่มข้อมูล

    def __str__(self):
        return f"{self.name} {self.last}"
