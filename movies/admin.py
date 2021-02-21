from django.contrib import admin
from movies.models import Movie, Actor


class ActorAdmin(admin.ModelAdmin):
  fieldsets = [
    (None, {'fields': ['name', 'last_name']}),
  ]
  readonly_fields = ['last_name']


admin.site.register(Actor, ActorAdmin)
admin.site.register(Movie)

# Register your models here.
