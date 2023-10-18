from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import SliderContent


class SliderAdmin(admin.ModelAdmin):
    list_display = ('slider_title', 'slider_text', 'slider_css', 'get_img')
    list_display_links = ('slider_title',)
    list_editable = ('slider_css',)

    fields = ('slider_title', 'slider_text', 'slider_css', 'slider_img', 'get_img')
    readonly_fields = ('get_img',)

    def get_img(self, obj):
        if obj.slider_img:
            return mark_safe(f'<img src="{obj.slider_img.url}" width="80px"')
        else:
            return 'image NOT found'

    get_img.short_description = 'Attachment'


admin.site.register(SliderContent, SliderAdmin)
