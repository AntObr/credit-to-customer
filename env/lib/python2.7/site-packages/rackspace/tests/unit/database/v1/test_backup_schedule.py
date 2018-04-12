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

from openstack.database.v1 import instance
from rackspace.database.v1 import backup_schedule


EXAMPLE = {
    "action": "backup",
    "created": "2014-10-30T12:30:00",
    "day_of_month": 'null',
    "day_of_week": 0,
    "hour": 14,
    "id": "2e351a71-dd28-4bcb-a7d6-d36a5b487173",
    "instance_id": "44b277eb-39be-4921-be31-3d61b43651d7",
    "last_scheduled": 'null',
    "minute": 30,
    "month": 'null',
    "next_run": "2014-11-02T14:30:00",
    "updated": "2014-10-30T12:30:00"
    }


class TestBackupSchedule(testtools.TestCase):
    def test_basic(self):
        sot = backup_schedule.BackupSchedule()
        self.assertEqual('schedules', sot.resources_key)
        self.assertEqual('schedules', sot.base_path)
        self.assertEqual("cloudDatabases", sot.service.service_name)
        self.assertTrue(sot.allow_create)
        self.assertTrue(sot.allow_delete)
        self.assertTrue(sot.allow_list)
        self.assertTrue(sot.allow_retrieve)
        self.assertTrue(sot.allow_update)

    def test_make_it(self):
        sot = backup_schedule.BackupSchedule(EXAMPLE)
        self.assertEqual(EXAMPLE['action'], sot.action)
        self.assertEqual(EXAMPLE['created'], sot.created_at)
        self.assertEqual(EXAMPLE['last_scheduled'], sot.last_run)
        self.assertEqual(EXAMPLE['next_run'], sot.next_run)
        self.assertEqual(type(sot.source_instance), instance.Instance)
        self.assertEqual(EXAMPLE['day_of_month'], sot.start_day_of_month_at)
        self.assertEqual(EXAMPLE['day_of_week'], sot.start_day_of_week_at)
        self.assertEqual(EXAMPLE['hour'], sot.start_hour_at)
        self.assertEqual(EXAMPLE['minute'], sot.start_minute_at)
        self.assertEqual(EXAMPLE['month'], sot.start_month_at)
        self.assertEqual(EXAMPLE['updated'], sot.updated_at)
