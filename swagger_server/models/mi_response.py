# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.mi_response_response import MiResponseResponse  # noqa: F401,E501
from swagger_server import util


class MiResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, version: str=None, session_attributes: object=None, is_session_end: bool=None, response: MiResponseResponse=None):  # noqa: E501
        """MiResponse - a model defined in Swagger

        :param version: The version of this MiResponse.  # noqa: E501
        :type version: str
        :param session_attributes: The session_attributes of this MiResponse.  # noqa: E501
        :type session_attributes: object
        :param is_session_end: The is_session_end of this MiResponse.  # noqa: E501
        :type is_session_end: bool
        :param response: The response of this MiResponse.  # noqa: E501
        :type response: MiResponseResponse
        """
        self.swagger_types = {
            'version': str,
            'session_attributes': object,
            'is_session_end': bool,
            'response': MiResponseResponse
        }

        self.attribute_map = {
            'version': 'version',
            'session_attributes': 'session_attributes',
            'is_session_end': 'is_session_end',
            'response': 'response'
        }

        self._version = version
        self._session_attributes = session_attributes
        self._is_session_end = is_session_end
        self._response = response

    @classmethod
    def from_dict(cls, dikt) -> 'MiResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The MiResponse of this MiResponse.  # noqa: E501
        :rtype: MiResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def version(self) -> str:
        """Gets the version of this MiResponse.


        :return: The version of this MiResponse.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version: str):
        """Sets the version of this MiResponse.


        :param version: The version of this MiResponse.
        :type version: str
        """

        self._version = version

    @property
    def session_attributes(self) -> object:
        """Gets the session_attributes of this MiResponse.


        :return: The session_attributes of this MiResponse.
        :rtype: object
        """
        return self._session_attributes

    @session_attributes.setter
    def session_attributes(self, session_attributes: object):
        """Sets the session_attributes of this MiResponse.


        :param session_attributes: The session_attributes of this MiResponse.
        :type session_attributes: object
        """

        self._session_attributes = session_attributes

    @property
    def is_session_end(self) -> bool:
        """Gets the is_session_end of this MiResponse.


        :return: The is_session_end of this MiResponse.
        :rtype: bool
        """
        return self._is_session_end

    @is_session_end.setter
    def is_session_end(self, is_session_end: bool):
        """Sets the is_session_end of this MiResponse.


        :param is_session_end: The is_session_end of this MiResponse.
        :type is_session_end: bool
        """

        self._is_session_end = is_session_end

    @property
    def response(self) -> MiResponseResponse:
        """Gets the response of this MiResponse.


        :return: The response of this MiResponse.
        :rtype: MiResponseResponse
        """
        return self._response

    @response.setter
    def response(self, response: MiResponseResponse):
        """Sets the response of this MiResponse.


        :param response: The response of this MiResponse.
        :type response: MiResponseResponse
        """

        self._response = response