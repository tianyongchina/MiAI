# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class MiRequestSessionApplication(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, app_id: str=None):  # noqa: E501
        """MiRequestSessionApplication - a model defined in Swagger

        :param app_id: The app_id of this MiRequestSessionApplication.  # noqa: E501
        :type app_id: str
        """
        self.swagger_types = {
            'app_id': str
        }

        self.attribute_map = {
            'app_id': 'app_id'
        }

        self._app_id = app_id

    @classmethod
    def from_dict(cls, dikt) -> 'MiRequestSessionApplication':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The MiRequest_session_application of this MiRequestSessionApplication.  # noqa: E501
        :rtype: MiRequestSessionApplication
        """
        return util.deserialize_model(dikt, cls)

    @property
    def app_id(self) -> str:
        """Gets the app_id of this MiRequestSessionApplication.


        :return: The app_id of this MiRequestSessionApplication.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id: str):
        """Sets the app_id of this MiRequestSessionApplication.


        :param app_id: The app_id of this MiRequestSessionApplication.
        :type app_id: str
        """

        self._app_id = app_id
