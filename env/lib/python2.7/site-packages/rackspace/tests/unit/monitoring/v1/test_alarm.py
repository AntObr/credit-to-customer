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

from rackspace.monitoring.v1 import alarm


FAKE = {
    "values": [
        dict(),
        dict()
    ]
}

EXAMPLE = {
    "active_suppressions": [],
    "check_id": "chAAAA",
    "created_at": 1234567890,
    "criteria": ("if (metric[\"duration\"] >= 2) { return new AlarmStatus(OK);"
                 " } return new AlarmStatus(CRITICAL);"),
    "disabled": "false",
    "entity_id": "enZZZZA",
    "id": "alAAAA",
    "label": "defcon1",
    "timeout": "1234567890",
    "metadata": {"1": "2", "3": "4"},
    "notification_plan_id": "npAAAAA",
    "scheduled_suppressions": [],
    "updated_at": 1234567890
}


class TestAlarm(testtools.TestCase):
    def test_basic(self):
        sot = alarm.Alarm()
        self.assertEqual('values', sot.resources_key)
        self.assertEqual('/entities/%(entity_id)s/alarms', sot.base_path)
        self.assertEqual("cloudMonitoring", sot.service.service_name)
        self.assertTrue(sot.allow_create)
        self.assertTrue(sot.allow_delete)
        self.assertTrue(sot.allow_list)
        self.assertTrue(sot.allow_retrieve)
        self.assertTrue(sot.allow_update)

    def test_make_it(self):
        sot = alarm.Alarm(EXAMPLE)
        self.assertEqual(EXAMPLE['active_suppressions'],
                         sot.active_suppressions)
        self.assertEqual(EXAMPLE['check_id'], sot.check_id)
        self.assertEqual(EXAMPLE['created_at'], sot.created_at)
        self.assertEqual(EXAMPLE['criteria'], sot.criteria)
        self.assertFalse(sot.is_disabled)
        self.assertEqual(EXAMPLE['entity_id'], sot.entity_id)
        self.assertEqual(EXAMPLE['label'], sot.name)
        self.assertEqual(EXAMPLE['metadata'], sot.metadata)
        self.assertEqual(EXAMPLE['notification_plan_id'],
                         sot.notification_plan_id)
        self.assertEqual(EXAMPLE['scheduled_suppressions'],
                         sot.scheduled_suppressions)
        self.assertEqual(EXAMPLE['updated_at'], sot.updated_at)

    def test_notification_history(self):
        sot = alarm.Alarm(EXAMPLE)

        response = mock.Mock()
        response.body = FAKE
        response.json = mock.Mock(return_value=FAKE)

        session = mock.Mock()
        session.get = mock.Mock(return_value=response)
        session.get.json = mock.Mock(return_value=FAKE)

        self.assertEqual(response.body['values'],
                         sot.notification_history(session))

        url = ("entities/%s/alarms/%s/notification_history/%s" % (
               sot.entity_id, sot.id, sot.check_id))
        session.get.assert_called_with(url, endpoint_filter=sot.service)
