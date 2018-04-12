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

import mock
import unittest2

from openstack import profile
from rackspace import connection


class TestConnection(unittest2.TestCase):

    @mock.patch.object(profile.Profile, 'set_region')
    def test_with_region(self, mock_set_region):
        region = "BEN"

        connection.Connection(region=region,
                              username="test", api_key="test")

        mock_set_region.assert_called_with(profile.Profile.ALL, region)

    @mock.patch("rackspaceauth.v2.APIKey")
    def test_auth_with_APIKey(self, mock_apikey):
        user = "brian"
        api_key = "123"

        connection.Connection(region="the moon", username=user,
                              api_key=api_key)

        mock_apikey.assert_called_with(username=user, api_key=api_key)

    @mock.patch("rackspaceauth.v2.Password")
    def test_auth_with_Password(self, mock_password):
        user = "walter"
        password = "123"

        connection.Connection(region="the moon", username=user,
                              password=password)

        mock_password.assert_called_with(username=user, password=password)

    @mock.patch("rackspaceauth.v2.Token")
    def test_auth_with_Token(self, mock_token):
        tenant = "everett"
        token = "123"

        connection.Connection(region="the moon", tenant_id=tenant,
                              token=token)

        mock_token.assert_called_with(tenant_id=tenant, token=token)

    def test_auth_no_user_or_tenant(self):
        self.assertRaisesRegexp(ValueError,
                                "username or tenant_id must be specified",
                                connection.Connection, region="test")

    def test_auth_user_and_tenant(self):
        self.assertRaisesRegexp(
            ValueError,
            "username and tenant_id cannot be used together",
            connection.Connection, username="test", tenant_id="test",
            region="test")

    def test_auth_user_only(self):
        self.assertRaisesRegexp(
            ValueError,
            "Either api_key or password must be passed with username",
            connection.Connection, username="test", region="test")
