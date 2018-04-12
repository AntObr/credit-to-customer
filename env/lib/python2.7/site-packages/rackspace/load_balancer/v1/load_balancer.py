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

from openstack import format
from openstack import resource2

from rackspace.load_balancer import load_balancer_service


class LoadBalancer(resource2.Resource):
    resource_key = "loadBalancer"
    resources_key = "loadBalancers"
    base_path = "/loadbalancers"
    service = load_balancer_service.LoadBalancerService()

    allow_create = True
    allow_update = True
    allow_get = True
    allow_list = True
    # TODO(briancurtin): CLB supports bulk delete by specifying
    # multiple CLB IDs in the query params.
    allow_delete = True

    _query_mapping = resource2.QueryParameters("status",
                                               node_address="nodeaddress",
                                               changes_since="changes-since")

    #: Name of the load balancer. The name must be 128 characters or
    #: fewer in length, and all UTF-8 characters are valid.
    name = resource2.Body("name")
    #: Protocol of the service that is being load balanced.
    protocol = resource2.Body("protocol")
    #: Port number for the service you are load balancing.
    port = resource2.Body("port", type=int)
    #: Algorithm that defines how traffic should be directed between
    #: back-end nodes.
    algorithm = resource2.Body("algorithm")
    #: The status of the load balancer.
    status = resource2.Body("status")
    #: The number of load balancer nodes.
    node_count = resource2.Body("nodeCount", type=int)
    #: The date and time what the load balancer was created.
    created_at = resource2.Body("created", type=dict)
    #: The date and time what the load balancer was last updated.
    updated_at = resource2.Body("updated", type=dict)
    #: The list of virtualIps for a load balancer. Each virtual IP has
    #:  id, address, type, and ipVersion keys.
    virtual_ips = resource2.Body("virtualIps", type=list)
    #: Nodes to be added to the load balancer. A list of dictionaries
    #: that include address, port, and condition keys.
    nodes = resource2.Body("nodes", type=list)
    #: Enables or disables Half-Closed support for the load balancer.
    #: Half-Closed support provides the ability for one end of the
    #: connection to terminate its output, while still receiving data
    #: from the other end. Only available for TCP/TCP_CLIENT_FIRST protocols.
    is_half_closed = resource2.Body("halfClosed", type=format.BoolStr)
    #: The access list management feature allows fine-grained network
    #: access controls to be applied to the load balancer virtual
    #: IP address. Refer to Access lists for information and examples.
    access_list = resource2.Body("accessList")
    #: Current connection logging configuration. Refer to Log connections
    #: for information and examples.
    connection_logging = resource2.Body("connectionLogging")
    #: Specifies limits on the number of connections per IP address to
    #: help mitigate malicious or abusive traffic to your applications.
    #: See Throttle connections for information and examples.
    connection_throttle = resource2.Body("connectionThrottle")
    #: The type of health monitor check to perform to ensure that the
    #: service is performing properly.
    health_monitor = resource2.Body("healthMonitor")
    #: Information (metadata) that can be associated with each load balancer.
    metadata = resource2.Body("metadata")
    #: The timeout value for the load balancer and communications with
    #: its nodes. Defaults to 30 seconds with a maximum of 120 seconds.
    timeout = resource2.Body("timeout", type=int)
    #: Specifies whether multiple requests from clients are directed
    #: to the same node.
    session_persistence = resource2.Body("sessionPersistence")
    #: Enables or disables HTTP to HTTPS redirection for the load balancer.
    #: When enabled, any HTTP request returns status code 301
    #: (Moved Permanently), and the requester is redirected to the
    #: requested URL via the HTTPS protocol on port 443.
    redirect_https = resource2.Body("httpsRedirect", type=format.BoolStr)
    #: The cluster name.
    cluster = resource2.Body("cluster")
    #: The source public and private IP addresses.
    source_addresses = resource2.Body("sourceAddresses")

    def update(self, session):
        """Update a load balancer

        :param session: The session to use for making this request.
        :type session: :class:`~openstack.session.Session`

        :return: This :class:`Resource` instance.
        :raises: :exc:`~openstack.exceptions.MethodNotSupported` if
                 :data:`Resource.allow_update` is not set to ``True``.
        """
        # NOTE (briancurtin): We override the base update because
        # CLB asynchronously processes the update, so it doesn't
        # return anything. We have to avoid the _translate_response call.

        # Only try to update if we actually have anything to update.
        if not any([self._body.dirty, self._header.dirty]):
            return self

        request = self._prepare_request(prepend_key=True)

        session.put(request.uri, endpoint_filter=self.service,
                    json=request.body, headers=request.headers)

        return self
