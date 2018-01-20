# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class MiResponseResponseToDisplayWidget(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, info: object=None, params: object=None):  # noqa: E501
        """MiResponseResponseToDisplayWidget - a model defined in Swagger

        :param info: The info of this MiResponseResponseToDisplayWidget.  # noqa: E501
        :type info: object
        :param params: The params of this MiResponseResponseToDisplayWidget.  # noqa: E501
        :type params: object
        """
        self.swagger_types = {
            'info': object,
            'params': object
        }

        self.attribute_map = {
            'info': 'info',
            'params': 'params'
        }

        self._info = info
        self._params = params

    @classmethod
    def from_dict(cls, dikt) -> 'MiResponseResponseToDisplayWidget':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The MiResponse_response_to_display_widget of this MiResponseResponseToDisplayWidget.  # noqa: E501
        :rtype: MiResponseResponseToDisplayWidget
        """
        return util.deserialize_model(dikt, cls)

    @property
    def info(self) -> object:
        """Gets the info of this MiResponseResponseToDisplayWidget.


        :return: The info of this MiResponseResponseToDisplayWidget.
        :rtype: object
        """
        return self._info

    @info.setter
    def info(self, info: object):
        """Sets the info of this MiResponseResponseToDisplayWidget.


        :param info: The info of this MiResponseResponseToDisplayWidget.
        :type info: object
        """

        self._info = info

    @property
    def params(self) -> object:
        """Gets the params of this MiResponseResponseToDisplayWidget.


        :return: The params of this MiResponseResponseToDisplayWidget.
        :rtype: object
        """
        return self._params

    @params.setter
    def params(self, params: object):
        """Sets the params of this MiResponseResponseToDisplayWidget.


        :param params: The params of this MiResponseResponseToDisplayWidget.
        :type params: object
        """

        self._params = params
