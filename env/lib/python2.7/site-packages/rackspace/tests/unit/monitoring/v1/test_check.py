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

from rackspace.monitoring.v1 import check


EXAMPLE = {
    "active_suppressions": [],
    "id": "chAAAA",
    "created_at": 1234567890,
    "label": "Website check 1",
    "type": "remote.http",
    "details": {
        "url": "http://www.foo.com",
        "method": "GET",
        "follow_redirects": "true",
        "include_body": "false"
    },
    "entity_id": "en123456",
    "monitoring_zones_poll": [
        "mzA"
    ],
    "timeout": 30,
    "period": 100,
    "target_alias": "entity_ip_addresses_hash_key",
    "target_hostname": "shouldnotbehere",
    "target_resolver": "ipv4",
    "scheduled_suppressions": [],
    "updated_at": 1234567890
}


class TestCheck(testtools.TestCase):
    def test_basic(self):
        sot = check.Check()
        self.assertEqual('values', sot.resources_key)
        self.assertEqual('/entities/%(entity_id)s/checks', sot.base_path)
        self.assertEqual("cloudMonitoring", sot.service.service_name)
        self.assertTrue(sot.allow_create)
        self.assertTrue(sot.allow_delete)
        self.assertTrue(sot.allow_list)
        self.assertTrue(sot.allow_retrieve)
        self.assertTrue(sot.allow_update)

    def test_make_it(self):
        sot = check.Check(EXAMPLE)
        self.assertEqual(EXAMPLE['active_suppressions'],
                         sot.active_suppressions)
        self.assertEqual(EXAMPLE['created_at'], sot.created_at)
        self.assertEqual(EXAMPLE['details'], sot.details)
        self.assertEqual(EXAMPLE['entity_id'], sot.entity_id)
        self.assertEqual(EXAMPLE['period'], sot.frequency)
        self.assertEqual(EXAMPLE['label'], sot.name)
        self.assertEqual(EXAMPLE['monitoring_zones_poll'],
                         sot.monitoring_zones)
        self.assertEqual(EXAMPLE['scheduled_suppressions'],
                         sot.scheduled_suppressions)
        self.assertEqual(EXAMPLE['type'], sot.type_id)
        self.assertEqual(EXAMPLE['target_alias'], sot.target_alias)
        self.assertEqual(EXAMPLE['target_hostname'], sot.target_hostname)
        self.assertEqual(EXAMPLE['target_resolver'], sot.target_resolver)
        self.assertEqual(EXAMPLE['timeout'], sot.timeout)
        self.assertEqual(EXAMPLE['updated_at'], sot.updated_at)

    def test_metrics(self):
        sot = check.Check(EXAMPLE)
        fake = {"values": [dict(), dict()]}

        response = mock.Mock()
        response.body = fake
        response.json = mock.Mock(return_value=fake)

        session = mock.Mock()
        session.get = mock.Mock(return_value=response)
        session.get.json = mock.Mock(return_value=fake)

        self.assertEqual(response.body['values'], sot.metrics(session))

        url = ("entities/%s/checks/%s/metrics" % (sot.entity_id, sot.id))
        session.get.assert_called_with(url, endpoint_filter=sot.service)

    def test_test(self):
        sot = check.Check(EXAMPLE)
        fake = {"values": [dict(), dict()]}

        response = mock.Mock()
        response.body = fake
        response.json = mock.Mock(return_value=fake)

        session = mock.Mock()
        session.get = mock.Mock(return_value=response)
        session.get.json = mock.Mock(return_value=fake)

        self.assertEqual(response.body, sot.test(session))

        url = ("entities/%s/checks/%s/test" % (sot.entity_id, sot.id))
        session.get.assert_called_with(url, endpoint_filter=sot.service)
