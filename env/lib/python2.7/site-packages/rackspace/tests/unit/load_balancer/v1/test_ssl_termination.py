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
import testtools

from rackspace.load_balancer.v1 import ssl_termination

EXAMPLE = {
    "privateKey": "pk",
    "certificate": "cert",
    "intermediateCertificate": "iCert",
    "enabled": "true",
    "sercureTrafficOnly": "false",
    "securePort": 443,
    "securityProtocols": [1]
}


class TestSSLTermination(testtools.TestCase):

    def test_basic(self):
        sot = ssl_termination.SSLTermination()

        self.assertEqual("sslTermination", sot.resource_key)
        self.assertEqual("/loadbalancers/%(load_balancer_id)s/ssltermination",
                         sot.base_path)
        self.assertEqual("rax:load-balancer", sot.service.service_type)
        self.assertTrue(sot.allow_get)
        self.assertTrue(sot.allow_update)
        self.assertTrue(sot.allow_delete)
        self.assertFalse(sot.allow_create)
        self.assertFalse(sot.allow_list)

    def test_make_it(self):
        sot = ssl_termination.SSLTermination(**EXAMPLE)
        self.assertEqual(EXAMPLE["privateKey"], sot.private_key)
        self.assertEqual(EXAMPLE["certificate"], sot.certificate)
        self.assertEqual(EXAMPLE["intermediateCertificate"],
                         sot.intermediate_certificate)
        self.assertTrue(sot.is_enabled)
        self.assertFalse(sot.only_secure_traffic)
        self.assertEqual(EXAMPLE["securePort"], sot.secure_port)
        self.assertEqual(EXAMPLE["securityProtocols"], sot.security_protocols)

    @mock.patch("openstack.resource2.Resource._prepare_request")
    def test_prepare_request_override(self, base_prepare):
        sot = ssl_termination.SSLTermination()

        sot._prepare_request(requires_id=True, prepend_key=False)
        base_prepare.assert_called_with(requires_id=False, prepend_key=False)

        sot._prepare_request(requires_id=True, prepend_key=True)
        base_prepare.assert_called_with(requires_id=False, prepend_key=True)
