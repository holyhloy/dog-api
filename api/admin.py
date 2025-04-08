from django.contrib import admin

from api.models import Breed
from api.models import Dog


admin.site.register(Breed)
admin.site.register(Dog)
