from .models import Talent_Ethnicity, Talent
from django.contrib import admin

admin.site.site_title = "InfluDom"
admin.site.site_header = "InfluDom"
admin.site.index_title = "InfluDom"


@admin.register(Talent)
class Talent(admin.ModelAdmin):
    list_display = ('phone_number', 'gender', 'ethnicity', 'age', 'weight', 'height', 'email')
    list_filter = ( 'email', 'age', 'gender')
    search_fields = ('email', 'age', 'gender')


@admin.register(Talent_Ethnicity)
class Talent_Ethnicity(admin.ModelAdmin):
    list_display = ('ethnicity',)
    list_filter = ('ethnicity',)
    search_fields = ('ethnicity',)



