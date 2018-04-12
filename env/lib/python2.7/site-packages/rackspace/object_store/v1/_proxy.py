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

from openstack.object_store.v1 import _proxy
from openstack.object_store.v1 import container as _container

from rackspace.object_store.v1 import bulk_delete


class Proxy(_proxy.Proxy):

    def __init__(self, session):
        super(Proxy, self).__init__(session)

    # TODO(briancurtin): Bulk delete can also take a list of containers,
    # not just empty out the objects within a container.

    def bulk_delete(self, container):
        """Delete all objects in a container

        :param container: The container with objects to delete. You can
            pass a container object or the name of a container.
        :type container:
            :class:`~openstack.object_store.v1.container.Container`

        :returns: An object containing information about the
            bulk delete operation
        :rtype:
            :class:`~rackspace.object_store.v1.bulk_delete.BulkDelete`
        """
        objects = []
        container = _container.Container.from_id(container)
        for obj in self.objects(container):
            full_name = "/{0.container}/{0.name}".format(obj)
            objects.append(full_name)
        objects = "\n".join(objects)

        return bulk_delete.BulkDelete.delete(self.session, objects)
