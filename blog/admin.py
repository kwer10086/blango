from django.contrib import admin
from blog.models import Tag,Post,Comment,AuthorProfile

# Register your models here.
admin.site.register(Tag)

class PostAdmin(admin.ModelAdmin):
  prepopulated_fields={"slug":("title",)}
  # list_display = ('slug','published_at')
  list_display = ('summary','title','author')


admin.site.register(Post,PostAdmin)
admin.site.register(Comment)
admin.site.register(AuthorProfile)