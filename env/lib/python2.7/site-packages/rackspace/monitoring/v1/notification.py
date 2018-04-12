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


class Notification(resource.Resource):
    base_path = 'notifications'
    resources_key = 'values'
    service = monitoring_service.MonitoringService()

    # capabilities
    allow_create = True
    allow_delete = True
    allow_list = True
    allow_retrieve = True
    allow_update = True

    # Properties
    #: Details specific to the notification. *Type: dict*
    details = resource.prop('details', type=dict)
    #: A friendly label for the notification type
    name = resource.prop('label')
    #: The type of notification to send
    type = resource.prop('type')

    def test(self, session):
        """Test an existing notification

        The notification comes from the same server that the alert messages
        come from. One use for this test is to verify that your firewall is
        configured properly.

        :param session: The session to use for making this request.
        :type session: :class:`~openstack.session.Session`
        :returns: ``dict``
        """
        url = utils.urljoin(self.base_path, self.id, 'test')
        return session.post(url, endpoint_filter=self.service).body
