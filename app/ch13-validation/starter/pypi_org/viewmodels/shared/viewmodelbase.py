from typing import Optional

import flask
from flask import Request

# Recall the request_dict unify data across the site into a single place
from pypi_org.infrastructure import request_dict, cookie_auth


class ViewModelBase:
    """ Class created with a flask request, a blank dictionary, an error message and a user id"""
    def __init__(self):
        self.request: Request = flask.request
        self.request_dict = request_dict.create('')

        self.error: Optional[str] = None
        self.user_id: Optional[int] = cookie_auth.get_user_id_via_auth_cookie(self.request)

    def to_dict(self):
        """ Convert from an object to a dictionary"""
        return self.__dict__
