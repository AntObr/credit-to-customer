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

from rackspace.monitoring.v1 import monitoring_zone


EXAMPLE = {
    "id": "mzdfw",
    "label": "Dallas Fort Worth (DFW)",
    "country_code": "US",
    "source_ips": [
        "1234:5678:1234:5678::/64",
        "1.2.3.4/26"
    ]
}


class TestMonitoringZone(testtools.TestCase):
    def test_basic(self):
        sot = monitoring_zone.MonitoringZone()
        self.assertEqual('values', sot.resources_key)
        self.assertEqual('monitoring_zones', sot.base_path)
        self.assertEqual("cloudMonitoring", sot.service.service_name)
        self.assertFalse(sot.allow_create)
        self.assertFalse(sot.allow_delete)
        self.assertTrue(sot.allow_list)
        self.assertTrue(sot.allow_retrieve)
        self.assertFalse(sot.allow_update)

    def test_make_it(self):
        sot = monitoring_zone.MonitoringZone(EXAMPLE)
        self.assertEqual(EXAMPLE['country_code'], sot.country)
        self.assertEqual(EXAMPLE['label'], sot.name)
        self.assertEqual(EXAMPLE['source_ips'], sot.source_ip_addresses)

    def test_traceroute(self):
        sot = monitoring_zone.MonitoringZone(EXAMPLE)

        fake = {"result": [
            {
                "number": 1,
                "rtts": [3.025, 3.116, 3.189],
                "ip": "50.57.208.106"
            },
            {
                "number": 2,
                "rtts": [0.675, 0.943, 1.083],
                "ip": "50.56.6.34"
            }]
        }

        fake_target = '1.2.3.4'
        fake_target_resolver = 'IPv4'
        fake_body = {"target": fake_target,
                     "target_resolver": fake_target_resolver}

        response = mock.Mock()
        response.body = fake
        response.json = mock.Mock(return_value=fake)

        session = mock.Mock()
        session.post = mock.Mock(return_value=response)
        session.post.json = mock.Mock(return_value=fake)

        self.assertEqual(response.body['result'], sot.traceroute(
            session, fake_target, fake_target_resolver))

        url = ("monitoring_zones/%s/traceroute" % sot.id)
        session.post.assert_called_with(
            url, endpoint_filter=sot.service, json=fake_body)
