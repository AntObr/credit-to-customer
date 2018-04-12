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

from rackspace.load_balancer.v1 import load_balancer

EXAMPLE = {
    "name": "me",
    "protocol": "lol",
    "port": 999,
    "algorithm": "something",
    "status": "great",
    "nodeCount": 3,
    "created": {"time": 1},
    "updated": {"time": 2},
    "virtualIps": [1],
    "nodes": [2],
    "halfClosed": "false",
    "accessList": "blah",
    "connectionLogging": "sure",
    "connectionThrottle": "yeah",
    "healthMonitor": "fine",
    "metadata": "nah",
    "timeout": 30,
    "sessionPersistence": "ok",
    "httpsRedirect": "true",
    "cluster": "bluster",
    "sourceAddresses": "whatever"
}


class TestLoadBalancer(testtools.TestCase):

    def test_basic(self):
        sot = load_balancer.LoadBalancer()

        self.assertEqual("loadBalancer", sot.resource_key)
        self.assertEqual("loadBalancers", sot.resources_key)
        self.assertEqual("/loadbalancers", sot.base_path)
        self.assertEqual("rax:load-balancer", sot.service.service_type)
        self.assertTrue(sot.allow_get)
        self.assertTrue(sot.allow_update)
        self.assertTrue(sot.allow_delete)
        self.assertTrue(sot.allow_create)
        self.assertTrue(sot.allow_list)

        self.assertDictEqual({"status": "status", "limit": "limit",
                              "marker": "marker",
                              "node_address": "nodeaddress",
                              "changes_since": "changes-since"},
                             sot._query_mapping._mapping)

    def test_make_it(self):
        sot = load_balancer.LoadBalancer(**EXAMPLE)
        self.assertEqual(EXAMPLE["name"], sot.name)
        self.assertEqual(EXAMPLE["protocol"], sot.protocol)
        self.assertEqual(EXAMPLE["port"], sot.port)
        self.assertEqual(EXAMPLE["algorithm"], sot.algorithm)
        self.assertEqual(EXAMPLE["status"], sot.status)
        self.assertEqual(EXAMPLE["nodeCount"], sot.node_count)
        self.assertEqual(EXAMPLE["created"], sot.created_at)
        self.assertEqual(EXAMPLE["updated"], sot.updated_at)
        self.assertEqual(EXAMPLE["virtualIps"], sot.virtual_ips)
        self.assertEqual(EXAMPLE["nodes"], sot.nodes)
        self.assertFalse(sot.is_half_closed)
        self.assertEqual(EXAMPLE["accessList"], sot.access_list)
        self.assertEqual(EXAMPLE["connectionLogging"],
                         sot.connection_logging)
        self.assertEqual(EXAMPLE["connectionThrottle"],
                         sot.connection_throttle)
        self.assertEqual(EXAMPLE["healthMonitor"], sot.health_monitor)
        self.assertEqual(EXAMPLE["metadata"], sot.metadata)
        self.assertEqual(EXAMPLE["timeout"], sot.timeout)
        self.assertEqual(EXAMPLE["sessionPersistence"],
                         sot.session_persistence)
        self.assertTrue(sot.redirect_https)
        self.assertEqual(EXAMPLE["cluster"], sot.cluster)
        self.assertEqual(EXAMPLE["sourceAddresses"], sot.source_addresses)
