from django.contrib import admin
from .models import Author, BlogPost

# Enregistrement des modèles dans le panneau d'administration
admin.site.register(Author)
admin.site.register(BlogPost)
