from django.contrib import admin
from .models import DiscussionTopic, Discussions, News, Category, Borderlandspatch

admin.site.register(News)
admin.site.register(Category)
admin.site.register(Borderlandspatch)
admin.site.register(Discussions)
admin.site.register(DiscussionTopic)