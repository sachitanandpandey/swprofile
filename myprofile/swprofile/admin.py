from django.contrib import admin

from .models import homemsg
from .models import apps
from .models import aboutus, posts

admin.site.register(homemsg)
admin.site.register(apps)
admin.site.register(aboutus)
admin.site.register(posts)

