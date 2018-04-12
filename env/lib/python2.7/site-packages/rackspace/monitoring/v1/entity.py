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


class Entity(resource.Resource):
    base_path = 'entities'
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
    #: Agent to which this entity is bound
    agent_id = resource.prop('agent_id')
    #: Creation timestamp.
    #: Time is shown in Coordinated Universal Time (UTC) as the number
    #: of milliseconds that have elapsed since January 1, 1970. *Type: int*
    created_at = resource.prop('created_at', type=int)
    #: Dictionary of IP addresses that can be referenced by
    #: checks on this entity. *Type: dict*
    ip_addresses = resource.prop('ip_addresses', type=dict)
    #: Indicates if this entity is managed
    #: by Rackspace Managed Cloud. *Type: bool*
    is_managed = resource.prop('managed', type=format.BoolStr)
    #: Arbitrary key/value pairs. *Type: dict*
    metadata = resource.prop('metadata', type=dict)
    #: A friendly label for the entity
    name = resource.prop('label')
    #: List of scheduled suppressions. *Type: list*
    scheduled_suppressions = resource.prop('scheduled_suppressions', type=list)
    #: Update timestamp.
    #: Time is shown in Coordinated Universal Time (UTC) as the number
    #: of milliseconds that have elapsed since January 1, 1970. *Type: int*
    updated_at = resource.prop('updated_at', type=int)
    #: The Rackspace Cloud identifier of this entity.
    #: Only applies to Rackspace Cloud servers.
    uri = resource.prop('uri')

    def alarm_changelog(self, session):
        """Return alarm changelog for the entity

        :param session: The session to use for making this request.
        :type session: :class:`~openstack.session.Session`
        :returns: ``list``
        """
        url = utils.urljoin('changelogs', 'alarms?entityId=' + self.id)
        resp = session.get(url, endpoint_filter=self.service).json()
        return resp['values']

    def test_alarm(self, session, check_data, criteria):
        """Test an alarm

        Post alarm criteria and alarm data to test whether the alarm criteria
        is valid and to show how the alarm state is evaluated.

        The response not only provides the final evaluated state, but also
        includes all state transitions noticed during the calculation.
        You need to provide one or more observations.

        An observation consists of a set of metrics from a single data center.
        A group of observations consist of a set of metrics from more than one
        data center. When you test an alarm, you provide a list of check data,
        which you can retrieve from a test check operation.

        :param check_data: Metrics to check.
        :param criteria: The alarm DSL for describing alerting conditions.
        :param session: The session to use for making this request.
        :type session: :class:`~openstack.session.Session`
        :returns: ``list``
        """
        body = {"criteria": criteria, "check_data": check_data}
        url = utils.urljoin(self.base_path, self.id, 'test-alarm')
        return session.post(url, service=self.service, json=body).body

    def test_new_check(self, session, attributes):
        """Test a new check

        This operation causes Rackspace Cloud Monitoring to attempt to run the
        check on the specified monitoring zones and return the results.
        It allows you to test the check parameters in a single step before the
        check is actually created in the system.

        For the `remote.http` this call also includes debug information and the
        response body. Note: Only the first 512KB of the response body is read.
        If the response body is longer, it is truncated to 512KB.

        It requires a valid set of attributes from the checks attributes table.
        For a tutorial on creating some basic checks, see "Create checks" in
        the "Rackspace Cloud Monitoring Getting Started Guide".

        You can copy the results of a test check response and paste it directly
        into a test alarm.

        :param attributes: Valid set of attributes for check creation.
        :param session: The session to use for making this request.
        :type session: :class:`~openstack.session.Session`
        :returns: ``list``
        """
        url = utils.urljoin(self.base_path, self.id, 'test-check')
        return session.post(url, service=self.service, json=attributes).body
