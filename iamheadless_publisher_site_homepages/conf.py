from django.conf import settings as dj_settings

from iamheadless_translate.conf import settings as iamheadless_translate_settings

from .apps import IamheadlessPublisherSiteHomepagesConfig as AppConfig
from .translations import translations


class Settings:

    APP_NAME = AppConfig.name
    VAR_PREFIX = APP_NAME.upper()

    ITEM_TYPE = 'homepage'

    VAR_FOOTER_TEMPLATE = f'{VAR_PREFIX}_FOOTER_TEMPLATE'
    VAR_MAIN_MENU_TEMPLATE = f'{VAR_PREFIX}_MAIN_MENU_TEMPLATE'
    VAR_TEMPLATE = f'{VAR_PREFIX}_TEMPLATE'

    URLNAME_HOMEPAGE = 'site-homepage'

    @property
    def FOOTER_TEMPLATE(self):
        return getattr(
            dj_settings,
            self.VAR_FOOTER_TEMPLATE,
            f'{APP_NAME}/footer.html'
        )

    @property
    def MAIN_MENU_TEMPLATE(self):
        return getattr(
            dj_settings,
            self.VAR_MAIN_MENU_TEMPLATE,
            f'{APP_NAME}/main_menu.html'
        )

    @property
    def TEMPLATE(self):
        return getattr(
            dj_settings,
            self.VAR_TEMPLATE,
            f'{APP_NAME}/item.html'
        )

    def __getattr__(self, name):
        return getattr(dj_settings, name)


settings = Settings()


iamheadless_translate_settings.TRANSLATION_REGISTRY.bulk_register(translations)
