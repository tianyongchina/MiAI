# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.mi_response_response_to_display_ui_template_item import MiResponseResponseToDisplayUiTemplateItem  # noqa: F401,E501
from swagger_server.models.mi_response_response_to_display_ui_template_items import MiResponseResponseToDisplayUiTemplateItems  # noqa: F401,E501
from swagger_server import util


class MiResponseResponseToDisplayUiTemplate(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, type: int=None, items: MiResponseResponseToDisplayUiTemplateItems=None, item: MiResponseResponseToDisplayUiTemplateItem=None):  # noqa: E501
        """MiResponseResponseToDisplayUiTemplate - a model defined in Swagger

        :param type: The type of this MiResponseResponseToDisplayUiTemplate.  # noqa: E501
        :type type: int
        :param items: The items of this MiResponseResponseToDisplayUiTemplate.  # noqa: E501
        :type items: MiResponseResponseToDisplayUiTemplateItems
        :param item: The item of this MiResponseResponseToDisplayUiTemplate.  # noqa: E501
        :type item: MiResponseResponseToDisplayUiTemplateItem
        """
        self.swagger_types = {
            'type': int,
            'items': MiResponseResponseToDisplayUiTemplateItems,
            'item': MiResponseResponseToDisplayUiTemplateItem
        }

        self.attribute_map = {
            'type': 'type',
            'items': 'items',
            'item': 'item'
        }

        self._type = type
        self._items = items
        self._item = item

    @classmethod
    def from_dict(cls, dikt) -> 'MiResponseResponseToDisplayUiTemplate':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The MiResponse_response_to_display_ui_template of this MiResponseResponseToDisplayUiTemplate.  # noqa: E501
        :rtype: MiResponseResponseToDisplayUiTemplate
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type(self) -> int:
        """Gets the type of this MiResponseResponseToDisplayUiTemplate.


        :return: The type of this MiResponseResponseToDisplayUiTemplate.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type: int):
        """Sets the type of this MiResponseResponseToDisplayUiTemplate.


        :param type: The type of this MiResponseResponseToDisplayUiTemplate.
        :type type: int
        """

        self._type = type

    @property
    def items(self) -> MiResponseResponseToDisplayUiTemplateItems:
        """Gets the items of this MiResponseResponseToDisplayUiTemplate.


        :return: The items of this MiResponseResponseToDisplayUiTemplate.
        :rtype: MiResponseResponseToDisplayUiTemplateItems
        """
        return self._items

    @items.setter
    def items(self, items: MiResponseResponseToDisplayUiTemplateItems):
        """Sets the items of this MiResponseResponseToDisplayUiTemplate.


        :param items: The items of this MiResponseResponseToDisplayUiTemplate.
        :type items: MiResponseResponseToDisplayUiTemplateItems
        """

        self._items = items

    @property
    def item(self) -> MiResponseResponseToDisplayUiTemplateItem:
        """Gets the item of this MiResponseResponseToDisplayUiTemplate.


        :return: The item of this MiResponseResponseToDisplayUiTemplate.
        :rtype: MiResponseResponseToDisplayUiTemplateItem
        """
        return self._item

    @item.setter
    def item(self, item: MiResponseResponseToDisplayUiTemplateItem):
        """Sets the item of this MiResponseResponseToDisplayUiTemplate.


        :param item: The item of this MiResponseResponseToDisplayUiTemplate.
        :type item: MiResponseResponseToDisplayUiTemplateItem
        """

        self._item = item
