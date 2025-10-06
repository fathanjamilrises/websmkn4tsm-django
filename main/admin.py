from django.contrib import admin
from .models import InformationStatistics
from  .models import Jurusan
from  .models import Eskul
from .models import Berita

# Register your models here.
admin.site.register(InformationStatistics)
admin.site.register(Jurusan)
admin.site.register(Eskul)
admin.site.register(Berita)
