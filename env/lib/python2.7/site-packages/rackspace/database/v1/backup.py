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


class Backup(resource.Resource):
    base_path = 'backups'
    resource_key = 'backup'
    resources_key = "backups"
    service = database_service.DatabaseService()

    # capabilities
    allow_create = True
    allow_delete = True
    allow_list = True
    allow_retrieve = True
    allow_update = False

    # Properties
    #: Creation time
    created_at = resource.prop('created')
    #: Datastore type and version. *Type: dict*
    datastore = resource.prop('datastore', type=dict)
    #: Long form description
    description = resource.prop('description')
    #: Full public Cloud Files URI where backups are stored
    destination = resource.prop('locationRef')
    #: Indicates if the backup is automated. Valid values include:
    #: ``0``: False
    #: ``1``: True
    is_automated = resource.prop('is_automated', type=int)
    #: Name of backup
    name = resource.prop('name')
    #: Flavor of original instance
    instance_flavor = resource.prop('flavor_ram')
    #: The source instance ID for a backup. *Type: Instance*
    instance_id = resource.prop('instance_id', type=instance.Instance)
    #: Volume size of original instance. *Type: int*
    instance_volume_size = resource.prop('volume_size', type=int)
    #: Size of backup in GB. *Type: float*
    size = resource.prop('size', type=float)
    #: Specifies the source type (instance/ha) and source id (instanceID/haID)
    source = resource.prop('source', type=dict)
    #: The state this instance is in. Valid values include:
    #: ``NEW``: A new backup task was created
    #: ``BUILDING``: The backup task is currently running
    #: ``COMPLETED``: The backup task was successfully completed
    #: ``FAILED``: The backup task failed to complete successfully
    #: ``DELETE_FAILED``: The backup task failed to delete Cloud Files objects
    status = resource.prop('status')
    #: Backup type. Valid values include:
    #: ``InnoBackupEx``: InnoDB datastore backup
    type = resource.prop('type')
    #: Update time
    updated_at = resource.prop('updated')

    def restore(self, session, **attrs):
        """Creates a new database instance from this backup.

        Refer to Create instance for details on other options available during
        the creation of a new instance. All users/passwords/access that were on
        the instance at the time of the backup will be restored along with the
        databases. You can create new users or databases if you want, but they
        cannot be the same as the ones from the instance that was backed up.
        You can restore from an incremental backup the same as from a full
        backup. The system automatically restores all parents first,
        and then applies the incremental backup.

        :param session: The session to use for making this request.
        :param dict attrs: Keyword arguments which will be used to create
                           a :class:`~rackspace.database.v1.backup.Backup`,
                           comprised of the properties on the Backup class.
        :type session: :class:`~openstack.session.Session`
        :returns: ``dict``
        """
        body = {"instance": {"restorePoint": {"backupRef": self.id}}}
        body.update(attrs)
        resp = session.post('instances', service=self.service, json=body).body
        return resp['instance']
