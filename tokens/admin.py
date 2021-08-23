from django.contrib import admin

# Register your models here.
from django.apps import apps


class DynamicColumnAdmin(admin.ModelAdmin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        field_list = [i.name for i in self.model._meta.fields]
        self.list_display = field_list
        self.list_display_links = field_list


my_app = apps.get_app_config("tokens")

for model in list(my_app.get_models()):
    admin.site.register(model, DynamicColumnAdmin)
