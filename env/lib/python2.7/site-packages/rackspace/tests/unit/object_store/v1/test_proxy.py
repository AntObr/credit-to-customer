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
from openstack.object_store.v1 import container
from openstack.tests.unit import test_proxy_base

from rackspace.object_store.v1 import _proxy


class TestObjectStoreProxy(test_proxy_base.TestProxyBase):

    def setUp(self):
        super(TestObjectStoreProxy, self).setUp()
        self.session = mock.Mock()

        self.proxy = _proxy.Proxy(self.session)


class Test_bulk_delete(TestObjectStoreProxy):

    @mock.patch("rackspace.object_store.v1.bulk_delete.BulkDelete.delete")
    def test(self, mock_delete):
        self.proxy.objects = mock.Mock()
        container_name = "Clark"
        object_name = "Addison"
        rv = [container.Container.new(name=object_name,
                                      container=container_name)]
        self.proxy.objects.return_value = rv

        self.proxy.bulk_delete("doesn't matter")

        expected = "/{0}/{1}".format(container_name, object_name)
        mock_delete.assert_called_with(self.session, expected)
