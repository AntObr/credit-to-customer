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

from rackspace.monitoring.v1 import notification_type


EXAMPLE = {
    "id": "email",
    "fields": [{
        "name": "address",
        "description": "Email address to send notifications to",
        "optional": "false"}]
}


class TestAgent(testtools.TestCase):
    def test_basic(self):
        sot = notification_type.NotificationType()
        self.assertEqual('values', sot.resources_key)
        self.assertEqual('notification_types', sot.base_path)
        self.assertEqual("cloudMonitoring", sot.service.service_name)
        self.assertFalse(sot.allow_create)
        self.assertFalse(sot.allow_delete)
        self.assertTrue(sot.allow_list)
        self.assertTrue(sot.allow_retrieve)
        self.assertFalse(sot.allow_update)

    def test_make_it(self):
        sot = notification_type.NotificationType(EXAMPLE)
        self.assertEqual(EXAMPLE['fields'], sot.fields)
