from django.contrib import admin

# Register your models here.
from .models import Concert

@admin.register(Concert)
class ConcertAdmin(admin.ModelAdmin):
    list_display = ('concert_name', 'duration', 'city', 'date')  # Fields to display in the list view of Concerts
    search_fields = ('concert_name', 'city')  # Fields to enable searching in the admin interface
    list_filter = ('date',)  # Filter options for the list view
    date_hierarchy = 'date'  # Grouping by date in the admin interface


#admin.site.register(Concert)
