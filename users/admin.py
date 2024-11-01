from django.contrib import admin
from users.models import User, CodePhrase


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'email',)
    list_filter = ('email',)


@admin.register(CodePhrase)
class CodePhraseAdmin(admin.ModelAdmin):
    list_display = ('pk', 'company_name', 'codephrase',)
    search_fields = ('company_name',)
