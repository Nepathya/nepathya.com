from django.utils.translation import ugettext_lazy as _
from cms.toolbar_pool import toolbar_pool
from cms.toolbar_base import CMSToolbar
from django.core.urlresolvers import reverse
from cms.toolbar.items import Break
from cms.cms_toolbar import ADMIN_MENU_IDENTIFIER, ADMINISTRATION_BREAK


@toolbar_pool.register
class GalleryToolbar(CMSToolbar):
    def populate(self):
        admin_menu = self.toolbar.get_or_create_menu(ADMIN_MENU_IDENTIFIER, )
        position = admin_menu.find_first(Break, identifier=ADMINISTRATION_BREAK)

        # Employee app menu
        menu = admin_menu.get_or_create_menu('gallery-app', _('Gallery'), position=position)
        menu.add_sideframe_item(_('List Albums'), url=reverse('admin:gallery_album_changelist'))
        album_url = reverse('admin:gallery_album_add')
        image_url = reverse('admin:gallery_image_add')
        menu.add_sideframe_item(_('Add album'), url=album_url)
        menu.add_sideframe_item(_('List Images'), url=reverse('admin:gallery_image_changelist'))
        menu.add_sideframe_item(_('Add image'), url=image_url)
        admin_menu.add_break('album-break', position=menu)
