from django.db import models

# Create your models here.
class InformationStatistics(models.Model):
    siswa_aktif = models.IntegerField(default=0)
    guru_profesional = models.IntegerField(default=0)
    program_keahlian = models.IntegerField(default=0)

    def __str__(self):
        return f"Statistics: {self.siswa_aktif} Siswa, {self.guru_profesional} Guru, {self.program_keahlian} Program"
    


class Jurusan(models.Model):
        title=models.CharField(max_length=100)
        description=models.TextField()
        image_url=models.URLField()
        nama_kaprog=models.CharField(max_length=100)
        jumlah_siswa=models.IntegerField(default=0)
        jumlah_guru=models.IntegerField(default=0)

        def __str__(self):
            return self.title
        
class Eskul(models.Model):
        title=models.CharField(max_length=100)
        description=models.TextField()
        image_url=models.URLField()

        def __str__(self):
            return self.title
        
class Berita(models.Model):
        title=models.CharField(max_length=200)
        content=models.TextField()
        author=models.CharField(max_length=100)
        image_url=models.URLField(blank=True, null=True)
        published_date=models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return self.title
