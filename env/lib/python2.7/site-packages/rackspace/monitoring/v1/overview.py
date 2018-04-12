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


class Overview(resource.Resource):
    base_path = '/views/overview'
    resources_key = 'values'
    service = monitoring_service.MonitoringService()

    # capabilities
    allow_list = True

    # Properties
    #: List of alarms. *Type: list*
    alarms = resource.prop('alarms', type=list)
    #: List of checks. *Type: list*
    checks = resource.prop('checks', type=list)
    # The ID of the entity. *Type: Entity*
    entity = resource.prop('entity_id', type=dict)
    #: List of alarm states. *Type: list*
    latest_alarm_states = resource.prop('latest_alarm_states', type=list)
