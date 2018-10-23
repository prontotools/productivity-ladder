from django.contrib import admin

from contributors.models import Commit, Contributor


@admin.register(Contributor)
class ContributorAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'username',
        'name',
    )
    list_per_page = 30
    search_fields = ('username',)


@admin.register(Commit)
class CommitAdmin(admin.ModelAdmin):
    list_display = (
        'repositories',
        'contributors',
        'count',
        'date_committed',
    )
    search_fields = ('repositories', 'contributors', 'date_committed')
    list_per_page = 30
