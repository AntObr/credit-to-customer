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

from openstack import proxy2
from openstack import resource2

from rackspace.load_balancer.v1 import load_balancer as _load_balancer
from rackspace.load_balancer.v1 import ssl_termination


class Proxy(proxy2.BaseProxy):

    def __init__(self, session):
        super(Proxy, self).__init__(session)

    def load_balancers(self, **query):
        """Return a generator of load balancers

        :returns: A generator of load balancer objects
        :rtype:
            :class:`~rackspace.load_balancer.v1.load_balancer.LoadBalancer`
        """
        return self._list(_load_balancer.LoadBalancer,
                          paginated=False, **query)

    def get_load_balancer(self, load_balancer):
        """Get a single load balancer

        :param load_balancer: The value can be the ID of a load balancer or a
            :class:`~rackspace.load_balancer.v1.load_balancer.LoadBalancer`
            instance.

        :returns: One
            :class:`~rackspace.load_balancer.v1.load_balancer.LoadBalancer`
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(_load_balancer.LoadBalancer, load_balancer)

    def create_load_balancer(self, **attrs):
        """Create a new server from attributes

        :param dict attrs: Keyword arguments which will be used to create a
            :class:`~rackspace.load_balancer.v1.load_balancer.LoadBalancer`
            comprised of the properties on the LoadBalancer class.

        :returns: The results of load balancer creation
        :rtype:
            :class:`~rackspace.load_balancer.v1.load_balancer.LoadBalancer`
        """
        return self._create(_load_balancer.LoadBalancer, **attrs)

    def delete_load_balancer(self, load_balancer, ignore_missing=True):
        """Delete a load balancer

        :param load_balancer: Either the ID of a server or a
            :class:`~rackspace.load_balancer.v1.load_balancer.LoadBalancer`
            instance.
        :param bool ignore_missing: When set to ``False``
                    :class:`~openstack.exceptions.ResourceNotFound` will be
                    raised when the server does not exist.
                    When set to ``True``, no exception will be set when
                    attempting to delete a nonexistent server.

        :returns: ``None``
        """
        self._delete(_load_balancer.LoadBalancer, load_balancer,
                     ignore_missing=ignore_missing)

    def update_load_balancer(self, load_balancer, **attrs):
        """Update a load balancer

        :param load_balancer: Either the ID of a server or a
            :class:`~rackspace.load_balancer.v1.load_balancer.LoadBalancer`
            instance.
        :attrs kwargs: The attributes to update on the load balancer
                       represented by ``load_balancer``.

        :returns: The updated load balancer
        :rtype:
            :class:`~rackspace.load_balancer.v1.load_balancer.LoadBalancer`
        """
        res = self._get_resource(_load_balancer.LoadBalancer, load_balancer)
        res._update(**attrs)
        return res.update(self.session)

    def find_load_balancer(self, name_or_id, ignore_missing=True):
        """Find a single load balancer

        :param name_or_id: The name or ID of a load balancer.
        :param bool ignore_missing: When set to ``False``
                    :class:`~openstack.exceptions.ResourceNotFound` will be
                    raised when the resource does not exist.
                    When set to ``True``, None will be returned when
                    attempting to find a nonexistent resource.
        :returns: One
            :class:`~rackspace.load_balancer.v1.load_balancer.LoadBalancer`
            or None
        """
        return self._find(_load_balancer.LoadBalancer, name_or_id,
                          ignore_missing=ignore_missing)

    def get_ssl_termination(self, load_balancer):
        """Get the SSL termination configuration of a load balancer

        :param load_balancer: The value can be the ID of a load balancer or a
            :class:`~rackspace.load_balancer.v1.load_balancer.LoadBalancer`
            instance.

        :returns: An object containing information about the
            load balancer's SSL termination configuration.
        :rtype:
            :class:`~rackspace.load_balancer.v1.ssl_termination.SSLTermination`
        """
        load_balancer_id = resource2.Resource._get_id(load_balancer)
        return self._get(ssl_termination.SSLTermination,
                         load_balancer_id=load_balancer_id)

    def update_ssl_termination(self, load_balancer, **attrs):
        """Update the SSL termination configuration of a load balancer

        :param load_balancer: The value can be the ID of a load balancer or a
            :class:`~rackspace.load_balancer.v1.load_balancer.LoadBalancer`
            instance.
        :param **attrs: Attributes to be set on a
            :class:`~rackspace.load_balancer.v1.ssl_termination.SSLTermination`
            instance.

        :returns: An object containing information about the
            load balancer's SSL termination configuration.
        :rtype:
            :class:`~rackspace.load_balancer.v1.ssl_termination.SSLTermination`
        """
        load_balancer_id = resource2.Resource._get_id(load_balancer)
        return self._update(ssl_termination.SSLTermination,
                            load_balancer_id=load_balancer_id, **attrs)

    def delete_ssl_termination(self, load_balancer, ignore_missing=True):
        """Delete the SSL termination configuration of a load balancer

        :param load_balancer: The value can be the ID of a load balancer or a
            :class:`~rackspace.load_balancer.v1.load_balancer.LoadBalancer`
            instance.
        :param bool ignore_missing: When set to ``False``
                    :class:`~openstack.exceptions.ResourceNotFound` will be
                    raised when the member does not exist.
                    When set to ``True``, no exception will be set when
                    attempting to delete a nonexistent member.

        :returns: An object containing information about the
            load balancer's SSL termination configuration.
        :rtype:
            :class:`~rackspace.load_balancer.v1.ssl_termination.SSLTermination`
        """
        load_balancer_id = resource2.Resource._get_id(load_balancer)
        self._delete(ssl_termination.SSLTermination,
                     load_balancer_id=load_balancer_id,
                     ignore_missing=ignore_missing)
