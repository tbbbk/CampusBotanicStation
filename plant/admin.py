from django.contrib import admin

from .models import *

# 注册ArticlePost到admin中
admin.site.register(Plant)
admin.site.register(Genus)
admin.site.register(Family)  
admin.site.register(Recommendation)