# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class MiResponseResponseDirectivesTtsItem(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, text: str=None, type: str=None):  # noqa: E501
        """MiResponseResponseDirectivesTtsItem - a model defined in Swagger

        :param text: The text of this MiResponseResponseDirectivesTtsItem.  # noqa: E501
        :type text: str
        :param type: The type of this MiResponseResponseDirectivesTtsItem.  # noqa: E501
        :type type: str
        """
        self.swagger_types = {
            'text': str,
            'type': str
        }

        self.attribute_map = {
            'text': 'text',
            'type': 'type'
        }

        self._text = text
        self._type = type

    @classmethod
    def from_dict(cls, dikt) -> 'MiResponseResponseDirectivesTtsItem':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The MiResponse_response_directives_tts_item of this MiResponseResponseDirectivesTtsItem.  # noqa: E501
        :rtype: MiResponseResponseDirectivesTtsItem
        """
        return util.deserialize_model(dikt, cls)

    @property
    def text(self) -> str:
        """Gets the text of this MiResponseResponseDirectivesTtsItem.


        :return: The text of this MiResponseResponseDirectivesTtsItem.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text: str):
        """Sets the text of this MiResponseResponseDirectivesTtsItem.


        :param text: The text of this MiResponseResponseDirectivesTtsItem.
        :type text: str
        """

        self._text = text

    @property
    def type(self) -> str:
        """Gets the type of this MiResponseResponseDirectivesTtsItem.


        :return: The type of this MiResponseResponseDirectivesTtsItem.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this MiResponseResponseDirectivesTtsItem.


        :param type: The type of this MiResponseResponseDirectivesTtsItem.
        :type type: str
        """

        self._type = type
