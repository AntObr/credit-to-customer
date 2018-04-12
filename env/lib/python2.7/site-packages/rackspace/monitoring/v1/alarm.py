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
from openstack import resource
from openstack import utils
from rackspace.monitoring import monitoring_service


class Alarm(resource.Resource):
    base_path = '/entities/%(entity_id)s/alarms'
    resources_key = 'values'
    service = monitoring_service.MonitoringService()

    # capabilities
    allow_create = True
    allow_delete = True
    allow_list = True
    allow_retrieve = True
    allow_update = True

    # Properties
    #: List of active suppressions. *Type: list*
    active_suppressions = resource.prop('active_suppressions', type=list)
    #: The ID of the check to alert on
    check_id = resource.prop('check_id')
    #: Creation timestamp.
    #: Time is shown in Coordinated Universal Time (UTC) as the number
    #: of milliseconds that have elapsed since January 1, 1970. *Type: int*
    created_at = resource.prop('created_at', type=int)
    #: The alarm DSL for describing alerting conditions and their output states
    criteria = resource.prop('criteria')
    # The ID of the entity
    entity_id = resource.prop('entity_id')
    #: Disables the alarm. *Type: bool*
    is_disabled = resource.prop('disabled', type=format.BoolStr)
    #: Arbitrary key/value pairs. *Type: dict*
    metadata = resource.prop('metadata', type=dict)
    #: A friendly label for an alarm
    name = resource.prop('label')
    #: The id of the notification plan to execute when the state changes
    notification_plan_id = resource.prop('notification_plan_id')
    #: List of scheduled suppressions. *Type: list*
    scheduled_suppressions = resource.prop('scheduled_suppressions', type=list)
    #: Update timestamp.
    #: Time is shown in Coordinated Universal Time (UTC) as the number
    #: of milliseconds that have elapsed since January 1, 1970. *Type: int*
    updated_at = resource.prop('updated_at', type=int)

    def notification_history(self, session):
        """Lists alarm notification history for the alarm and check

        :param session: The session to use for making this request.
        :type session: :class:`~openstack.session.Session`
        :returns: ``list``
        """
        url = utils.urljoin('entities', self.entity_id, 'alarms', self.id,
                            'notification_history', self.check_id)
        resp = session.get(url, endpoint_filter=self.service).json()
        return resp['values']
