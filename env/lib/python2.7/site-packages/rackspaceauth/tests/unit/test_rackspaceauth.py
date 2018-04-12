# -*- coding: utf-8 -*-

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

import unittest2

from rackspaceauth import v2


class TestRackspaceauth(unittest2.TestCase):

    def test_apikey(self):
        user = "monterey"
        key = "jack"

        auth = v2.APIKey(username=user, api_key=key)
        data = auth.get_auth_data()

        creds = data["RAX-KSKEY:apiKeyCredentials"]
        self.assertEqual(creds["username"], user)
        self.assertEqual(creds["apiKey"], key)

    def test_password(self):
        user = "sharp"
        password = "cheddar"

        auth = v2.Password(username=user, password=password)
        data = auth.get_auth_data()

        creds = data["passwordCredentials"]
        self.assertEqual(creds["username"], user)
        self.assertEqual(creds["password"], password)

    def test_token(self):
        tenant = "queso"
        token = "fresco"

        auth = v2.Token(tenant_id=tenant, token=token)
        data = auth.get_auth_data()

        self.assertEqual(data["tenantId"], tenant)
        self.assertEqual(data["token"]["id"], token)
