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

from rackspace.monitoring.v1 import agent_token


EXAMPLE = {
    "token": "4c5e28f0-0b3f-11e1-860d-c55c4705a286:1234",
    "label": "aLabel"
}


class TestAgentToken(testtools.TestCase):
    def test_basic(self):
        sot = agent_token.AgentToken()
        self.assertEqual('values', sot.resources_key)
        self.assertEqual('agent_tokens', sot.base_path)
        self.assertEqual("cloudMonitoring", sot.service.service_name)
        self.assertTrue(sot.allow_create)
        self.assertTrue(sot.allow_delete)
        self.assertTrue(sot.allow_list)
        self.assertTrue(sot.allow_retrieve)
        self.assertTrue(sot.allow_update)

    def test_make_it(self):
        sot = agent_token.AgentToken(EXAMPLE)
        self.assertEqual(EXAMPLE['token'], sot.token)
        self.assertEqual(EXAMPLE['label'], sot.name)
