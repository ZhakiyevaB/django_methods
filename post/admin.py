from django.contrib import admin
from .models import Post

#admin.site.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')


#from django.contrib import admin 

#from .models import Post, User, Post_delete


#admin.site.register(Post) 
#admin.site.register(Post_delete)
#admin.site.register(User)