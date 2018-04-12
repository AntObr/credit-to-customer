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

from openstack.database.v1 import instance
from openstack import resource
from rackspace.database import database_service


class BackupSchedule(resource.Resource):
    id_attribute = 'id'
    base_path = 'schedules'
    resources_key = "schedules"
    service = database_service.DatabaseService()

    # capabilities
    allow_create = True
    allow_delete = True
    allow_list = True
    allow_retrieve = True
    allow_update = True

    # Properties
    #: Action (backup)
    action = resource.prop('action')
    #: Creation time
    created_at = resource.prop('created')
    #: Last scheduled run
    last_run = resource.prop('last_scheduled')
    #: Next scheduled run
    next_run = resource.prop('next_run')
    #: The instance ID of the source
    source_instance = resource.prop('instance_id', type=instance.Instance)
    #: Scheduled day of the month
    start_day_of_month_at = resource.prop('day_of_month')
    #: Scheduled day of the week
    start_day_of_week_at = resource.prop('day_of_week')
    #: Scheduled hour of the day
    start_hour_at = resource.prop('hour')
    #: Scheduled minute of the hour
    start_minute_at = resource.prop('minute')
    #: Scheduled month of the year
    start_month_at = resource.prop('month')
    #: Update time
    updated_at = resource.prop('updated')
