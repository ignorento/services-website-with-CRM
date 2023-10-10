from django.db import models


# Create your models here.
class SliderContent(models.Model):
    slider_img = models.ImageField(upload_to='slider_img/', verbose_name='Image')
    slider_title = models.CharField(max_length=200, verbose_name='Title')
    slider_text = models.CharField(max_length=200, verbose_name='Text')
    slider_css = models.CharField(max_length=200, null=True, default='-', verbose_name='CSS class')

    def __str__(self):
        return self.slider_title

    class Meta:
        verbose_name = 'Slide'
        verbose_name_plural = 'Slides'
