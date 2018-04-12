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

from rackspace.monitoring.v1 import suppression_log

EXAMPLE = {
    "id": '5a628ca0-8ca4-11e3-811c-fb1e1c039d36',
    "entity_id": 'enXXXXX',
    "alarm_id": 'alXXXXX',
    "check_id": 'chXXXXX',
    "notification_plan_id": 'npXXXXX',
    "suppressions": ["spXXXX1", "spXXXX2"],
    "state": 'OK',
    "timestamp": 1234567890,
    "transaction_id": ('.rh-Skiy.h-ord1-maas-stage-api1.r-zzTqFcaG'
                       '.c-1553.ts-1391108878406.v-65f8f6c')
}


class TestSuppressionLog(testtools.TestCase):
    def test_basic(self):
        sot = suppression_log.SuppressionLog()
        self.assertEqual('values', sot.resources_key)
        self.assertEqual('suppression_logs', sot.base_path)
        self.assertEqual("cloudMonitoring", sot.service.service_name)
        self.assertFalse(sot.allow_create)
        self.assertFalse(sot.allow_delete)
        self.assertTrue(sot.allow_list)
        self.assertFalse(sot.allow_retrieve)
        self.assertFalse(sot.allow_update)

    def test_make_it(self):
        sot = suppression_log.SuppressionLog(EXAMPLE)
        self.assertEqual(EXAMPLE['id'], sot.id)
        self.assertEqual(EXAMPLE['alarm_id'], sot.alarm_id)
        self.assertEqual(EXAMPLE['check_id'], sot.check_id)
        self.assertEqual(EXAMPLE['entity_id'], sot.entity_id)
        self.assertEqual(
            EXAMPLE['notification_plan_id'], sot.notification_plan_id)
        self.assertEqual(EXAMPLE['state'], sot.status)
        self.assertEqual(EXAMPLE['suppressions'], sot.suppressions)
        self.assertEqual(EXAMPLE['timestamp'], sot.timestamp)
        self.assertEqual(EXAMPLE['transaction_id'], sot.transaction)
