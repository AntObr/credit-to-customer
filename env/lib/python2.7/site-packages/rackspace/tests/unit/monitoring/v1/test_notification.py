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

from rackspace.monitoring.v1 import notification


EXAMPLE = {
    "id": "ntMANAGED",
    "label": "Rackspace Managed Notification",
    "type": "managed",
    "details": {},
    "created_at": 1424933635956,
    "updated_at": 1424933635956,
    "metadata": {}
}


class TestNotification(testtools.TestCase):
    def test_basic(self):
        sot = notification.Notification()
        self.assertEqual('values', sot.resources_key)
        self.assertEqual('notifications', sot.base_path)
        self.assertEqual("cloudMonitoring", sot.service.service_name)
        self.assertTrue(sot.allow_create)
        self.assertTrue(sot.allow_delete)
        self.assertTrue(sot.allow_list)
        self.assertTrue(sot.allow_retrieve)
        self.assertTrue(sot.allow_update)

    def test_make_it(self):
        sot = notification.Notification(EXAMPLE)
        self.assertEqual(EXAMPLE['created_at'], sot.created_at)
        self.assertEqual(EXAMPLE['details'], sot.details)
        self.assertEqual(EXAMPLE['label'], sot.name)
        self.assertEqual(EXAMPLE['metadata'], sot.metadata)
        self.assertEqual(EXAMPLE['type'], sot.type)
        self.assertEqual(EXAMPLE['updated_at'], sot.updated_at)

    def test_test(self):
        sot = notification.Notification(EXAMPLE)
        fake = {
            "status": "success",
            "message": "Success: Webhook successfully executed"
        }

        response = mock.Mock()
        response.body = fake
        response.json = mock.Mock(return_value=fake)

        session = mock.Mock()
        session.post = mock.Mock(return_value=response)
        session.post.json = mock.Mock(return_value=fake)

        self.assertEqual(response.body, sot.test(session))

        url = ("notifications/%s/test" % sot.id)
        session.post.assert_called_with(url, endpoint_filter=sot.service)
