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

from openstack import proxy
from rackspace.backup.v1 import activity
from rackspace.backup.v1 import agent
from rackspace.backup.v1 import backup_configuration
from rackspace.backup.v1 import restore_configuration


class Proxy(proxy.BaseProxy):

    def activities(self, **query):
        """Return a generator of activities

        :param kwargs \*\*query: Optional query parameters to be sent to limit
                                 the resources being returned.

        :returns: A generator of activity objects
        :rtype: :class:`~rackspace.backup.v1.activity.Activity`
        """
        return self._list(activity.Activity, paginated=False, **query)

    def agents(self, **query):
        """Return a generator of agents

        :param kwargs \*\*query: Optional query parameters to be sent to limit
                                 the resources being returned.

        :returns: A generator of agent objects
        :rtype: :class:`~rackspace.backup.v1.agent.Agent`
        """
        return self._list(agent.Agent, paginated=False, **query)

    def delete_agent(self, value, ignore_missing=True):
        """Delete an agent

        :param value: The value can be either the ID of a agent or a
               :class:`~rackspace.backup.v1.agent.Agent` instance.
        :param bool ignore_missing: When set to ``False``
                    :class:`~openstack.exceptions.ResourceNotFound` will be
                    raised when the agent does not exist.
                    When set to ``True``, no exception will be set when
                    attempting to delete a nonexistent agent.
        :returns: ``None``
        """
        self._delete(agent.Agent, value, ignore_missing=ignore_missing)

    def backup_configurations(self, **query):
        """Return a generator of backup configurations

        :param kwargs \*\*query: Optional query parameters to be sent to limit
                                 the resources being returned.

        :returns: A generator of backup configuration objects
        :rtype: :class:`~rackspace.backup.v1.backup_configuration
                                            .BackupConfiguration`
        """
        return self._list(backup_configuration.BackupConfiguration,
                          paginated=False, **query)

    def create_backup_configuration(self, **attrs):
        """Create a new backup configuration from attributes

        :param dict attrs: Keyword arguments which will be used to create
                           a :class:`~rackspace.backup.v1.
                                backup_configuration.BackupConfiguration`,
                           comprised of the properties on the
                           BackupConfiguration class.
        :returns: The results of backup_configuration creation
        :rtype: :class:`~rackspace.backup.v1.backup_configuration
                                             .BackupConfiguration`
        """
        return self._create(backup_configuration.BackupConfiguration,
                            **attrs)

    def delete_backup_configuration(self, value, ignore_missing=True):
        """Delete a backup configuration

        :param value: The value can be either the ID of a agent or a
               :class:`~rackspace.backup.v1.backup_configuration
                                           .BackupConfiguration` instance.
        :param bool ignore_missing: When set to ``False``
                    :class:`~openstack.exceptions.ResourceNotFound` will be
                    raised when the agent does not exist.
                    When set to ``True``, no exception will be set when
                    attempting to delete a nonexistent agent.
        :returns: ``None``
        """
        self._delete(backup_configuration.BackupConfiguration,
                     value, ignore_missing=ignore_missing)

    def find_backup_configuration(self, name_or_id, ignore_missing=True):
        """Find a single backup configuration

        :param name_or_id: The name or ID of a backup configuration.
        :param bool ignore_missing: When set to ``False``
                    :class:`~openstack.exceptions.ResourceNotFound` will be
                    raised when the resource does not exist.
                    When set to ``True``, None will be returned when
                    attempting to find a nonexistent resource.
        :returns: One :class:`~rackspace.backup.v1.backup_configuration
                                               .BackupConfiguration` or None
        """
        return self._find(backup_configuration.BackupConfiguration,
                          name_or_id, ignore_missing=ignore_missing)

    def get_backup_configuration(self, value):
        """Get a single backup configuration

        :param value: The value can be the ID of a activity or a
                      :class:`~rackspace.backup.v1.backup_configuration
                                        .BackupConfiguration` instance.
        :returns: One :class:`~rackspace.backup.v1.backup_configuration
                                                  .BackupConfiguration`
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(backup_configuration.BackupConfiguration, value)

    def update_backup_configuration(self, value, **attrs):
        """Update a backup configuration

        :param value: Either the id of a backup_configuration or a
                      :class:`~rackspace.backup.v1.backup_configuration
                                        .BackupConfiguration` instance.
        :attrs kwargs: The attributes to update on the backup_configuration
                           represented by ``value``.
        :returns: The updated backup_configuration
        :rtype: :class:`~rackspace.backup.v1.backup_configuration
                                            .BackupConfiguration`
        """
        return self._update(backup_configuration.BackupConfiguration,
                            value, **attrs)

    def create_restore_configuration(self, **attrs):
        """Create a new restore configuration from attributes

        :param dict attrs: Keyword arguments which will be used to create
                           a :class:`~rackspace.backup.v1
                                               .restore_configuration
                                               .RestoreConfiguration`,
                           comprised of the properties on the
                           RestoreConfiguration class.
        :returns: The results of restore_configuration creation
        :rtype: :class:`~rackspace.backup.v1.restore_configuration
                                             .RestoreConfiguration`
        """
        return self._create(restore_configuration.RestoreConfiguration,
                            **attrs)

    def update_restore_configuration(self, value, **attrs):
        """Update a restore configuration

        :param value: Either the id of a restore_configuration or a
                      :class:`~rackspace.backup.v1.restore_configuration
                                        .RestoreConfiguration` instance.
        :attrs kwargs: The attributes to update on the restore_configuration
                       represented by ``value``.
        :returns: The updated restore_configuration
        :rtype: :class:`~rackspace.backup.v1.restore_configuration
                                            .RestoreConfiguration`
        """
        return self._update(restore_configuration.RestoreConfiguration,
                            value, **attrs)
