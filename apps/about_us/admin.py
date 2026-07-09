from django.contrib import admin
from .models import Team
from apps.utils.admin import BaseAdmin


@admin.register(Team)
class TeamAdmin(BaseAdmin):
    list_display = (
        "display_order",
        "first_name",
        "last_name",
        "designation",
        "is_active",
        "created_at",
    )

    ordering = ("display_order",)

    search_fields = (
        "first_name",
        "last_name",
        "designation",
    )

    list_filter = (
        "is_active",
        "created_at",
    )

    ordering = ("id",)   # ID ascending (1, 2, 3...)