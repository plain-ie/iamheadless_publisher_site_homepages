from django.shortcuts import render, reverse, redirect
from django.utils.decorators import method_decorator

from iamheadless_publisher_site import utils as iamheadless_publisher_site_utils
from iamheadless_publisher_site.conf import settings as iamheadless_publisher_site_settings
from iamheadless_publisher_site import decorators as iamheadless_publisher_site_decorators
from iamheadless_publisher_site.viewsets.item import ItemViewSet

from .conf import settings


class HomepageViewSet(ItemViewSet):

    template = settings.TEMPLATE

    @method_decorator(iamheadless_publisher_site_decorators.has_allowed_language(allow_none=True), name='dispatch')
    def get(self, request, language=None):

        if language is None:
            url = reverse(
                settings.URLNAME_HOMEPAGE,
                kwargs={
                    'language': iamheadless_publisher_site_settings.DEFAULT_LANGUAGE[0]
                }
            )
            return redirect(url)

        return render(request, self.get_template(), context=self.get_context())

    def get_context(self):

        context = super().get_context()

        language = iamheadless_publisher_site_utils.get_request_language(self.request)
        languages = iamheadless_publisher_site_settings.LANGUAGES

        language_links = []

        for x in languages:
            language = x[0]
            language_links.append({
                'display_name': x[1],
                'url': reverse(settings.URLNAME_HOMEPAGE, kwargs={'language': language}),
                'language': language
            })

        context['language_links'] = language_links

        return context

    def get_item(self):

        items = self.client.retrieve_items(
            iamheadless_publisher_site_settings.PROJECT_ID,
            item_type=settings.ITEM_TYPE,
        )

        return items['results'][0]
