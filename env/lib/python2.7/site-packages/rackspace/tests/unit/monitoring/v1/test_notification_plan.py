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

import testtools

from rackspace.monitoring.v1 import notification_plan


EXAMPLE = {
    "id": "np2JTlcpCs",
    "label": "Notification Plan 1",
    "critical_state": [],
    "warning_state": [],
    "ok_state": [],
    "active_suppressions": [],
    "scheduled_suppressions": [],
    "created_at": 1405916469945,
    "updated_at": 1405916469945,
    "metadata": {}
}


class TestNotificationPlan(testtools.TestCase):
    def test_basic(self):
        sot = notification_plan.NotificationPlan()
        self.assertEqual('values', sot.resources_key)
        self.assertEqual('notification_plans', sot.base_path)
        self.assertEqual("cloudMonitoring", sot.service.service_name)
        self.assertTrue(sot.allow_create)
        self.assertTrue(sot.allow_delete)
        self.assertTrue(sot.allow_list)
        self.assertTrue(sot.allow_retrieve)
        self.assertTrue(sot.allow_update)

    def test_make_it(self):
        sot = notification_plan.NotificationPlan(EXAMPLE)
        self.assertEqual(EXAMPLE['active_suppressions'],
                         sot.active_suppressions)
        self.assertEqual(EXAMPLE['created_at'], sot.created_at)
        self.assertEqual(EXAMPLE['label'], sot.name)
        self.assertEqual(EXAMPLE['metadata'], sot.metadata)
        self.assertEqual(EXAMPLE['critical_state'], sot.recipients_on_critical)
        self.assertEqual(EXAMPLE['ok_state'], sot.recipients_on_ok)
        self.assertEqual(EXAMPLE['warning_state'], sot.recipients_on_warning)
        self.assertEqual(EXAMPLE['scheduled_suppressions'],
                         sot.scheduled_suppressions)
        self.assertEqual(EXAMPLE['updated_at'], sot.updated_at)
