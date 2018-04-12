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

from openstack.database.v1 import instance
from rackspace.database.v1 import backup


EXAMPLE = {
    "status": "COMPLETED",
    "updated": "2015-09-01T03:23:36Z",
    "description": "My standalone instance backup1",
    "datastore": {
        "version": "5.6",
        "type": "percona",
        "version_id": "c9760c5b-5675-4482-b097-dffdf50c22ab"
    },
    "id": "61f12fef-edb1-4561-8122-e7c00ef26a82",
    "size": 0.18,
    "is_automated": 0,
    "name": "test_instance-backup",
    "parent_id": "null",
    "created": "2015-09-01T03:23:28Z",
    "flavor_ram": 1024,
    "instance_id": "f4aaba46-fb5f-4316-988d-88da77759968",
    "source": {
          "type": "instance",
          "id": "f4aaba46-fb5f-4316-988d-88da77759968"
    },
    "locationRef": ("https://snet-storage101.dfw1.clouddrive.com/v1/"
                    "MossoCloudFS_938359/z_CLOUDDB_BACKUPS/"
                    "d9f56b04-e17d-41f0-ae92-30a3b47b8d29.xbstream.gz"),
    "type": "InnoBackupEx",
    "volume_size": 1
}


class TestBackup(testtools.TestCase):
    def test_basic(self):
        sot = backup.Backup()
        self.assertEqual('backups', sot.resources_key)
        self.assertEqual('backups', sot.base_path)
        self.assertEqual("cloudDatabases", sot.service.service_name)
        self.assertTrue(sot.allow_create)
        self.assertTrue(sot.allow_delete)
        self.assertTrue(sot.allow_list)
        self.assertTrue(sot.allow_retrieve)
        self.assertFalse(sot.allow_update)

    def test_make_it(self):
        sot = backup.Backup(EXAMPLE)
        self.assertEqual(EXAMPLE['created'], sot.created_at)
        self.assertEqual(EXAMPLE['datastore'], sot.datastore)
        self.assertEqual(EXAMPLE['description'], sot.description)
        self.assertEqual(EXAMPLE['locationRef'], sot.destination)
        self.assertEqual(EXAMPLE['is_automated'], sot.is_automated)
        self.assertEqual(EXAMPLE['name'], sot.name)
        self.assertEqual(EXAMPLE['flavor_ram'], sot.instance_flavor)
        self.assertEqual(type(sot.instance_id), instance.Instance)
        self.assertEqual(EXAMPLE['volume_size'], sot.instance_volume_size)
        self.assertEqual(EXAMPLE['size'], sot.size)
        self.assertEqual(EXAMPLE['source'], sot.source)
        self.assertEqual(EXAMPLE['status'], sot.status)
        self.assertEqual(EXAMPLE['type'], sot.type)
        self.assertEqual(EXAMPLE['updated'], sot.updated_at)

    def test_restore(self):
        response = mock.Mock()
        response.body = {'instance': None}
        sess = mock.Mock()
        sess.post = mock.Mock()
        sess.post.return_value = response
        sot = backup.Backup(EXAMPLE)

        self.assertIsNone(sot.restore(sess))

        body = {"instance": {"restorePoint": {"backupRef": sot.id}}}
        url = 'instances'
        sess.post.assert_called_with(url, service=sot.service, json=body)
