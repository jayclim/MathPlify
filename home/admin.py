from django.contrib import admin
from .models import Problem, GeneratedProblem

# Register your models here.
class ProblemAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'user']

class GeneratedProblemAdmin(admin.ModelAdmin):
    list_display = ['id', 'problem', 'generated']
    

admin.site.register(Problem, ProblemAdmin)
admin.site.register(GeneratedProblem, GeneratedProblemAdmin)