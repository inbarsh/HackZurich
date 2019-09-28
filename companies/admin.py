from django.contrib import admin

from .models import Company

class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name", "score", "graph_image", "words_frequency_image",)

admin.site.register(Company, CompanyAdmin)
