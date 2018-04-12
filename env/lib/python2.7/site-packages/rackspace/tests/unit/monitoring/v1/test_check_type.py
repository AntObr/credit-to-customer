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

from rackspace.monitoring.v1 import check_type


EXAMPLE = {
    "id": "remote.dns",
    "category": "remote",
    "type": "remote",
    "fields": [
        {
            "name": "port",
            "description": "Port number (default: 53)",
            "optional": "true"
        },
        {
            "name": "query",
            "description": "DNS Query",
            "optional": "false"
        },
        {
            "name": "record_type",
            "description": "DNS Record Type",
            "optional": "false"
        }
    ],
    "supported_platforms": []
}


class TestCheckType(testtools.TestCase):
    def test_basic(self):
        sot = check_type.CheckType()
        self.assertEqual('values', sot.resources_key)
        self.assertEqual('check_types', sot.base_path)
        self.assertEqual("cloudMonitoring", sot.service.service_name)
        self.assertFalse(sot.allow_create)
        self.assertFalse(sot.allow_delete)
        self.assertTrue(sot.allow_list)
        self.assertTrue(sot.allow_retrieve)
        self.assertFalse(sot.allow_update)

    def test_make_it(self):
        sot = check_type.CheckType(EXAMPLE)
        self.assertEqual(EXAMPLE['id'], sot.id)
        self.assertEqual(EXAMPLE['category'], sot.category)
        self.assertEqual(type(sot.fields), type(list()))
        self.assertEqual(EXAMPLE['fields'], sot.fields)
        self.assertEqual(EXAMPLE['supported_platforms'],
                         sot.supported_platforms)
        self.assertEqual(EXAMPLE['type'], sot.type)

    def test_targets(self):
        sot = check_type.CheckType(EXAMPLE)
        fake = {"values": [dict(), dict()]}
        fake_entity_id = '12345678'

        response = mock.Mock()
        response.body = fake
        response.json = mock.Mock(return_value=fake)

        session = mock.Mock()
        session.get = mock.Mock(return_value=response)
        session.get.json = mock.Mock(return_value=fake)

        self.assertEqual(response.body['values'],
                         sot.targets(session, fake_entity_id))

        url = ("entities/%s/agent/check_types/%s/targets" % (
               fake_entity_id, sot.id))
        session.get.assert_called_with(url, endpoint_filter=sot.service)
