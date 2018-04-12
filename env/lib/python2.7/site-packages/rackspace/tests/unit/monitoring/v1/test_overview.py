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

from rackspace.monitoring.v1 import overview

EXAMPLE = {
    "alarms": [{
        "id": "alThree",
        "check_id": "chFour",
        "criteria": "if (metric[\"size\"] >= 200) { return new Alarm...",
        "notification_plan_id": "npOne"}],
    "entity": {
        "id": "enBBBBIPV4",
        "label": "entity b v4",
        "ip_addresses": {"default": "127.0.0.1"},
        "metadata": "null"},
    "checks": [{
        "id": "chFour",
        "label": "ch a",
        "type": "remote.http",
        "details": {"url": "http://www.foo.com", "method": "GET"},
        "monitoring_zones_poll": ["mzA"],
        "timeout": 30,
        "period": 60,
        "target_alias": "default",
        "target_hostname": "",
        "target_resolver": "",
        "disabled": "false"}],
    "latest_alarm_states": [{
        "timestamp": 1321898988,
        "entity_id": "enBBBBIPV4",
        "alarm_id": "alThree",
        "check_id": "chFour",
        "status": "everything is ok",
        "state": "OK",
        "previous_state": "WARNING",
        "analyzed_by_monitoring_zone_id": "null"}]
}


class TestOverview(testtools.TestCase):
    def test_basic(self):
        sot = overview.Overview()
        self.assertEqual('values', sot.resources_key)
        self.assertEqual('/views/overview', sot.base_path)
        self.assertEqual("cloudMonitoring", sot.service.service_name)
        self.assertFalse(sot.allow_create)
        self.assertFalse(sot.allow_delete)
        self.assertTrue(sot.allow_list)
        self.assertFalse(sot.allow_retrieve)
        self.assertFalse(sot.allow_update)

    def test_make_it(self):
        sot = overview.Overview(EXAMPLE)
        self.assertEqual(EXAMPLE['alarms'], sot.alarms)
        self.assertEqual(EXAMPLE['checks'], sot.checks)
        self.assertEqual(EXAMPLE['entity'], sot.entity)
        self.assertEqual(EXAMPLE['latest_alarm_states'],
                         sot.latest_alarm_states)
