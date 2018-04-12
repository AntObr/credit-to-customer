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
from rackspace.backup import backup_service


class BackupConfiguration(resource.Resource):
    id_attribute = 'BackupConfigurationId'
    base_path = 'backup-configuration'
    service = backup_service.BackupService()

    # capabilities
    allow_create = True
    allow_delete = True
    allow_list = True
    allow_retrieve = True
    allow_update = True

    # Properties
    #: ID that uniquely identifies a Cloud Backup agent
    agent_id = resource.prop('MachineAgentId')
    #: List of files and folders not to back up. *Type: list*
    exclusions = resource.prop('Exclusions', type=list)
    #: Type of server. Valid values are:
    #: ``RaxCloudServer``: Rackspace Cloud Servers
    flavor = resource.prop('Flavor')
    #: Frequency of backup schedule. Valid values are:
    #: ``Manually``, ``Hourly``, ``Daily``, and ``Weekly``.
    frequency = resource.prop('Frequency')
    #: List of files and folders to back up. *Type: list*
    inclusions = resource.prop('Inclusions', type=list)
    #: Indicates if a backup configuration is active. Valid values are:
    #: ``true`` or ``false``.
    is_active = resource.prop('IsActive')
    #: Indicates if the backup configuration is deleted. Valid values are:
    #: ``true`` or ``false``.
    is_deleted = resource.prop('IsDeleted')
    #: Indicates if backups are encrypted. Valid values are:
    #: ``true`` or ``false``.
    is_encrypted = resource.prop('IsEncrypted')
    #: AM or PM time for manual and hourly backups. Valid values are:
    #: ``AM`` or ``PM``
    #: ``null``: if frequency value is ``Manually`` ,``Hourly``.
    hour_am_pm_at = resource.prop('StartTimeAmPm')
    #: The hour if frequency is set to ``Hourly``. Valid values are:
    #: ``1`` through ``23``
    #: ``null``: if frequency value is ``Manually``, ``Daily``, or ``Weekly``.
    hourly_at = resource.prop('HourInterval')
    #: The name of the backup configuration. Configurations typically have
    #: the backup schedule, files to backup, and notification options.
    name = resource.prop('BackupConfigurationName')
    #: Notify after a failed backup. Valid values are:
    #: ``true`` or ``false``.
    notify_on_failure = resource.prop('NotifySuccess')
    #: Notify after a successful backup. Valid values are:
    #: ``true`` or ``false``.
    notify_on_success = resource.prop('NotifyFailure')
    #: The email address to notify
    notify_to = resource.prop('NotifyRecipients')
    #: Specifies when to send notification. Valid values are:
    #: ``1``: Notifications are sent as soon as possible
    #: ``2``: Notifications are sent at the next scheduled time
    notify_when = resource.prop('MissedBackupActionId', type=int)
    #: Indicates how many days backup revisions are maintained. Valid values:
    #: ``0``, ``30`` , and ``60``. ``0`` means indefinite.
    retention = resource.prop('VersionRetention')
    #: ID that uniquely identifies a Cloud Backup schedule
    schedule = resource.prop('BackupConfigurationScheduleId')
    #: The day of the week if frequency is set to ``Hourly``. Valid values are:
    #: ``0`` through ``6``: with ``0`` representing ``Sunday``
    #:                      and ``6`` representing ``Saturday``
    #: ``null``: if frequency value is ``Manually``, ``Daily``, or ``Weekly``.
    start_day_of_week_at = resource.prop('DayOfWeekId')
    #: The hour when the backup runs if frequency is
    #: set to ``Daily`` or ``Weekly``. Valid values are:
    #: ``1`` through ``12``
    #: ``null``: if frequency value is ``Manually`` or ``Hourly``.
    start_hour_at = resource.prop('StartTimeHour')
    #: The hour when the backup runs if frequency is
    #: set to ``Daily`` or ``Weekly``. Valid values are:
    #: ``0`` through ``59``
    #: ``null``: if frequency value is ``Manually`` or ``Hourly``.
    start_minute_at = resource.prop('StartTimeHour')
    #: Specifies the time zone where the backup runs. For example:
    #: ``Eastern Standard Time``.
    timezone = resource.prop('TimeZoneId')

    def disable(self, session):
        """Disable backup configuration.

        This operation disables the backup configuration. Disabling a backup
        configuration does not delete it or its data. You can re-enable
        disabled backup configurations later.

        :param session: The session to use for making this request.
        :type session: :class:`~openstack.session.Session`
        :returns: ``None``
        """
        body = {"Enable": 'false'}
        url = utils.urljoin('backup-configuration', 'enable', self.id)
        session.post(url, service=self.service, json=body)

    def enable(self, session):
        """Enable backup configuration.

        This operation enables the backup configuration. Disabling a backup
        configuration does not delete it or its data. You can re-enable
        disabled backup configurations later.

        :param session: The session to use for making this request.
        :type session: :class:`~openstack.session.Session`
        :returns: ``None``
        """
        body = {"Enable": 'true'}
        url = utils.urljoin('backup-configuration', 'enable', self.id)
        session.post(url, service=self.service, json=body)
