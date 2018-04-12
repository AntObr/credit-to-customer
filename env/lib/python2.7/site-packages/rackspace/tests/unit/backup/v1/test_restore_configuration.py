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

from rackspace.backup.v1 import restore_configuration

EXAMPLE = {
    "RestoreId": 1394,
    "BackupId": 133599,
    "DestinationMachineId": 156751,
    "OverwriteFiles": 'false',
    "BackupConfigurationId": 6265,
    "BackupConfigurationName": "Restore_Backup",
    "BackupRestorePoint": "\/Date(1357151359000)\/",
    "BackupMachineId": 5,
    "MachineAgentId": 213564,
    "BackupMachineName": "BALAJIMBP",
    "BackupFlavor": "RaxCloudServer",
    "DestinationMachineName": "BILLS-TEST-WIN",
    "DestinationPath": "C:\\FolderPathForRestore\\",
    "BackupDataCenter": "DFW",
    "IsEncrypted": 'false',
    "EncryptedPassword": 'null',
    "PublicKey": {
        "ModulusHex": "CA759606B13DC5350A3FAE3F851C76F260DC ...",
        "ExponentHex": 10001
    },
    "RestoreStateId": 0,
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


class TestRestoreConfiguration(testtools.TestCase):

    def test_basic(self):
        sot = restore_configuration.RestoreConfiguration(EXAMPLE)
        self.assertEqual('BackupId', sot.id_attribute)
        self.assertEqual('restore', sot.base_path)
        self.assertEqual('cloudBackup', sot.service.service_name)
        self.assertTrue(sot.allow_create)
        self.assertFalse(sot.allow_retrieve)
        self.assertTrue(sot.allow_update)
        self.assertFalse(sot.allow_delete)
        self.assertFalse(sot.allow_list)
        self.assertEqual(EXAMPLE['MachineAgentId'], sot.agent_id)
        self.assertEqual(EXAMPLE['BackupMachineName'], sot.agent_name)
        self.assertEqual(EXAMPLE['BackupConfigurationId'],
                         sot.backup_configuration_id)
        self.assertEqual(EXAMPLE['BackupConfigurationName'],
                         sot.backup_configuration_name)
        self.assertEqual(EXAMPLE['BackupId'], sot.backup_id)
        self.assertEqual(EXAMPLE['OverwriteFiles'], sot.can_overwrite)
        self.assertEqual(EXAMPLE['BackupDataCenter'], sot.datacenter)
        self.assertEqual(EXAMPLE['DestinationMachineId'],
                         sot.destination_agent_id)
        self.assertEqual(EXAMPLE['DestinationMachineName'],
                         sot.destination_agent_name)
        self.assertEqual(EXAMPLE['DestinationPath'],
                         sot.destination_path)
        self.assertEqual(EXAMPLE['EncryptedPassword'], sot.encrypted_password)
        self.assertEqual(EXAMPLE['Exclusions'], sot.exclusions)
        self.assertEqual(EXAMPLE['BackupFlavor'], sot.flavor)
        self.assertEqual(EXAMPLE['Inclusions'], sot.inclusions)
        self.assertEqual(EXAMPLE['IsEncrypted'], sot.is_encrypted)
        self.assertEqual(EXAMPLE['PublicKey'], sot.public_key)
        self.assertEqual(EXAMPLE['RestoreId'], sot.restore_id)
        self.assertEqual(EXAMPLE['BackupMachineId'], sot.source_agent_id)
        self.assertEqual(EXAMPLE['RestoreStateId'], sot.status)
        self.assertEqual(EXAMPLE['BackupRestorePoint'], sot.timestamp)
