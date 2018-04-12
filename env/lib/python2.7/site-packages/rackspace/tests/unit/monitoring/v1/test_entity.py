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

from rackspace.monitoring.v1 import entity

EXAMPLE = {
    "active_suppressions": [],
    "scheduled_suppressions": [],
    "agent_id": "de305d54-75b4-431b-adb2-eb6b9e546014",
    "created_at": 761601600,
    "updated_at": 761601600,
    "uri": "https://lon.servers.api.rackspacecloud.com/123/servers...",
    "ip_addresses": {},
    "metadata": {},
    "label": "extraterrestrialbiologicalentity",
    "id": "enEBE"
}


class TestEntity(testtools.TestCase):
    def test_basic(self):
        sot = entity.Entity()
        self.assertEqual('values', sot.resources_key)
        self.assertEqual('entities', sot.base_path)
        self.assertEqual("cloudMonitoring", sot.service.service_name)
        self.assertTrue(sot.allow_create)
        self.assertTrue(sot.allow_delete)
        self.assertTrue(sot.allow_list)
        self.assertTrue(sot.allow_retrieve)
        self.assertTrue(sot.allow_update)

    def test_make_it(self):
        sot = entity.Entity(EXAMPLE)
        self.assertEqual(EXAMPLE['active_suppressions'],
                         sot.active_suppressions)
        self.assertEqual(EXAMPLE['agent_id'], sot.agent_id)
        self.assertEqual(EXAMPLE['created_at'], sot.created_at)
        self.assertEqual(EXAMPLE['ip_addresses'], sot.ip_addresses)
        self.assertFalse(sot.is_managed)
        self.assertEqual(EXAMPLE['label'], sot.name)
        self.assertEqual(EXAMPLE['metadata'], sot.metadata)
        self.assertEqual(EXAMPLE['scheduled_suppressions'],
                         sot.scheduled_suppressions)
        self.assertEqual(EXAMPLE['updated_at'], sot.updated_at)
        self.assertEqual(EXAMPLE['uri'], sot.uri)

    def test_alarm_changelog(self):
        sot = entity.Entity(EXAMPLE)
        fake = {"values": [dict(), dict()]}

        response = mock.Mock()
        response.body = fake
        response.json = mock.Mock(return_value=fake)

        session = mock.Mock()
        session.get = mock.Mock(return_value=response)
        session.get.json = mock.Mock(return_value=fake)

        self.assertEqual(response.body['values'], sot.alarm_changelog(session))

        url = ("changelogs/alarms?entityId=%s" % sot.id)
        session.get.assert_called_with(url, endpoint_filter=sot.service)

    def test_test_alarm(self):
        sot = entity.Entity(EXAMPLE)

        fake = {"values": [dict(), dict()]}
        fake_check_data = str()
        fake_criteria = str()
        fake_body = {"criteria": fake_criteria,
                     "check_data": fake_check_data}

        response = mock.Mock()
        response.body = fake
        response.json = mock.Mock(return_value=fake)

        session = mock.Mock()
        session.post = mock.Mock(return_value=response)
        session.post.json = mock.Mock(return_value=fake)

        self.assertEqual(response.body, (
            sot.test_alarm(session, fake_check_data, fake_criteria)))

        url = ("entities/%s/test-alarm" % sot.id)
        session.post.assert_called_with(
            url, service=sot.service, json=fake_body)

    def test_test_new_check(self):
        sot = entity.Entity(EXAMPLE)

        fake = {"values": [dict(), dict()]}
        fake_attributes = dict()

        response = mock.Mock()
        response.body = fake
        response.json = mock.Mock(return_value=fake)

        session = mock.Mock()
        session.post = mock.Mock(return_value=response)
        session.post.json = mock.Mock(return_value=fake)

        self.assertEqual(
            response.body, sot.test_new_check(session, fake_attributes))

        url = ("entities/%s/test-check" % sot.id)
        session.post.assert_called_with(
            url, service=sot.service, json=fake_attributes)
