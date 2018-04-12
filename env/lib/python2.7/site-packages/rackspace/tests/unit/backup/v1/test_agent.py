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

from rackspace.backup.v1 import agent

DATACENTER = 'LON'
DESTINATION = '654321'
ENCRYPTIONKEY = 'xxxxxxxx'
EXAMPLE = {
    "AgentVersion": "1.05.005848",
    "Architecture": "64-bit",
    "Flavor": "RaxCloudServer",
    "BackupVaultSize": "35.3 MB",
    "BackupContainer": ("https://storage101.DC.clouddrive.com/v1"
                        "/yourAccount/CloudBackup_v2_0_yourUUID"),
    "CleanupAllowed": 'true',
    "Datacenter": DATACENTER,
    "IPAddress": "192.168.1.1",
    "IsDisabled": 'false',
    "IsEncrypted": 'true',
    "MachineAgentId": 213564,
    "MachineName": "Web Server",
    "OperatingSystem": "Windows Server 2012",
    "OperatingSystemVersion": "",
    "PublicKey": {
        "ModulusHex": "a5261939156948bb7a58dffe5ff89e65f0498f9175f5a ...",
        "ExponentHex": "09528"
    },
    "Status": "Online",
    "TimeOfLastSuccessfulBackup": "/Date(1357817400000)/",
    "UseServiceNet": "true",
    "HostServerId":  "87c3b6e1-fb1a-41f9-91e5-313ae35a5a06"
}
NEW_KEY = 'xxxxxxxx'
OLD_KEY = 'yyyyyyyy'
SERVICENET = 'false'


class TestAgent(testtools.TestCase):

    def test_basic(self):
        sot = agent.Agent(EXAMPLE)
        self.assertEqual('MachineAgentId', sot.id_attribute)
        self.assertEqual('/user/agents', sot.base_path)
        self.assertEqual('cloudBackup', sot.service.service_name)
        self.assertFalse(sot.allow_create)
        self.assertTrue(sot.allow_retrieve)
        self.assertFalse(sot.allow_update)
        self.assertTrue(sot.allow_delete)
        self.assertTrue(sot.allow_list)
        self.assertEqual(EXAMPLE['CleanupAllowed'], sot.can_cleanup)
        self.assertEqual(EXAMPLE['BackupContainer'], sot.container)
        self.assertEqual(EXAMPLE['Datacenter'], sot.datacenter)
        self.assertEqual(EXAMPLE['Flavor'], sot.flavor)
        self.assertEqual(EXAMPLE['IsDisabled'], sot.is_disabled)
        self.assertEqual(EXAMPLE['IsEncrypted'], sot.is_encrypted)
        self.assertEqual(EXAMPLE['TimeOfLastSuccessfulBackup'],
                         sot.last_successful_backup_at)
        self.assertEqual(EXAMPLE['PublicKey'], sot.public_key)
        self.assertEqual(EXAMPLE['Architecture'], sot.server_arch)
        self.assertEqual(EXAMPLE['MachineName'], sot.server_name)
        self.assertEqual(EXAMPLE['OperatingSystem'], sot.server_os)
        self.assertEqual(EXAMPLE['OperatingSystemVersion'],
                         sot.server_os_version)
        self.assertEqual(EXAMPLE['IPAddress'], sot.server_ipaddress)
        self.assertEqual(EXAMPLE['HostServerId'], sot.server_uuid)
        self.assertEqual(EXAMPLE['UseServiceNet'], sot.servicenet)
        self.assertEqual(EXAMPLE['Status'], sot.status)
        self.assertEqual(EXAMPLE['BackupVaultSize'], sot.vault_size)
        self.assertEqual(EXAMPLE['AgentVersion'], sot.version)

    def test_disable(self):
        response = mock.Mock()
        response.body = ''
        sess = mock.Mock()
        sess.post = mock.Mock()
        sess.post.return_value = response
        sot = agent.Agent(EXAMPLE)

        self.assertIsNone(sot.disable(sess))

        body = {'MachineAgentId': sot.id, 'Enable': 'false'}
        url = 'agent/enable'
        sess.post.assert_called_with(url, service=sot.service, json=body)

    def test_encrypt_volume(self):
        response = mock.Mock()
        response.body = ''
        sess = mock.Mock()
        sess.post = mock.Mock()
        sess.post.return_value = response
        sot = agent.Agent(EXAMPLE)

        self.assertEqual('', sot.encrypt_volume(sess, ENCRYPTIONKEY))

        body = {'MachineAgentId': sot.id,
                'EncryptedPasswordHex': ENCRYPTIONKEY}
        url = 'agent/encrypt'
        sess.post.assert_called_with(url, service=sot.service, json=body)

    def test_enable(self):
        response = mock.Mock()
        response.body = ''
        sess = mock.Mock()
        sess.post = mock.Mock()
        sess.post.return_value = response
        sot = agent.Agent(EXAMPLE)

        self.assertIsNone(sot.enable(sess))

        body = {'MachineAgentId': sot.id, 'Enable': 'true'}
        url = 'agent/enable'
        sess.post.assert_called_with(url, service=sot.service, json=body)

    def test_migrate_vault(self):
        response = mock.Mock()
        response.body = ''
        sess = mock.Mock()
        sess.post = mock.Mock()
        sess.post.return_value = response
        sot = agent.Agent(EXAMPLE)

        self.assertIsNone(sot.migrate_vault(sess, DESTINATION))

        body = {'SourceMachineAgentId': sot.id,
                'DestinationMachineAgentId': DESTINATION}
        url = 'agent/migratevault'
        sess.post.assert_called_with(url, service=sot.service, json=body)

    def test_update_behavior(self):
        response = mock.Mock()
        response.body = ''
        sess = mock.Mock()
        sess.post = mock.Mock()
        sess.post.return_value = response
        sot = agent.Agent(EXAMPLE)

        self.assertIsNone(sot.update_behavior(sess, DATACENTER, SERVICENET))

        body = {'BackupDataCenter': DATACENTER,
                'UseServiceNet': SERVICENET}
        url = 'agent/%s' % sot.id
        sess.post.assert_called_with(url, service=sot.service, json=body)

    def test_update_encryption_password(self):
        response = mock.Mock()
        response.body = ''
        sess = mock.Mock()
        sess.post = mock.Mock()
        sess.post.return_value = response
        sot = agent.Agent(EXAMPLE)

        self.assertEqual('', sot.update_encryption_password(
            sess, OLD_KEY, NEW_KEY))

        body = {'MachineAgentId': sot.id,
                'OldEncryptedPasswordHex': OLD_KEY,
                'NewEncryptedPasswordHex': NEW_KEY}
        url = 'agent/changeencryption'
        sess.post.assert_called_with(url, service=sot.service, json=body)
