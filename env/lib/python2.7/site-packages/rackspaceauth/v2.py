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
Rackspace identity plugins.
"""

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

from keystoneauth1.identity import v2

AUTH_URL = "https://identity.api.rackspacecloud.com/v2.0/"


class APIKey(v2.Auth):

    def __init__(self, username=None, api_key=None, reauthenticate=True,
                 auth_url=AUTH_URL):
        """A plugin for authenticating with a username and API key

        :param str username: Username to authenticate with
        :param str key: API key to authenticate with
        :param bool reauthenticate: Allow fetching a new token if the current
                                    one is about to expire.
        """
        super(APIKey, self).__init__(auth_url, reauthenticate=reauthenticate)

        self.username = username
        self.api_key = api_key
        self.auth_url = auth_url

    def get_auth_data(self, headers=None):
        return {"RAX-KSKEY:apiKeyCredentials":
                {"username": self.username, "apiKey": self.api_key}}


class Password(v2.Auth):

    def __init__(self, username=None, password=None, reauthenticate=True,
                 auth_url=AUTH_URL):
        """A plugin for authenticating with a username and password

        :param str username: Username to authenticate with
        :param str password: Password to authenticate with
        :param bool reauthenticate: Allow fetching a new token if the current
                                    one is about to expire.
        """
        super(Password, self).__init__(auth_url, reauthenticate=reauthenticate)

        self.username = username
        self.password = password
        self.auth_url = auth_url

    def get_auth_data(self, headers=None):
        return {"passwordCredentials": {
                "username": self.username, "password": self.password}}


class Token(v2.Auth):

    def __init__(self, tenant_id=None, token=None,
                 auth_url=AUTH_URL):
        """A plugin for authenticating with a username and password

        :param str tenant_id: Tenant ID to authenticate with
        :param str token: Token to authenticate with
        """
        super(Token, self).__init__(auth_url=auth_url, reauthenticate=False)

        self.tenant_id = tenant_id
        self.token = token

    def get_auth_data(self, headers=None):
        return {"token": {"id": self.token},
                "tenantId": self.tenant_id}
