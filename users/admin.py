from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Настройки отображения модели User в админ-панели Django."""

    list_display = ("id", "email", "phone_number", "city")
    search_fields = ("email", "phone_number")
