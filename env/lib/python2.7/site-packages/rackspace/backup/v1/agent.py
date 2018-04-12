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


class Agent(resource.Resource):
    id_attribute = 'MachineAgentId'
    base_path = '/user/agents'
    service = backup_service.BackupService()

    # capabilities
    allow_delete = True
    allow_retrieve = True
    allow_list = True

    # Properties
    #: Indicates whether a cleanup can be manually
    #: triggered on the backup vault
    can_cleanup = resource.prop('CleanupAllowed')
    #: Full public Cloud Files URI where backups are stored for this agent
    container = resource.prop('BackupContainer')
    #: Data center where the Cloud Server is located. Valid values are:
    #: ``IAD``, ``ORD``, ``DFW``, ``HKG``, ``LON``, or SYD.
    datacenter = resource.prop('Datacenter')
    #: Type of server. Valid values are:
    #: ``RaxCloudServer``: Rackspace Cloud Servers
    flavor = resource.prop('Flavor')
    #: Indicates if the Rackspace Cloud Backup agent on the server is disabled
    is_disabled = resource.prop('IsDisabled')
    #: Indicates if backups are encrypted. Valid values are:
    #: ``true`` or ``false``.
    is_encrypted = resource.prop('IsEncrypted')
    #: Time of last successful backup
    last_successful_backup_at = resource.prop('TimeOfLastSuccessfulBackup')
    #: Public key of the public/private encryption key pair
    public_key = resource.prop('PublicKey')
    #: Base architecture of the Cloud Server. Valid values are:
    # ``64-bit`` or ``32-bit``.
    server_arch = resource.prop('Architecture')
    #: Public IPv4 address of server
    server_ipaddress = resource.prop('IPAddress')
    #: Name of the server
    server_name = resource.prop('MachineName')
    #: Operating system of server
    server_os = resource.prop('OperatingSystem')
    #: Operating system version of server
    server_os_version = resource.prop('OperatingSystemVersion')
    #: The server ID of the host server where the Cloud Backup agent is running
    server_uuid = resource.prop('HostServerId')
    #: Indicates if the Cloud Backup agent is using Rackspace's ServiceNet
    #: to backup data to Cloud Files. Valid values are:
    #: ``true`` or ``false``.
    servicenet = resource.prop('UseServiceNet')
    #: Status of the Cloud Backup agent. Valid values are:
    # ``Online`` or ``Offline``.
    status = resource.prop('Status')
    #: Size of backup data in MB
    vault_size = resource.prop('BackupVaultSize')
    #: Version of the Rackspace Cloud Backup agent
    version = resource.prop('AgentVersion')

    def disable(self, session):
        """Disable agent.

        This operation disables the Cloud Backup agent. Disabling an agent
        does not delete it or its data. You can re-enable disabled agents
        later.

        :param session: The session to use for making this request.
        :type session: :class:`~openstack.session.Session`
        :returns: ``None``
        """
        body = {'MachineAgentId': self.id, 'Enable': 'false'}
        url = utils.urljoin('agent', 'enable')
        session.post(url, service=self.service, json=body)

    def encrypt_volume(self, session, secret):
        """Enable volume AES-256 encryption.

        After encryption is turned on, you cannot turn it off. This is a
        security measure. If you lose or forget your passphrase, you will
        not be able to recover your encrypted backups. If anyone ever gained
        access to your account, they would not be able to access your backups
        without your passphrase.
        http://www.rackspace.com/knowledge_center/
        article/generating-your-encrypted-key-in-cloud-backup

        :param session: The session to use for making this request.
        :param str secret: Encrypted passphrase
        :type session: :class:`~openstack.session.Session`
        :returns: ``str``
        """
        body = {'MachineAgentId': self.id, 'EncryptedPasswordHex': secret}
        url = utils.urljoin('agent', 'encrypt')
        return session.post(url, service=self.service, json=body).body

    def enable(self, session):
        """Enable agent.

        This operation enables the Cloud Backup agent. Disabling an agent
        does not delete it or its data. You can re-enable disabled agents
        later.

        :param session: The session to use for making this request.
        :type session: :class:`~openstack.session.Session`
        :returns: ``None``
        """
        body = {'MachineAgentId': self.id, 'Enable': 'true'}
        url = utils.urljoin('agent', 'enable')
        session.post(url, service=self.service, json=body)

    def migrate_vault(self, session, destination):
        """Migrate the backup vault to another machine agent.

        The destination agent should be under the same user and its backups
        should not be encrypted. The destination machine agent should not
        have any backups already configured and running.

        :param session: The session to use for making this request.
        :param str destination: Agent ID of the destination machine.
        :type session: :class:`~openstack.session.Session`
        :returns: ``None``
        """
        body = {'SourceMachineAgentId': self.id,
                'DestinationMachineAgentId': destination}
        url = utils.urljoin('agent', 'migratevault')
        session.post(url, service=self.service, json=body)

    def update_behavior(self, session, datacenter, servicenet=True):
        """Updates the backup datacenter and/or ServiceNet.

        Specifies the backup datacenter where this agent's backup
        will reside. You must have Cloud Servers in the data center specified
        or this operation will fail. If ServiceNet is enabled, the agent
        connects to Cloud Files over a private network and
        does not incur any bandwidth charges.

        :param session: The session to use for making this request.
        :param str datacenter: Valid datacenter. Valid values are: `IAD``,
                               ``ORD``, ``DFW``, ``HKG``, ``LON``, or SYD.
        :param bool servicenet: Enable/disable ServiceNet.
        :type session: :class:`~openstack.session.Session`
        :returns: ``None``
        """
        body = {'BackupDataCenter': datacenter,
                'UseServiceNet': servicenet}
        url = utils.urljoin('agent', self.id)
        session.post(url, service=self.service, json=body)

    def update_encryption_password(self, session, oldsecret, newsecret):
        """Update the volume AES-256 encryption passphrase.

        After encryption is turned on, you cannot turn it off. This is a
        security measure. If you lose or forget your passphrase, you will
        not be able to recover your encrypted backups. If anyone ever gained
        access to your account, they would not be able to access your backups
        without your passphrase.

        http://www.rackspace.com/knowledge_center/
        article/generating-your-encrypted-key-in-cloud-backup

        :param session: The session to use for making this request.
        :param str oldsecret: Old encrypted passphrase.
        :param str newsecret: New encrypted passphrase.
        :type session: :class:`~openstack.session.Session`
        :returns: ``str``
        """
        body = {'MachineAgentId': self.id,
                'OldEncryptedPasswordHex': oldsecret,
                'NewEncryptedPasswordHex': newsecret}
        url = utils.urljoin('agent', 'changeencryption')
        return session.post(url, service=self.service, json=body).body
