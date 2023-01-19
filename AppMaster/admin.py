from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Post)
admin.site.register(Avatar)
admin.site.register(AvatarSuper)
#admin.site.register(UserExt)
admin.site.register(Profile)


