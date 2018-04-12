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

from openstack import resource
from openstack import utils
from rackspace.monitoring import monitoring_service


class MonitoringZone(resource.Resource):
    base_path = 'monitoring_zones'
    resources_key = 'values'
    service = monitoring_service.MonitoringService()

    # capabilities
    allow_list = True
    allow_retrieve = True

    # Properties
    #: Country Code
    country = resource.prop('country_code')
    #: A friendly label for the monitoring zone
    name = resource.prop('label')
    #: Source IP list for the monitoring zone. *Type: list*
    source_ip_addresses = resource.prop('source_ips', type=list)

    def traceroute(self, session, target, target_resolver="IPv4"):
        """Issue a traceroute from a monitoring zone to a host

        :param str target: Hostname or IP address
        :param str target_resolver: `IPv4` or `IPv6`
        :param session: The session to use for making this request.
        :type session: :class:`~openstack.session.Session`
        :returns: ``list``
        """
        body = {"target": target, "target_resolver": target_resolver}
        url = utils.urljoin(self.base_path, self.id, 'traceroute')
        resp = session.post(url, endpoint_filter=self.service, json=body).body
        return resp['result']
