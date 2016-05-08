from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


class GalleryAppHook(CMSApp):
    name = "Gallery"
    urls = ["gallery.urls"]


apphook_pool.register(GalleryAppHook)
