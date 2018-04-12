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

from openstack.tests.unit import test_proxy_base2

from rackspace.load_balancer.v1 import _proxy
from rackspace.load_balancer.v1 import load_balancer
from rackspace.load_balancer.v1 import ssl_termination


class TestLoadBalancerProxy(test_proxy_base2.TestProxyBase):

    def setUp(self):
        super(TestLoadBalancerProxy, self).setUp()
        self.proxy = _proxy.Proxy(self.session)

    def test_load_balancer_create(self):
        self.verify_create(self.proxy.create_load_balancer,
                           load_balancer.LoadBalancer)

    def test_load_balancer_delete(self):
        self.verify_delete(self.proxy.delete_load_balancer,
                           load_balancer.LoadBalancer, False)

    def test_load_balancer_delete_ignore(self):
        self.verify_delete(self.proxy.delete_load_balancer,
                           load_balancer.LoadBalancer, True)

    def test_load_balancer_find(self):
        self.verify_find(self.proxy.find_load_balancer,
                         load_balancer.LoadBalancer)

    def test_load_balancer_get(self):
        self.verify_get(self.proxy.get_load_balancer,
                        load_balancer.LoadBalancer)

    def test_load_balancers(self):
        self.verify_list(self.proxy.load_balancers,
                         load_balancer.LoadBalancer,
                         paginated=False,
                         method_kwargs={"changes_since": 1},
                         expected_kwargs={"changes_since": 1})

    def test_load_balancer_update(self):
        rv = 100
        fake_lb = mock.Mock(spec=load_balancer.LoadBalancer)
        fake_lb.update.return_value = rv

        attrs = {"name": "brian"}

        self.proxy._get_resource = lambda *args: fake_lb
        result = self.proxy.update_load_balancer("lb", **attrs)

        fake_lb._update.assert_called_with(**attrs)

        self.assertEqual(result, rv)

    def test_ssl_termination_delete(self):
        lb_id = "load_balancer_id"

        self._verify2('openstack.proxy2.BaseProxy._delete',
                      self.proxy.delete_ssl_termination,
                      method_args=[lb_id],
                      method_kwargs={"ignore_missing": False},
                      expected_args=[ssl_termination.SSLTermination],
                      expected_kwargs={"load_balancer_id": lb_id,
                                       "ignore_missing": False})

    def test_ssl_termination_delete_ignore(self):
        lb_id = "load_balancer_id"

        self._verify2('openstack.proxy2.BaseProxy._delete',
                      self.proxy.delete_ssl_termination,
                      method_args=[lb_id],
                      expected_args=[ssl_termination.SSLTermination],
                      expected_kwargs={"load_balancer_id": lb_id,
                                       "ignore_missing": True})

    def test_ssl_termination_get(self):
        lb_id = "load_balancer_id"

        self._verify2('openstack.proxy2.BaseProxy._get',
                      self.proxy.get_ssl_termination,
                      method_args=[lb_id],
                      expected_args=[ssl_termination.SSLTermination],
                      expected_kwargs={"load_balancer_id": lb_id})

    def test_ssl_termination_update(self):
        lb_id = "load_balancer_id"

        self._verify2("openstack.proxy2.BaseProxy._update",
                      self.proxy.update_ssl_termination,
                      method_args=[lb_id],
                      expected_args=[ssl_termination.SSLTermination],
                      expected_kwargs={"load_balancer_id": lb_id})
