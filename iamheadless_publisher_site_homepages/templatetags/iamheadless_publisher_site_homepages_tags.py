import datetime

from django import template
from django.shortcuts import reverse

from iamheadless_publisher_site.conf import settings as iamheadless_publisher_site_settings
from iamheadless_publisher_site import utils as iamheadless_publisher_site_utils

from ..conf import settings


register = template.Library()


@register.simple_tag
def build_id():
    build_id = getattr(settings, 'BUILD_ID', None)
    if build_id is None:
        build_id = datetime.datetime.now().strftime('%Y%m%d%H%M')
    return build_id


@register.simple_tag
def define(value):
    return value


@register.inclusion_tag(settings.FOOTER_TEMPLATE, takes_context=True)
def footer(context):
    request = context['request']
    return {
        'request': request
    }


@register.inclusion_tag(settings.MAIN_MENU_TEMPLATE, takes_context=True)
def main_menu(context):

    request = context['request']

    language = iamheadless_publisher_site_utils.get_request_language(request)

    home_url_kwargs = {}
    if language is not None:
        home_url_kwargs['language'] = language
    home_url = reverse(settings.URLNAME_HOMEPAGE, kwargs=home_url_kwargs)

    language_links = context.get('language_links', [])

    return {
        'brand_image': None,
        'brand_link': home_url,
        'brand_title': settings.PROJECT_TITLE,
        'language': language,
        'language_links': language_links,
        'request': request,
    }


@register.simple_tag
def project_title():
    return getattr(iamheadless_publisher_site_settings, 'PROJECT_TITLE')


@register.simple_tag
def setting(name):
    return getattr(settings, name)
