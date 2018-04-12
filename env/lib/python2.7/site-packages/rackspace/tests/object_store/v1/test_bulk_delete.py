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

from rackspace.object_store.v1 import bulk_delete

BODY = {
    "Number Not Found": 100,
    "Response Status": "200 OK",
    "Errors": ["damn, i'm thirsty"],
    "Number Deleted": 81,
    "Response Body": "tell me a story"
}


class TestBulkDelete(testtools.TestCase):

    def setUp(self):
        super(TestBulkDelete, self).setUp()
        self.resp = mock.Mock()
        self.resp.body = BODY
        self.sess = mock.Mock()
        self.sess.delete = mock.MagicMock()
        self.sess.delete.return_value = self.resp

    def test_basic(self):
        sot = bulk_delete.BulkDelete(BODY)
        self.assertIsNone(sot.resource_key)
        self.assertIsNone(sot.resources_key)
        self.assertEqual("/?bulk-delete", sot.base_path)
        self.assertTrue(sot.allow_delete)
        self.assertFalse(sot.allow_create)
        self.assertFalse(sot.allow_update)
        self.assertFalse(sot.allow_retrieve)
        self.assertFalse(sot.allow_list)
        self.assertFalse(sot.allow_head)

    def test_make_it(self):
        sot = bulk_delete.BulkDelete(BODY)
        self.assertEqual(BODY["Number Not Found"], sot.not_found)
        self.assertEqual(BODY["Response Status"], sot.response_code)
        self.assertEqual(BODY["Errors"], sot.errors)
        self.assertEqual(BODY["Number Deleted"], sot.deleted)
        self.assertEqual(BODY["Response Body"], sot.response_body)

    def test_delete(self):
        sot = bulk_delete.BulkDelete()
        diplomats = "\n".join(["/Cam", "/Juelz", "/Jimmy", "/Freeky"])
        result = sot.delete(self.sess, diplomats)

        self.assertEqual(result, bulk_delete.BulkDelete(BODY))
