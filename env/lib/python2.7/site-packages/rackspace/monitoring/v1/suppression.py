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
from rackspace.monitoring import monitoring_service


class Suppression(resource.Resource):
    base_path = 'suppressions'
    resources_key = 'values'
    service = monitoring_service.MonitoringService()

    # capabilities
    allow_create = True
    allow_delete = True
    allow_list = True
    allow_retrieve = True
    allow_update = True

    # Properties
    #: A list of alarm IDs for determining notification suppression
    #: *Type: list*
    alarms = resource.prop('alarms', type=list)
    #: A list of check IDs for determining notification suppression
    #: *Type: list*
    checks = resource.prop('checks', type=list)
    #: The Unix timestamp in milliseconds that the suppression will end.
    #: Specify `0` to use the current time. *Type: int*
    ends_at = resource.prop('end_time', type=int)
    #: A list of entity IDs for determining notification suppression
    #: *Type: list*
    entities = resource.prop('entities', type=list)
    #: A friendly label for the suppression
    name = resource.prop('label')
    #: A list of notification plans IDs for determining notification plans
    #: *Type: list*
    notification_plans = resource.prop('notification_plans', type=list)
    #: The Unix timestamp in milliseconds that the suppression will start.
    #: Specify `0` to use the current time. *Type: int*
    starts_at = resource.prop('start_time', type=int)
