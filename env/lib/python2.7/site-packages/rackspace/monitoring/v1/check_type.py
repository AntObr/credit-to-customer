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


class CheckType(resource.Resource):
    base_path = 'check_types'
    resources_key = 'values'
    service = monitoring_service.MonitoringService()

    # capabilities
    allow_list = True
    allow_retrieve = True

    # Properties
    #: The category the check is in. Valid values are:
    #: ``agent`` or ``remote``.
    category = resource.prop('category')
    #: Check type fields. *Type: list*
    fields = resource.prop('fields', type=list)
    #: A friendly label
    name = resource.prop('id')
    #: Platforms on which an agent check type is supported. This is advisory
    #: information only. The check may still work on other platforms,
    #: or report that check execution failed at runtime.
    supported_platforms = resource.prop('supported_platforms')
    #: The name of the supported check type. Valid values are:
    #: ``agent`` or ``remote``.
    type = resource.prop('type')

    def targets(self, session, entity_id):
        """Lists agent check type targets for an entity

        Agent check types can gather data for a related set of target devices
        on the server where the agent is installed. Not every check type has a
        configurable target; currently supported check types with targets are:
        `agent.filesystem`, `agent.disk`, `agent.network`, and `agent.plugin`.

        :param entity_id: Target entity id where the agent is installed
        :param session: The session to use for making this request.
        :type session: :class:`~openstack.session.Session`
        :returns: ``list``
        """
        url = utils.urljoin('entities', entity_id, 'agent',
                            'check_types', self.id, 'targets')
        resp = session.get(url, endpoint_filter=self.service).json()
        return resp['values']
