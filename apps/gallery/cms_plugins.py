from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from gallery.models import AlbumPlugin, Image
from django.contrib import admin


class ImageInlineAdmin(admin.StackedInline):
    model = Image


class AlbumPlugin(CMSPluginBase):
    name = u'AlbumPlugin'
    model = AlbumPlugin
    render_template = "_hello_plugin.html"
    inlines = (ImageInlineAdmin,)

plugin_pool.register_plugin(AlbumPlugin)
