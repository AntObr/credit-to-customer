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


class Agent(resource.Resource):
    base_path = 'agents'
    resources_key = 'values'
    service = monitoring_service.MonitoringService()

    # capabilities
    allow_list = True
    allow_retrieve = True

    # Properties
    #: User specified strings that are a maximum of 255 characters and
    #: can contain letters, numbers, dashes (-) and dots (.). If you used
    #: the Setup wizard to install and configure the agent on your host server,
    #: the ID for your agent is the fully qualified domain name (FQDN) of the
    #: host on which the agent is installed.
    id = resource.prop('id')
    #: Agent last connection time to a monitoring zone. If an agent does not
    #: connect to the account for 30 days, the agent is automatically deleted.
    #: Time is shown in Coordinated Universal Time (UTC) as the number
    #: of milliseconds that have elapsed since January 1, 1970. *Type: int*
    last_connected_at = resource.prop('last_connected', type=int)

    def connections(self, session):
        """List currently active connections for the agent

        Agents are connected to three monitoring zones
        when operating normally.

        :param session: The session to use for making this request.
        :type session: :class:`~openstack.session.Session`
        :returns: ``list``
        """
        url = utils.urljoin(self.base_path, self.id, 'connections')
        resp = session.get(url, endpoint_filter=self.service).json()
        return resp['values']

    def host_info_types(self, session):
        """List the types of host info data supported by the agent

        :param session: The session to use for making this request.
        :type session: :class:`~openstack.session.Session`
        :returns: ``list``
        """
        url = utils.urljoin(self.base_path, self.id, 'host_info_types')
        resp = session.get(url, endpoint_filter=self.service).json()
        return resp['types']

    def host_cpus(self, session):
        """Get information about the host CPUs

        :param session: The session to use for making this request.
        :type session: :class:`~openstack.session.Session`
        :returns: ``list``
        """
        url = utils.urljoin(self.base_path, self.id, 'host_info', 'cpus')
        resp = session.get(url, endpoint_filter=self.service).json()
        return resp['info']

    def host_disks(self, session):
        """Get information about the host disks

        :param session: The session to use for making this request.
        :type session: :class:`~openstack.session.Session`
        :returns: ``list``
        """
        url = utils.urljoin(self.base_path, self.id, 'host_info', 'disks')
        resp = session.get(url, endpoint_filter=self.service).json()
        return resp['info']

    def host_filesystems(self, session):
        """Get information about the host filesystems

        :param session: The session to use for making this request.
        :type session: :class:`~openstack.session.Session`
        :returns: ``list``
        """
        url = utils.urljoin(
            self.base_path, self.id, 'host_info', 'filesystems')
        resp = session.get(url, endpoint_filter=self.service).json()
        return resp['info']

    def host_memory(self, session):
        """Get information about the host memory use

        :param session: The session to use for making this request.
        :type session: :class:`~openstack.session.Session`
        :returns: ``list``
        """
        url = utils.urljoin(self.base_path, self.id, 'host_info', 'memory')
        resp = session.get(url, endpoint_filter=self.service).json()
        return resp['info']

    def host_nics(self, session):
        """Get information about the host network interfaces

        :param session: The session to use for making this request.
        :type session: :class:`~openstack.session.Session`
        :returns: ``list``
        """
        url = utils.urljoin(
            self.base_path, self.id, 'host_info', 'network_interfaces')
        resp = session.get(url, endpoint_filter=self.service).json()
        return resp['info']

    def host_processes(self, session):
        """Get information about the host running processes

        :param session: The session to use for making this request.
        :type session: :class:`~openstack.session.Session`
        :returns: ``list``
        """
        url = utils.urljoin(self.base_path, self.id, 'host_info', 'processes')
        resp = session.get(url, endpoint_filter=self.service).json()
        return resp['info']

    def host_system(self, session):
        """Get system information about the host

        :param session: The session to use for making this request.
        :type session: :class:`~openstack.session.Session`
        :returns: ``list``
        """
        url = utils.urljoin(self.base_path, self.id, 'host_info', 'system')
        resp = session.get(url, endpoint_filter=self.service).json()
        return resp['info']

    def host_users(self, session):
        """Get information on users who are logged into the host

        :param session: The session to use for making this request.
        :type session: :class:`~openstack.session.Session`
        :returns: ``list``
        """
        url = utils.urljoin(self.base_path, self.id, 'host_info', 'who')
        resp = session.get(url, endpoint_filter=self.service).json()
        return resp['info']
