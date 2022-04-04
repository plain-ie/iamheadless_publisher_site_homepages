from typing import List, Optional

from django.shortcuts import reverse

from iamheadless_publisher_site.pydantic_models import BaseItemContentsPydanticModel, BaseItemDataPydanticModel, BaseItemPydanticModel

from .conf import settings
from .urls import urlpatterns


class HomepageContentPydanticModel(BaseItemContentsPydanticModel):
    title: str
    language: str
    content: Optional[str]
    seo_keywords: Optional[str]
    seo_description: Optional[str]


class HomepageDataPydanticModel(BaseItemDataPydanticModel):
    contents: List[HomepageContentPydanticModel]


class HomepagePydanticModel(BaseItemPydanticModel):
    _content_model = HomepageContentPydanticModel
    _data_model = HomepageDataPydanticModel
    _display_name_plural = 'homepages'
    _display_name_singular = 'homepage'
    _item_type = 'homepage'
    _searchable = False
    _browsable = True
    _urlpatterns = urlpatterns

    data: HomepageDataPydanticModel

    def get_item_url(self, language):
        return reverse(
            settings.URLNAME_HOMEPAGE,
            kwargs={
                'language': language
            }
        )

    @property
    def CONTENTS(self):
        return self.dict()['data']['contents']
