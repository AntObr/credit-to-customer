# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

"""
Rackspace authorization plugins.
"""

import logging

# NOTE: The following two lines disable warning messages coming out of the
# urllib3 that is vendored by requests. This is currently necessary to
# silence a warning about an issue with the certificate in our identity
# environment. The certificate is missing a subjectAltName, and urllib3
# is warning that the fallback to check the commonName is something that is
# soon to be unsupported. The Rackspace Identity team has been working on
# a solution to this issue, and the environment is slated to be upgraded
# by end of year 2015.
import requests
requests.packages.urllib3.disable_warnings()

from openstack.auth.identity import discoverable
from openstack.auth.identity import v2
from openstack import exceptions

_logger = logging.getLogger(__name__)

AUTH_URL = "https://identity.api.rackspacecloud.com/v2.0/"

PASSWORD_OPTIONS = [
    "auth_url",
    "username",
    "api_key",
    "password",
    "tenant_id",
    "project_id",
    "tenant_name",
    "project_name",
    "reauthenticate",
]

TOKEN_OPTIONS = [
    "auth_url",
    "token",
    "tenant_id",
    "project_id",
    "tenant_name",
    "project_name",
    "reauthenticate",
]


class Discoverable(discoverable.Auth):

    #: Valid options for this plugin
    valid_options = list(set(PASSWORD_OPTIONS + TOKEN_OPTIONS))

    def __init__(self, auth_url=AUTH_URL, reauthenticate=True,
                 project_id=None, tenant_id=None,
                 project_name=None, tenant_name=None, **auth_args):
        """Construct an Identity Authentication Plugin.

        This authorization plugin should be constructed with an auth_url
        and everything needed by either a v2 or v3 identity plugin.

        :param string auth_url: Identity service endpoint for authentication.

        :raises TypeError: if a user_id, username or token is not provided.
        """
        if not auth_url:
            msg = ("The authorization URL auth_url was not provided.")
            raise exceptions.AuthorizationFailure(msg)

        self.auth_url = auth_url
        self.access_info = None
        self.reauthenticate = reauthenticate

        self.tenant_id = project_id
        if not self.tenant_id:
            self.tenant_id = tenant_id
        self.tenant_name = project_name
        if not self.tenant_name:
            self.tenant_name = tenant_name

        if auth_args.get('token'):
            plugin = Token
        else:
            plugin = Password

        valid_list = plugin.valid_options
        args = dict((n, auth_args[n]) for n in valid_list if n in auth_args)
        self.auth_plugin = plugin(auth_url, **args)


class Auth(v2.Auth):

    def invalidate(self):
        """Invalidate the current authentication data."""
        if super(Auth, self).invalidate():
            self.token = None
            self.access_info = None
            return True
        return False


class Password(Auth):

    #: Valid options for Password plugin
    valid_options = PASSWORD_OPTIONS

    def __init__(self, auth_url=AUTH_URL, username=None, password="",
                 api_key="", **kwargs):
        """A plugin for authenticating with a user_name and password.

        A user_name or user_id must be provided.

        :param string auth_url: Identity service endpoint for authorization.
                                This defaults to AUTH_URL
        :param string username: Username for authentication
        :param string password: Password for authentication
        :param string api_key: API Key for authentication
        :param string tenant_id: Tenant ID for tenant scoping
        :param string tenant_name: Tenant name for tenant scoping
        :param bool reauthenticate: Allow fetching a new token if the
                                    current one is going to expire.
                                    (optional) default True

        :raises: ValueError if the username is ``None`` or if both a
                 ``tenant_name`` and ``tenant_id`` are specified.
        """
        super(Password, self).__init__(auth_url=auth_url, **kwargs)

        if username is None:
            raise exceptions.AuthorizationFailure(
                "You must specify a username")

        self.username = username
        self.password = password
        self.api_key = api_key

    def get_auth_data(self, headers=None):
        """Identity v2 token authentication data."""

        if self.password:
            return {"passwordCredentials": {
                    "username": self.username, "password": self.password}}
        elif self.api_key:
            return {"RAX-KSKEY:apiKeyCredentials": {
                    "username": self.username, "apiKey": self.api_key}}


class Token(Auth):

    #: Valid options for Token plugin
    valid_options = TOKEN_OPTIONS

    def __init__(self, auth_url=AUTH_URL, token=None, **kwargs):
        """A plugin for authenticating with an existing token.

        :param string auth_url: Identity service endpoint for authorization.
        :param string token: Existing token for authentication.
        :param string tenant_id: Tenant ID for tenant scoping.
        :param string tenant_name: Tenant name for tenant scoping.
        :param bool reauthenticate: Allow fetching a new token if the current
                                    one is going to expire.
                                    (optional) default True
        """
        super(Token, self).__init__(auth_url=auth_url, **kwargs)

        if not token:
            raise exceptions.AuthorizationFailure("You must specify a token")

        if all([self.tenant_name, self.tenant_id]):
            raise exceptions.AuthorizationFailure(
                "You cannot specify both a tenant_name and tenant_id")

        self.token = token

    def get_auth_data(self, headers=None):
        data = {"token": {"id": self.token}}

        if self.tenant_id:
            data["tenantId"] = self.tenant_id
        elif self.tenant_name:
            data["tenantName"] = self.tenant_name

        return data
