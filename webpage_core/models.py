from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.template.loader import get_template
from tinymce.models import HTMLField
from model_utils.managers import InheritanceManager
from django.template import Context

class Page(models.Model):
    title = models.CharField(max_length=64, verbose_name=_('Title'))
    html_name = models.CharField(max_length=32, verbose_name=_('HTML Name'))
    order = models.PositiveIntegerField()
    url_name = models.CharField(max_length=64)
    background = models.ImageField(blank=True, null=True, upload_to='images')

    def __unicode__(self):
        return u'%s' % self.title

class Content(models.Model):
    pages = models.ManyToManyField(Page, related_name='contents', blank=True, null=True)
    position = models.PositiveIntegerField()
    is_global = models.BooleanField(default=False)
    objects = InheritanceManager()

    def get_preview_html(self):
        template = self.get_template_from_name(self.get_template_preview_name())
        context = Context(self.get_context(**kwargs))
        return template.render(context)

    def get_html(self, **kwargs):
        template = self.get_template_from_name(self.get_template_name())
        context = Context(self.get_context(**kwargs))
        return template.render(context)

    def get_template_from_name(self, template_name):
        return get_template(template_name)

    def get_template_name(self):
        pass

    def get_template_preview_name(self):
        pass

    def get_context(self, **kwargs):
        pass

class SimpleText(Content):
    title = models.CharField(max_length=64, verbose_name=_('Title'))
    text = HTMLField()

    def get_template_name(self):
        return 'simple_text.html'

    def get_context(self, **kwargs):
        return {'title': self.title, 'text': self.text}

    def __unicode__(self):
        return u'%s-%s' % (self.title, str(self.pages))

class SimpleImageContent(Content):
    image = models.ImageField(blank=True, null=True, upload_to='images')

    def get_template_name(self):
        return 'simple_image.html'

    def get_context(self, **kwargs):
        return {'image': self.image}

    def __unicode__(self):
        return u'%s' % (str(self.pages))

class ImageTextContent(SimpleImageContent):
    title = models.CharField(max_length=64, verbose_name=_('Title'))
    text = HTMLField()

    def get_template_name(self):
        return 'image_text.html'

    def get_context(self, **kwargs):
        return {'title': self.title, 'text': self.text, 'image': self.image}

    def __unicode__(self):
        return u'%s-%s' % (self.title, str(self.pages))
