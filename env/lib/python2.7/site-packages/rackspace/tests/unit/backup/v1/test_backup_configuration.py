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

from rackspace.backup.v1 import backup_configuration


EXAMPLE = {
    "BackupConfigurationId": 148325,
    "MachineAgentId": 156953,
    "MachineName": "Web Server",
    "Flavor": "RaxCloudServer",
    "IsEncrypted": 'false',
    "BackupConfigurationName": "Weekly Website Backup",

    "IsActive": 'true',
    "IsDeleted": 'false',
    "VersionRetention": 60,
    "BackupConfigurationScheduleId": 145406,
    "MissedBackupActionId": 1,
    "Frequency": "Weekly",
    "StartTimeHour": 11,
    "StartTimeMinute": 30,
    "StartTimeAmPm": "AM",
    "DayOfWeekId": 4,
    "HourInterval": 'null',
    "TimeZoneId": "Eastern Standard Time",
    "NextScheduledRunTime": "\/Date(1357817400000)\/",
    "LastRunTime": 'null',
    "LastRunBackupReportId": 'null',
    "NotifyRecipients": "raxtestaddress@rackspace.com",
    "NotifySuccess": 'false',
    "NotifyFailure": 'false',
    "Inclusions": [
        {
            "FilePath": "C:\\backed_up_folder",
            "ParentId": 148325,
            "FileItemType": "Folder",
            "FileId": 35000
        },
        {
            "FilePath": "C:\\backup_up_file.txt",
            "ParentId": 148325,
            "FileItemType": "File",
            "FileId": 34999
        }
    ],
    "Exclusions": [
        {
            "FilePath": "C:\\backed_up_folder\\excluded_folder",
            "ParentId": 148325,
            "FileItemType": "Folder",
            "FileId": 35002
        },
        {
            "FilePath": "C:\\backed_up_folder\\excluded_file.txt",
            "ParentId": 148325,
            "FileItemType": "File",
            "FileId": 35001
        }
    ]
}


class TestBackupConfiguration(testtools.TestCase):

    def test_basic(self):
        sot = backup_configuration.BackupConfiguration(EXAMPLE)
        self.assertEqual('BackupConfigurationId', sot.id_attribute)
        self.assertEqual('backup-configuration', sot.base_path)
        self.assertEqual('cloudBackup', sot.service.service_name)
        self.assertTrue(sot.allow_create)
        self.assertTrue(sot.allow_retrieve)
        self.assertTrue(sot.allow_update)
        self.assertTrue(sot.allow_delete)
        self.assertTrue(sot.allow_list)
        self.assertEqual(EXAMPLE['MachineAgentId'], sot.agent_id)
        self.assertEqual(EXAMPLE['Exclusions'], sot.exclusions)
        self.assertEqual(EXAMPLE['Flavor'], sot.flavor)
        self.assertEqual(EXAMPLE['Frequency'], sot.frequency)
        self.assertEqual(EXAMPLE['Inclusions'], sot.inclusions)
        self.assertEqual(EXAMPLE['IsActive'], sot.is_active)
        self.assertEqual(EXAMPLE['IsDeleted'], sot.is_deleted)
        self.assertEqual(EXAMPLE['IsEncrypted'], sot.is_encrypted)
        self.assertEqual(EXAMPLE['StartTimeAmPm'], sot.hour_am_pm_at)
        self.assertEqual(EXAMPLE['HourInterval'], sot.hourly_at)
        self.assertEqual(EXAMPLE['BackupConfigurationName'], sot.name)
        self.assertEqual(EXAMPLE['NotifySuccess'], sot.notify_on_failure)
        self.assertEqual(EXAMPLE['NotifyFailure'], sot.notify_on_success)
        self.assertEqual(EXAMPLE['NotifyRecipients'], sot.notify_to)
        self.assertEqual(EXAMPLE['MissedBackupActionId'], sot.notify_when)
        self.assertEqual(EXAMPLE['VersionRetention'], sot.retention)
        self.assertEqual(EXAMPLE['BackupConfigurationScheduleId'],
                         sot.schedule)
        self.assertEqual(EXAMPLE['DayOfWeekId'], sot.start_day_of_week_at)
        self.assertEqual(EXAMPLE['StartTimeHour'], sot.start_hour_at)
        self.assertEqual(EXAMPLE['StartTimeHour'], sot.start_minute_at)
        self.assertEqual(EXAMPLE['TimeZoneId'], sot.timezone)

    def test_disable(self):
        response = mock.Mock()
        response.body = ''
        sess = mock.Mock()
        sess.post = mock.Mock()
        sess.post.return_value = response
        sot = backup_configuration.BackupConfiguration(EXAMPLE)

        self.assertIsNone(sot.disable(sess))

        body = {"Enable": 'false'}
        url = 'backup-configuration/enable/%s' % sot.id
        sess.post.assert_called_with(url, service=sot.service, json=body)

    def test_enable(self):
        response = mock.Mock()
        response.body = ''
        sess = mock.Mock()
        sess.post = mock.Mock()
        sess.post.return_value = response
        sot = backup_configuration.BackupConfiguration(EXAMPLE)

        self.assertIsNone(sot.enable(sess))

        body = {"Enable": 'true'}
        url = 'backup-configuration/enable/%s' % sot.id
        sess.post.assert_called_with(url, service=sot.service, json=body)
