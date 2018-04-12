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

from rackspace.monitoring.v1 import suppression


EXAMPLE = {
    "id": "spAAAAA",
    "alarms": [],
    "checks": ['en123:ch123'],
    "end_time": 123456789,
    "entities": [],
    "label": "Suppress a bit",
    "notification_plans": ['npfooBar'],
    "start_time": 123456789
}


class TestSuppression(testtools.TestCase):
    def test_basic(self):
        sot = suppression.Suppression()
        self.assertEqual('values', sot.resources_key)
        self.assertEqual('suppressions', sot.base_path)
        self.assertEqual("cloudMonitoring", sot.service.service_name)
        self.assertTrue(sot.allow_create)
        self.assertTrue(sot.allow_delete)
        self.assertTrue(sot.allow_list)
        self.assertTrue(sot.allow_retrieve)
        self.assertTrue(sot.allow_update)

    def test_make_it(self):
        sot = suppression.Suppression(EXAMPLE)
        self.assertEqual(EXAMPLE['alarms'], sot.alarms)
        self.assertEqual(EXAMPLE['checks'], sot.checks)
        self.assertEqual(EXAMPLE['end_time'], sot.ends_at)
        self.assertEqual(EXAMPLE['entities'], sot.entities)
        self.assertEqual(EXAMPLE['label'], sot.name)
        self.assertEqual(EXAMPLE['notification_plans'], sot.notification_plans)
        self.assertEqual(EXAMPLE['start_time'], sot.starts_at)
