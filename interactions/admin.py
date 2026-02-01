from django.contrib import admin
from .models import Vote, KarmaTransaction

admin.site.register(Vote)
admin.site.register(KarmaTransaction)
