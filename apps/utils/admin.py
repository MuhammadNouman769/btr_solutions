from django.contrib import admin


class BaseAdmin(admin.ModelAdmin):
    list_per_page = 20
    readonly_fields = ("created_at", "updated_at")

    list_filter = ("created_at", "updated_at")
    ordering = ("-created_at",)