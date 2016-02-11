from django.contrib import admin

from simple_history.admin import SimpleHistoryAdmin

from technology_radar import models


admin.site.register(models.Radar)
admin.site.register(models.Blip, SimpleHistoryAdmin)
