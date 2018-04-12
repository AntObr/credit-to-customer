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


class SuppressionLog(resource.Resource):
    base_path = 'suppression_logs'
    resources_key = 'values'
    service = monitoring_service.MonitoringService()

    # capabilities
    allow_list = True

    # Properties
    #: The ID of the alarm
    alarm_id = resource.prop('alarm_id')
    #: The ID of the check
    check_id = resource.prop('check_id')
    #: The ID of the entity
    entity_id = resource.prop('entity_id')
    #: The ID of the notification plan
    notification_plan_id = resource.prop('notification_plan_id')
    #: Status
    status = resource.prop('state')
    #: List of suppression IDs. *Type: list*
    suppressions = resource.prop('suppressions', type=list)
    #: Timestamp. *Type: int*
    timestamp = resource.prop('timestamp', type=int)
    #: The ID of the transaction
    transaction = resource.prop('transaction_id')
