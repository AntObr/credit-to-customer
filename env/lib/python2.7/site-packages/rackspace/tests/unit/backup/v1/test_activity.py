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

from rackspace.backup.v1 import activity

EXAMPLE = {
    "ID": 137987,
    "Type": "Backup",
    "ParentId": 162423,
    "DisplayName": "Weekly Website Backup",
    "IsBackupConfigurationDeleted": 'false',
    "SourceMachineAgentId": 232180,
    "SourceMachineName": "Web Server",
    "DestinationMachineAgentId": 0,
    "DestinationMachineName": "",
    "CurrentState": "Completed",
    "TimeOfActivity": "\/Date(1359033934000)\/",
    "BackupId": 134332
}


class TestActivity(testtools.TestCase):

    def test_basic(self):
        sot = activity.Activity(EXAMPLE)
        self.assertEqual('ID', sot.id_attribute)
        self.assertEqual('activity', sot.base_path)
        self.assertEqual('cloudBackup', sot.service.service_name)
        self.assertFalse(sot.allow_create)
        self.assertFalse(sot.allow_retrieve)
        self.assertFalse(sot.allow_update)
        self.assertFalse(sot.allow_delete)
        self.assertTrue(sot.allow_list)
        self.assertEqual(EXAMPLE['ParentId'], sot.backup_configuration_id)
        self.assertEqual(EXAMPLE['BackupId'], sot.backup_id)
        self.assertEqual(EXAMPLE['DestinationMachineAgentId'],
                         sot.destination_agent_id)
        self.assertEqual(EXAMPLE['DestinationMachineName'],
                         sot.destination_agent_name)
        self.assertEqual(EXAMPLE['IsBackupConfigurationDeleted'],
                         sot.is_backup_configuration_deleted)
        self.assertEqual(EXAMPLE['DisplayName'], sot.name)
        self.assertEqual(EXAMPLE['SourceMachineAgentId'], sot.source_agent_id)
        self.assertEqual(EXAMPLE['SourceMachineName'], sot.source_agent_name)
        self.assertEqual(EXAMPLE['CurrentState'], sot.status)
        self.assertEqual(EXAMPLE['TimeOfActivity'], sot.timestamp)
        self.assertEqual(EXAMPLE['Type'], sot.type)
