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
from openstack import exceptions
from openstack.tests.unit.auth import common
import testtools

from rackspace.auth.identity import rackspace

TEST_SERVICE_CATALOG = common.TEST_SERVICE_CATALOG_V2
TEST_RESPONSE_DICT = common.TEST_RESPONSE_DICT_V2


class TestRackspaceAuth(testtools.TestCase):

    def test_password(self):
        kargs = {
            "password": common.TEST_PASS,
            "username": common.TEST_USER,
        }

        sot = rackspace.Password(**kargs)

        self.assertEqual(common.TEST_USER, sot.username)
        self.assertEqual(common.TEST_PASS, sot.password)
        expected = {"passwordCredentials": {"password": common.TEST_PASS,
                                            "username": common.TEST_USER}}
        headers = {}
        self.assertEqual(expected, sot.get_auth_data(headers))
        self.assertEqual({}, headers)

    def test_api_key(self):
        kargs = {
            "api_key": common.TEST_PASS,
            "username": common.TEST_USER,
        }

        sot = rackspace.Password(**kargs)

        self.assertEqual(common.TEST_USER, sot.username)
        self.assertEqual(common.TEST_PASS, sot.api_key)
        expected = {"RAX-KSKEY:apiKeyCredentials":
                    {"apiKey": common.TEST_PASS,
                     "username": common.TEST_USER}}
        headers = {}
        self.assertEqual(expected, sot.get_auth_data(headers))
        self.assertEqual({}, headers)

    def test_empty_token(self):
        kargs = {
            "token": "",
            "tenant_id": common.TEST_TENANT_ID,
        }

        with testtools.ExpectedException(exceptions.AuthorizationFailure):
            rackspace.Token(**kargs)

    def test_token_with_tenant_id(self):
        kargs = {
            "tenant_id": common.TEST_TENANT_ID,
            "token": common.TEST_TOKEN,
        }
        expected = {"tenantId": common.TEST_TENANT_ID,
                    "token": {"id": common.TEST_TOKEN}}
        sot = self._test_token(kargs, expected)
        self.assertEqual(common.TEST_TENANT_ID, sot.tenant_id)

    def test_token_with_tenant_name(self):
        kargs = {
            "tenant_name": common.TEST_TENANT_NAME,
            "token": common.TEST_TOKEN,
        }
        expected = {"tenantName": common.TEST_TENANT_NAME,
                    "token": {"id": common.TEST_TOKEN}}
        sot = self._test_token(kargs, expected)
        self.assertEqual(common.TEST_TENANT_NAME, sot.tenant_name)

    def _test_token(self, kargs, expected):
        sot = rackspace.Token(**kargs)

        self.assertEqual(common.TEST_TOKEN, sot.token)
        headers = {}
        self.assertEqual(expected, sot.get_auth_data(headers))
        return sot

    def create_mock_transport(self, xresp):
        transport = mock.Mock()
        transport.post = mock.Mock()
        response = mock.Mock()
        response.json = mock.Mock()
        response.json.return_value = xresp
        transport.post.return_value = response
        return transport

    def test_authorize_tenant_id(self):
        kargs = {
            "tenant_id": common.TEST_TENANT_ID,
            "token": common.TEST_TOKEN,
        }
        sot = rackspace.Token(**kargs)
        xport = self.create_mock_transport(TEST_RESPONSE_DICT)

        resp = sot.authorize(xport)

        eurl = rackspace.AUTH_URL.rstrip("/") + "/tokens"
        eheaders = {"Accept": "application/json"}
        ejson = {"auth": {"token": {"id": common.TEST_TOKEN},
                          "tenantId": common.TEST_TENANT_ID}}
        xport.post.assert_called_with(eurl, headers=eheaders, json=ejson)
        ecatalog = TEST_RESPONSE_DICT["access"].copy()
        ecatalog["version"] = "v2.0"
        self.assertEqual(ecatalog, resp._info)

    def test_authorize_tenant_name(self):
        kargs = {
            "tenant_name": common.TEST_TENANT_NAME,
            "token": common.TEST_TOKEN,
        }
        sot = rackspace.Token(**kargs)
        xport = self.create_mock_transport(TEST_RESPONSE_DICT)

        resp = sot.authorize(xport)

        eurl = rackspace.AUTH_URL.rstrip("/") + "/tokens"
        eheaders = {"Accept": "application/json"}
        ejson = {"auth": {"token": {"id": common.TEST_TOKEN},
                          "tenantName": common.TEST_TENANT_NAME}}
        xport.post.assert_called_with(eurl, headers=eheaders, json=ejson)
        ecatalog = TEST_RESPONSE_DICT["access"].copy()
        ecatalog["version"] = "v2.0"
        self.assertEqual(ecatalog, resp._info)

    def test_authorize_bad_response(self):
        kargs = {
            "token": common.TEST_TOKEN,
            "tenant_name": common.TEST_TENANT_NAME
        }
        sot = rackspace.Token(**kargs)
        xport = self.create_mock_transport({})

        with testtools.ExpectedException(exceptions.InvalidResponse):
            sot.authorize(xport)

    def test_invalidate(self):
        kargs = {
            "token": common.TEST_TOKEN,
            "tenant_name": common.TEST_TENANT_NAME,
        }
        sot = rackspace.Token(**kargs)
        expected = {"tenantName": common.TEST_TENANT_NAME,
                    "token": {"id": common.TEST_TOKEN}}
        headers = {}
        self.assertEqual(expected, sot.get_auth_data(headers))

        self.assertEqual(True, sot.invalidate())

        self.assertEqual(None, sot.token)
        self.assertEqual(None, sot.access_info)
