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

from rackspace.monitoring.v1 import agent

FAKE = {
    "timestamp": 1234567890,
    "info": [dict(), dict()]
}

EXAMPLE = {
    "id": "436fd64b-74f9-49cc-83cc-7b02dbcd478a",
    "last_connected": 1234567890
}


class TestAgent(testtools.TestCase):

    def test_basic(self):
        sot = agent.Agent(EXAMPLE)
        self.assertEqual('values', sot.resources_key)
        self.assertEqual('agents', sot.base_path)
        self.assertEqual("cloudMonitoring", sot.service.service_name)
        self.assertFalse(sot.allow_create)
        self.assertFalse(sot.allow_delete)
        self.assertTrue(sot.allow_list)
        self.assertTrue(sot.allow_retrieve)
        self.assertFalse(sot.allow_update)

    def test_make_it(self):
        sot = agent.Agent(EXAMPLE)
        self.assertEqual(EXAMPLE['id'], sot.id)
        self.assertEqual(EXAMPLE['last_connected'], sot.last_connected_at)

    def test_connections(self):
        sot = agent.Agent(EXAMPLE)
        fake = {"values": [dict(), dict()]}

        response = mock.Mock()
        response.body = fake
        response.json = mock.Mock(return_value=fake)

        session = mock.Mock()
        session.get = mock.Mock(return_value=response)
        session.get.json = mock.Mock(return_value=fake)

        self.assertEqual(response.body['values'], sot.connections(session))

        url = ("agents/%s/connections" % sot.id)
        session.get.assert_called_with(url, endpoint_filter=sot.service)

    def test_host_info_types(self):
        sot = agent.Agent(EXAMPLE)
        fake = {"types": ["cpus", "disks", "filesystems", "memory",
                          "network_interfaces", "nil", "processes", "system",
                          "who"]}

        response = mock.Mock()
        response.body = fake
        response.json = mock.Mock(return_value=fake)

        session = mock.Mock()
        session.get = mock.Mock(return_value=response)
        session.get.json = mock.Mock(return_value=fake)

        self.assertEqual(response.body['types'],
                         sot.host_info_types(session))

        url = ("agents/%s/host_info_types" % sot.id)
        session.get.assert_called_with(url, endpoint_filter=sot.service)

    def test_host_cpus(self):
        sot = agent.Agent(EXAMPLE)

        response = mock.Mock()
        response.body = FAKE
        response.json = mock.Mock(return_value=FAKE)

        session = mock.Mock()
        session.get = mock.Mock(return_value=response)
        session.get.json = mock.Mock(return_value=FAKE)

        self.assertEqual(response.body['info'], sot.host_cpus(session))

        url = ("agents/%s/host_info/cpus" % sot.id)
        session.get.assert_called_with(url, endpoint_filter=sot.service)

    def test_host_disks(self):
        sot = agent.Agent(EXAMPLE)

        response = mock.Mock()
        response.body = FAKE
        response.json = mock.Mock(return_value=FAKE)

        session = mock.Mock()
        session.get = mock.Mock(return_value=response)
        session.get.json = mock.Mock(return_value=FAKE)

        self.assertEqual(response.body['info'], sot.host_disks(session))

        url = ("agents/%s/host_info/disks" % sot.id)
        session.get.assert_called_with(url, endpoint_filter=sot.service)

    def test_host_filesystems(self):
        sot = agent.Agent(EXAMPLE)

        response = mock.Mock()
        response.body = FAKE
        response.json = mock.Mock(return_value=FAKE)

        session = mock.Mock()
        session.get = mock.Mock(return_value=response)
        session.get.json = mock.Mock(return_value=FAKE)

        self.assertEqual(response.body['info'], sot.host_filesystems(session))

        url = ("agents/%s/host_info/filesystems" % sot.id)
        session.get.assert_called_with(url, endpoint_filter=sot.service)

    def test_host_memory(self):
        sot = agent.Agent(EXAMPLE)

        response = mock.Mock()
        response.body = FAKE
        response.json = mock.Mock(return_value=FAKE)

        session = mock.Mock()
        session.get = mock.Mock(return_value=response)
        session.get.json = mock.Mock(return_value=FAKE)

        self.assertEqual(response.body['info'], sot.host_memory(session))

        url = ("agents/%s/host_info/memory" % sot.id)
        session.get.assert_called_with(url, endpoint_filter=sot.service)

    def test_host_nics(self):
        sot = agent.Agent(EXAMPLE)

        response = mock.Mock()
        response.body = FAKE
        response.json = mock.Mock(return_value=FAKE)

        session = mock.Mock()
        session.get = mock.Mock(return_value=response)
        session.get.json = mock.Mock(return_value=FAKE)

        self.assertEqual(response.body['info'], sot.host_nics(session))

        url = ("agents/%s/host_info/network_interfaces" % sot.id)
        session.get.assert_called_with(url, endpoint_filter=sot.service)

    def test_host_processes(self):
        sot = agent.Agent(EXAMPLE)

        response = mock.Mock()
        response.body = FAKE
        response.json = mock.Mock(return_value=FAKE)

        session = mock.Mock()
        session.get = mock.Mock(return_value=response)
        session.get.json = mock.Mock(return_value=FAKE)

        self.assertEqual(response.body['info'], sot.host_processes(session))

        url = ("agents/%s/host_info/processes" % sot.id)
        session.get.assert_called_with(url, endpoint_filter=sot.service)

    def test_host_system(self):
        sot = agent.Agent(EXAMPLE)

        response = mock.Mock()
        response.body = FAKE
        response.json = mock.Mock(return_value=FAKE)

        session = mock.Mock()
        session.get = mock.Mock(return_value=response)
        session.get.json = mock.Mock(return_value=FAKE)

        self.assertEqual(response.body['info'], sot.host_system(session))

        url = ("agents/%s/host_info/system" % sot.id)
        session.get.assert_called_with(url, endpoint_filter=sot.service)

    def test_host_users(self):
        sot = agent.Agent(EXAMPLE)

        response = mock.Mock()
        response.body = FAKE
        response.json = mock.Mock(return_value=FAKE)

        session = mock.Mock()
        session.get = mock.Mock(return_value=response)
        session.get.json = mock.Mock(return_value=FAKE)

        self.assertEqual(response.body['info'], sot.host_users(session))

        url = ("agents/%s/host_info/who" % sot.id)
        session.get.assert_called_with(url, endpoint_filter=sot.service)
