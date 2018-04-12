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
from openstack import resource
from rackspace.monitoring.v1 import agent as _agent
from rackspace.monitoring.v1 import agent_token as _agent_token
from rackspace.monitoring.v1 import alarm as _alarm
from rackspace.monitoring.v1 import check as _check
from rackspace.monitoring.v1 import check_type as _check_type
from rackspace.monitoring.v1 import entity as _entity
from rackspace.monitoring.v1 import monitoring_zone as _monitoring_zone
from rackspace.monitoring.v1 import notification as _notification
from rackspace.monitoring.v1 import notification_plan as _notification_plan
from rackspace.monitoring.v1 import notification_type as _notification_type
from rackspace.monitoring.v1 import overview as _overview
from rackspace.monitoring.v1 import suppression as _suppression
from rackspace.monitoring.v1 import suppression_log as _suppression_log


class Proxy(proxy.BaseProxy):

    def agents(self, **query):
        """Return a generator of agents

        :param kwargs \*\*query: Optional query parameters to be sent to limit
                                 the resources being returned.

        :returns: A generator of agent objects
        :rtype: :class:`~rackspace.monitoring.v1.agent.Agent`
        """
        return self._list(_agent.Agent, paginated=False, **query)

    def agent_connections(self, agent):
        """List currently active connections for the agent

        :param agent: The value can be the ID of an agent or an instance of
                      :class:`~rackspace.monitoring.v1.agent.Agent`.

        :returns: ``list``
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        agent = _agent.Agent.from_id(agent)
        return agent.connections(self.session)

    def agent_host_info_types(self, agent):
        """List the types of host info data supported by the agent

        :param agent: The value can be the ID of an agent or an instance of
                      :class:`~rackspace.monitoring.v1.agent.Agent`.

        :returns: ``list``
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        agent = _agent.Agent.from_id(agent)
        return agent.host_info_types(self.session)

    def agent_host_cpus(self, agent):
        """Get information about the host CPUs

        :param agent: The value can be the ID of an agent or an instance of
                      :class:`~rackspace.monitoring.v1.agent.Agent`.

        :returns: ``list``
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        agent = _agent.Agent.from_id(agent)
        return agent.host_cpus(self.session)

    def agent_host_disks(self, agent):
        """Get information about the host disks

        :param agent: The value can be the ID of an agent or an instance of
                      :class:`~rackspace.monitoring.v1.agent.Agent`.

        :returns: ``list``
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        agent = _agent.Agent.from_id(agent)
        return agent.host_disks(self.session)

    def agent_host_filesystems(self, agent):
        """Get information about the host filesystems

        :param agent: The value can be the ID of an agent or an instance of
                      :class:`~rackspace.monitoring.v1.agent.Agent`.

        :returns: ``list``
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        agent = _agent.Agent.from_id(agent)
        return agent.host_filesystems(self.session)

    def agent_host_memory(self, agent):
        """Get information about the host memory

        :param agent: The value can be the ID of an agent or an instance of
                      :class:`~rackspace.monitoring.v1.agent.Agent`.

        :returns: ``list``
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        agent = _agent.Agent.from_id(agent)
        return agent.host_memory(self.session)

    def agent_host_nics(self, agent):
        """Get information about the host network interfaces

        :param agent: The value can be the ID of an agent or an instance of
                      :class:`~rackspace.monitoring.v1.agent.Agent`.

        :returns: ``list``
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        agent = _agent.Agent.from_id(agent)
        return agent.host_nics(self.session)

    def agent_host_processes(self, agent):
        """Get information about the host running processes

        :param agent: The value can be the ID of an agent or an instance of
                      :class:`~rackspace.monitoring.v1.agent.Agent`.

        :returns: ``list``
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        agent = _agent.Agent.from_id(agent)
        return agent.host_processes(self.session)

    def agent_host_system(self, agent):
        """Get system information about the host

        :param agent: The value can be the ID of an agent or an instance of
                      :class:`~rackspace.monitoring.v1.agent.Agent`.

        :returns: ``list``
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        agent = _agent.Agent.from_id(agent)
        return agent.host_system(self.session)

    def agent_host_users(self, agent):
        """Get information on users who are logged into the host

        :param agent: The value can be the ID of an agent or an instance of
                      :class:`~rackspace.monitoring.v1.agent.Agent`.

        :returns: ``list``
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        agent = _agent.Agent.from_id(agent)
        return agent.host_users(self.session)

    def find_agent(self, name_or_id, ignore_missing=True):
        """Find a single agent

        :param name_or_id: The value can be the ID of an agent or an instance
                           of :class:`~rackspace.monitoring.v1.agent.Agent`.
        :param bool ignore_missing: When set to ``False``
            :class:`~openstack.exceptions.ResourceNotFound` will be raised when
            the resource does not exist. When set to ``True``, ``None`` will be
            returned when attempting to find a nonexistent resource.

        :returns: One :class:`~rackspace.monitoring.v1.agent.Agent` or `None`
        """
        return self._find(_agent.Agent, name_or_id,
                          ignore_missing=ignore_missing)

    def get_agent(self, agent):
        """Get a single agent

        :param agent: The value can be the ID of an agent or an instance of
                      :class:`~rackspace.monitoring.v1.agent.Agent`.

        :returns: One :class:`~rackspace.monitoring.v1.agent.Agent`
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(_agent.Agent, agent)

    def agent_tokens(self, **query):
        """Return a generator of agent tokens

        :param kwargs \*\*query: Optional query parameters to be sent to limit
                                 the resources being returned.

        :returns: A generator of agent token objects
        :rtype: :class:`~rackspace.monitoring.v1.agent_token.AgentToken`
        """
        return self._list(_agent_token.AgentToken, paginated=False, **query)

    def create_agent_token(self, **attrs):
        """Create a new agent token from attributes

        :param dict attrs: Keyword arguments which will be used to create a
            :class:`~rackspace.monitoring.v1.agent_token.AgentToken` instance,
            comprised of the properties on the AgentToken class.

        :returns: The results of agent token creation
        :rtype: :class:`~rackspace.monitoring.v1.agent_token.AgentToken`
        """
        return self._create(_agent_token.AgentToken, **attrs)

    def delete_agent_token(self, agent_token, ignore_missing=True):
        """Delete a agent token

        :param agent_token: The value can be the ID of an agent token or a
            :class:`~rackspace.monitoring.v1.agent_token.AgentToken` instance.
        :param bool ignore_missing: When set to ``False``
            :class:`~openstack.exceptions.ResourceNotFound` will be raised when
            the resource does not exist. When set to ``True``, ``None`` will be
            returned when attempting to find a nonexistent resource.

        :returns: ``None``
        """
        self._delete(_agent_token.AgentToken, agent_token,
                     ignore_missing=ignore_missing)

    def find_agent_token(self, name_or_id, ignore_missing=True):
        """Find a single agent token

        :param name_or_id: The name or ID of an agent token.
        :param bool ignore_missing: When set to ``False``
            :class:`~openstack.exceptions.ResourceNotFound` will be raised when
            the resource does not exist. When set to ``True``, ``None`` will be
            returned when attempting to find a nonexistent resource.

        :returns: One :class:`~rackspace.monitoring.v1
                               .agent_token.AgentToken` or `None`
        """
        return self._find(_agent_token.AgentToken, name_or_id,
                          ignore_missing=ignore_missing)

    def get_agent_token(self, agent_token):
        """Get a single agent token

        :param agent_token: The value can be the ID of an agent token or a
            :class:`~rackspace.monitoring.v1.agent_token.AgentToken` instance.

        :returns: One :class:`~rackspace.monitoring
                               .v1.agent_token.AgentToken`
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(_agent_token.AgentToken, agent_token)

    def update_agent_token(self, agent_token, **attrs):
        """Update a agent token

        :param agent_token: The value can be the ID of an agent token or a
            :class:`~rackspace.monitoring.v1.agent_token.AgentToken` instance.
        :attrs kwargs: The attributes to update on the instance represented
                       by ``agent_token``.

        :returns: The updated agent token
        :rtype: :class:`~rackspace.monitoring.v1.agent_token.AgentToken`
        """
        return self._update(_agent_token.AgentToken, agent_token, **attrs)

    def alarms(self, entity, **query):
        """Return a generator of alarms for an entity

        :param entity: The value can be either the ID of an entity or a
            :class:`~rackspace.monitoring.v1.entity.Entity` instance.
        :param kwargs \*\*query: Optional query parameters to be sent to limit
                                 the resources being returned.

        :returns: A generator of alarm objects
        :rtype: :class:`~rackspace.monitoring.v1.alarm.Alarm`
        """
        entity_id = resource.Resource.get_id(entity)
        return self._list(_alarm.Alarm, path_args={'entity_id': entity_id},
                          paginated=False, **query)

    def alarm_changelog(self, entity):
        """Return alarm changelog for an entity

        :param entity: The value can be either the ID of an entity or a
            :class:`~rackspace.monitoring.v1.entity.Entity` instance.

        :returns: ``list``
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        entity = _entity.Entity.from_id(entity)
        return entity.alarm_changelog(self.session)

    def alarm_notification_history(self, alarm):
        """Lists alarm notification history for the alarm

        :param alarm: The value can be either the ID of an alarm or a
                      :class:`~rackspace.monitoring.v1.alarm.Alarm` instance.

        :returns: ``list``
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        alarm = _alarm.Alarm.from_id(alarm)
        return alarm.notification_history(self.session)

    def create_alarm(self, entity, **attrs):
        """Create a new alarm from attributes

        :param entity: The value can be either the ID of an entity or a
             :class:`~rackspace.monitoring.v1.entity.Entity` instance.
        :param dict attrs: Keyword arguments which will be used to create a
                           :class:`~rackspace.monitoring.v1.alarm.Alarm`,
                           comprised of the properties on the Alarm class.

        :returns: The results of alarm creation
        :rtype: :class:`~rackspace.monitoring.v1.alarm.Alarm`
        """
        entity_id = resource.Resource.get_id(entity)
        return self._create(_alarm.Alarm,
                            path_args={'entity_id': entity_id}, **attrs)

    def delete_alarm(self, alarm, entity=None, ignore_missing=True):
        """Delete a alarm

        :param alarm: The value can be either the ID of an alarm or a
                      :class:`~rackspace.monitoring.v1.alarm.Alarm` instance.
        :param entity: The value can be either the ID of an entity or a
            :class:`~rackspace.monitoring.v1.entity.Entity` instance.
            Needs to be specified when an ID is given for `alarm`.
        :param bool ignore_missing: When set to ``False``
            :class:`~openstack.exceptions.ResourceNotFound` will be raised when
            the resource does not exist. When set to ``True``, ``None`` will be
            returned when attempting to find a nonexistent resource.

        :returns: ``None``
        """
        if isinstance(alarm, _alarm.Alarm):
            entity_id = alarm.entity_id
        else:
            entity_id = resource.Resource.get_id(entity)
        self._delete(_alarm.Alarm, alarm, path_args={'entity_id': entity_id},
                     ignore_missing=ignore_missing)

    def find_alarm(self, name_or_id, entity=None, ignore_missing=True):
        """Find a single alarm for a given entity

        :param name_or_id: The name or ID of an alarm.
        :param entity: The value can be either the ID of an entity or a
            :class:`~rackspace.monitoring.v1.entity.Entity` instance.
            Needs to be specified when an ID is given for `alarm`.
        :param bool ignore_missing: When set to ``False``
            :class:`~openstack.exceptions.ResourceNotFound` will be raised when
            the resource does not exist. When set to ``True``, ``None`` will be
            returned when attempting to find a nonexistent resource.

        :returns: One :class:`~rackspace.monitoring.v1.alarm.Alarm` or `None`
        """
        if isinstance(entity, _entity.Entity):
            entity_id = entity.id
        else:
            entity_id = resource.Resource.get_id(entity)
        return self._find(_alarm.Alarm, name_or_id,
                          path_args={'entity_id': entity_id},
                          ignore_missing=ignore_missing)

    def get_alarm(self, alarm, entity=None):
        """Get a single alarm

        :param alarm: The value can be either the ID of an alarm or a
                      :class:`~rackspace.monitoring.v1.alarm.Alarm` instance.
        :param entity: The value can be either the ID of an entity or a
            :class:`~rackspace.monitoring.v1.entity.Entity` instance.
            Needs to be specified when an ID is given for `alarm`.

        :returns: One :class:`~rackspace.monitoring.v1.alarm.Alarm`
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        if isinstance(alarm, _alarm.Alarm):
            entity_id = alarm.entity_id
        else:
            entity_id = resource.Resource.get_id(entity)
        return self._get(_alarm.Alarm, alarm,
                         path_args={'entity_id': entity_id})

    def update_alarm(self, alarm, entity=None, **attrs):
        """Update a alarm

        :param alarm: The value can be either the ID of an alarm or a
                      :class:`~rackspace.monitoring.v1.alarm.Alarm` instance.
        :param entity: The value can be either the ID of an entity or a
            :class:`~rackspace.monitoring.v1.entity.Entity` instance.
            Needs to be specified when an ID is given for `alarm`.

        :returns: The updated alarm
        :rtype: :class:`~rackspace.monitoring.v1.alarm.Alarm`
        """
        if isinstance(alarm, _alarm.Alarm):
            entity_id = alarm.entity_id
        else:
            entity_id = resource.Resource.get_id(entity)
        return self._update(_alarm.Alarm, alarm,
                            path_args={'entity_id': entity_id}, **attrs)

    def checks(self, entity, **query):
        """Return a generator of checks for an entity

        :param entity: The value can be either the ID of an entity or a
            :class:`~rackspace.monitoring.v1.entity.Entity` instance.
        :param kwargs \*\*query: Optional query parameters to be sent to limit
                                 the resources being returned.

        :returns: A generator of checks objects
        :rtype: :class:`~rackspace.monitoring.v1.check.Check`
        """
        entity = _entity.Entity.from_id(entity)
        checks = _check.Check.list(self.session,
                                   path_args={"entity_id": entity.id}, **query)

        # Checks have to know their entity at this point, otherwise further
        # operations like getting their metrics or testing them is a hassle
        # because the end-user would have to maintain both
        # the entity and the object separately.
        for check in checks:
            check.entity_id = entity.id
            yield check

    def _get_entity_id(self, check, entity):
        if isinstance(check, _check.Check):
            if check.entity_id is not None:
                return check.entity_id
        if entity is not None:
            entity = _entity.Entity.from_id(entity)
            return entity.id

        raise ValueError("entity must be specified")

    def check_metrics(self, check, entity=None):
        """List metrics for the check

        :param check: The value can be either the ID of a check or
                      a :class:`~rackspace.monitoring.v1.check.Check` instance.
        :param entity: The value can be either the ID of an entity or a
            :class:`~rackspace.monitoring.v1.entity.Entity` instance.
            Needs to be specified when an ID is given for `check`.

        :returns: ``list``
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        check = _check.Check.from_id(check)
        check.entity_id = self._get_entity_id(check, entity)
        return check.metrics(self.session)

    def check_test(self, check, entity=None):
        """Test an existing check

        :param check: The value can be either the ID of a check or
                      a :class:`~rackspace.monitoring.v1.check.Check` instance.
        :param entity: The value can be either the ID of an entity or a
            :class:`~rackspace.monitoring.v1.entity.Entity` instance.
            Needs to be specified when an ID is given for `check`.

        :returns: ``list``
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        check = _check.Check.from_id(check)
        check.entity_id = self._get_entity_id(check, entity)
        return check.test(self.session)

    def create_check(self, entity, **attrs):
        """Create a new check for an entity from attributes

        :param entity: The value can be either the ID of an entity or a
            :class:`~rackspace.monitoring.v1.entity.Entity` instance.
        :param dict attrs: Keyword arguments which will be used to create a
                           :class:`~rackspace.monitoring.v1.check.Check`,
                           comprised of the properties on the Check class.

        :returns: The results of check creation
        :rtype: :class:`~rackspace.monitoring.v1.check.Check`
        """
        entity_id = resource.Resource.get_id(entity)
        return self._create(_check.Check,
                            path_args={'entity_id': entity_id}, **attrs)

    def delete_check(self, check, entity=None, ignore_missing=True):
        """Delete a check

        :param check: The value can be either the ID of a check or
                      a :class:`~rackspace.monitoring.v1.check.Check` instance.
        :param entity: The value can be either the ID of an entity or a
            :class:`~rackspace.monitoring.v1.entity.Entity` instance.
        :param bool ignore_missing: When set to ``False``
            :class:`~openstack.exceptions.ResourceNotFound` will be raised when
            the resource does not exist. When set to ``True``, ``None`` will be
            returned when attempting to find a nonexistent resource.

        :returns: ``None``
        """
        entity_id = self._get_entity_id(check, entity)
        self._delete(_check.Check, check, path_args={'entity_id': entity_id},
                     ignore_missing=ignore_missing)

    def find_check(self, name_or_id, entity=None, ignore_missing=True):
        """Find a single check for a given entity

        :param name_or_id: The name or ID of an check.
        :param entity: The value can be either the ID of an entity or a
            :class:`~rackspace.monitoring.v1.entity.Entity` instance.
        :param bool ignore_missing: When set to ``False``
            :class:`~openstack.exceptions.ResourceNotFound` will be raised when
            the resource does not exist. When set to ``True``, ``None`` will be
            returned when attempting to find a nonexistent resource.

        :returns: One :class:`~rackspace.monitoring.v1.check.Check` or `None`
        """
        entity_id = self._get_entity_id(name_or_id, entity)
        return self._find(_check.Check, name_or_id,
                          path_args={'entity_id': entity_id},
                          ignore_missing=ignore_missing)

    def get_check(self, check, entity=None):
        """Get a single check

        :param check: The value can be either the ID of a check or
                      a :class:`~rackspace.monitoring.v1.check.Check` instance.
        :param entity: The value can be either the ID of an entity or a
            :class:`~rackspace.monitoring.v1.entity.Entity` instance.

        :returns: One :class:`~rackspace.monitoring.v1.check.Check`
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        entity_id = self._get_entity_id(check, entity)
        return self._get(_check.Check, check,
                         path_args={'entity_id': entity_id})

    def update_check(self, check, entity=None, **attrs):
        """Update a check

        :param check: The value can be either the ID of a check or
                      a :class:`~rackspace.monitoring.v1.check.Check` instance.
        :param entity: The value can be either the ID of an entity or a
            :class:`~rackspace.monitoring.v1.entity.Entity` instance.
        :attrs kwargs: The attributes to update on the instance represented
                       by ``check``.

        :returns: The updated check
        :rtype: :class:`~rackspace.monitoring.v1.check.Check`
        """
        entity_id = self._get_entity_id(check, entity)
        return self._update(_check.Check, check,
                            path_args={'entity_id': entity_id}, **attrs)

    def check_types(self, **query):
        """Return a generator of check types

        :param kwargs \*\*query: Optional query parameters to be sent to limit
                                 the resources being returned.

        :returns: A generator of check types objects
        :rtype: :class:`~rackspace.monitoring.v1.check_type.CheckType`
        """
        return self._list(_check_type.CheckType, paginated=False, **query)

    def check_type_targets(self, check_type, entity):
        """Lists agent check type targets for an entity

        :param check_type: The value can be either the ID of a check type or
            a :class:`~rackspace.monitoring.v1.check_type.CheckType` instance.
        :param entity: The value can be either the ID of an entity or a
            :class:`~rackspace.monitoring.v1.entity.Entity` instance.

        :returns: ``list``
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        check_type = _check_type.CheckType.from_id(check_type)

        if isinstance(entity, _entity.Entity):
            entity_id = entity.id
        else:
            entity_id = resource.Resource.get_id(entity)
        return check_type.targets(self.session, entity_id)

    def find_check_type(self, name_or_id, ignore_missing=True):
        """Find a single check type

        :param name_or_id: The name or ID of a check type.
        :param bool ignore_missing: When set to ``False``
            :class:`~openstack.exceptions.ResourceNotFound` will be raised when
            the resource does not exist. When set to ``True``, ``None`` will be
            returned when attempting to find a nonexistent resource.

        :returns: One :class:`~rackspace.monitoring.v1.check_type.CheckType`
                  or `None`
        """
        return self._find(_check_type.CheckType, name_or_id,
                          ignore_missing=ignore_missing)

    def get_check_type(self, check_type):
        """Get a single check type

        :param check_type: The value can be either the ID of a check type or
            a :class:`~rackspace.monitoring.v1.check_type.CheckType` instance.

        :returns: One :class:`~rackspace.monitoring.v1.check_type.CheckType`
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(_check_type.CheckType, check_type)

    def entities(self, **query):
        """Return a generator of entities

        :param kwargs \*\*query: Optional query parameters to be sent to limit
                                 the resources being returned.

        :returns: A generator of entity objects
        :rtype: :class:`~rackspace.monitoring.v1.entity.Entity`
        """
        return self._list(_entity.Entity, paginated=False, **query)

    def create_entity(self, **attrs):
        """Create a new entity from attributes

        :param dict attrs: Keyword arguments which will be used to create a
                           :class:`~rackspace.monitoring.v1.entity.Entity`,
                           comprised of the properties on the Entity class.

        :returns: The results of entity creation
        :rtype: :class:`~rackspace.monitoring.v1.entity.Entity`
        """
        return self._create(_entity.Entity, **attrs)

    def delete_entity(self, entity, ignore_missing=True):
        """Delete an entity

        :param entity: The value can be either the ID of an entity or a
            :class:`~rackspace.monitoring.v1.entity.Entity` instance.
        :param bool ignore_missing: When set to ``False``
            :class:`~openstack.exceptions.ResourceNotFound` will be raised when
            the resource does not exist. When set to ``True``, ``None`` will be
            returned when attempting to find a nonexistent resource.

        :returns: ``None``
        """
        self._delete(_entity.Entity, entity, ignore_missing=ignore_missing)

    def find_entity(self, name_or_id, ignore_missing=True):
        """Find a single entity

        :param name_or_id: The name or ID of an entity.
        :param bool ignore_missing: When set to ``False``
            :class:`~openstack.exceptions.ResourceNotFound` will be raised when
            the resource does not exist. When set to ``True``, ``None`` will be
            returned when attempting to find a nonexistent resource.

        :returns: One :class:`~rackspace.monitoring.v1.entity.Entity` or `None`
        """
        return self._find(_entity.Entity, name_or_id,
                          ignore_missing=ignore_missing)

    def get_entity(self, entity):
        """Get a single entity

        :param entity: The value can be either the ID of an entity or a
            :class:`~rackspace.monitoring.v1.entity.Entity` instance.

        :returns: One :class:`~rackspace.monitoring.v1.entity.Entity`
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(_entity.Entity, entity)

    def update_entity(self, entity, **attrs):
        """Update an entity

        :param entity: The value can be either the ID of an entity or a
            :class:`~rackspace.monitoring.v1.entity.Entity` instance.
        :attrs kwargs: The attributes to update on the instance represented
                       by ``entity``.

        :returns: The updated entity
        :rtype: :class:`~rackspace.monitoring.v1.entity.Entity`
        """
        return self._update(_entity.Entity, entity, **attrs)

    def monitoring_zones(self, **query):
        """Return a generator of monitoring zones

        :param kwargs \*\*query: Optional query parameters to be sent to limit
                                 the resources being returned.

        :returns: A generator of monitoring zone objects
        :rtype: :class:`~rackspace.monitoring
                         .v1.monitoring_zone.MonitoringZone`
        """
        return self._list(_monitoring_zone.MonitoringZone,
                          paginated=False, **query)

    def find_monitoring_zone(self, name_or_id, ignore_missing=True):
        """Find a single monitoring zone

        :param name_or_id: The name or ID of a monitoring zone.
        :param bool ignore_missing: When set to ``False``
            :class:`~openstack.exceptions.ResourceNotFound` will be raised when
            the resource does not exist. When set to ``True``, ``None`` will be
            returned when attempting to find a nonexistent resource.

        :returns: One :class:`~rackspace.monitoring
                               .v1.monitoring_zone.MonitoringZone` or `None`
        """
        return self._find(_monitoring_zone.MonitoringZone, name_or_id,
                          ignore_missing=ignore_missing)

    def get_monitoring_zone(self, monitoring_zone):
        """Get a single monitoring zone

        :param monitoring_zone: The value can be either the ID of a monitoring
                                zone or an instance of :class:`~rackspace
                                .monitoring.v1.monitoring_zone.MonitoringZone`
                                instance.

        :returns: One :class:`~rackspace.monitoring
                               .v1.monitoring_zone.MonitoringZone`
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(_monitoring_zone.MonitoringZone, monitoring_zone)

    def notifications(self, **query):
        """Return a generator of notifications

        :param kwargs \*\*query: Optional query parameters to be sent to limit
                                 the resources being returned.

        :returns: A generator of notification objects
        :rtype: :class:`~rackspace.monitoring.v1.notification.Notification`
        """
        return self._list(_notification.Notification, paginated=False, **query)

    def create_notification(self, **attrs):
        """Create a new notification from attributes

        :param dict attrs: Keyword arguments which will be used to create a
            :class:`~rackspace.monitoring.v1.notification.Notification`,
            comprised of the properties on the Notification class.

        :returns: The results of notification creation
        :rtype: :class:`~rackspace.monitoring.v1.notification.Notification`
        """
        return self._create(_notification.Notification, **attrs)

    def delete_notification(self, notification, ignore_missing=True):
        """Delete an notification

        :param notification: The value can be either the ID of a notification
            or a :class:`~rackspace.monitoring.v1.notification.Notification`
            instance.
        :param bool ignore_missing: When set to ``False``
            :class:`~openstack.exceptions.ResourceNotFound` will be raised when
            the resource does not exist. When set to ``True``, ``None`` will be
            returned when attempting to find a nonexistent resource.

        :returns: ``None``
        """
        self._delete(_notification.Notification, notification,
                     ignore_missing=ignore_missing)

    def find_notification(self, name_or_id, ignore_missing=True):
        """Find a single notification

        :param name_or_id: The name or ID of a notification.
        :param bool ignore_missing: When set to ``False``
            :class:`~openstack.exceptions.ResourceNotFound` will be raised when
            the resource does not exist. When set to ``True``, ``None`` will be
            returned when attempting to find a nonexistent resource.

        :returns: One :class:`~rackspace.monitoring
                               .v1.notification.Notification` or `None`
        """
        return self._find(_notification.Notification, name_or_id,
                          ignore_missing=ignore_missing)

    def get_notification(self, notification):
        """Get a single notification

        :param notification: The value can be the ID of a notification or
          :class:`~rackspace.monitoring.v1.notification.Notification` instance.

        :returns: One :class:`~rackspace.monitoring
                               .v1.notification.Notification`
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(_notification.Notification, notification)

    def update_notification(self, notification, **attrs):
        """Update an notification

        :param notification: The value can be the ID of a notification or
          :class:`~rackspace.monitoring.v1.notification.Notification` instance.
        :attrs kwargs: The attributes to update on the instance represented
                       by ``notification``.

        :returns: The updated notification
        :rtype: :class:`~rackspace.monitoring.v1.notification.Notification`
        """
        return self._update(_notification.Notification, notification, **attrs)

    def notification_plans(self, **query):
        """Return a generator of notification plans

        :param kwargs \*\*query: Optional query parameters to be sent to limit
                                 the resources being returned.

        :returns: A generator of notification plans objects
        :rtype: :class:`~rackspace.monitoring.v1
                         .notification_plan.NotificationPlan`
        """
        return self._list(_notification_plan.NotificationPlan,
                          paginated=False, **query)

    def create_notification_plan(self, **attrs):
        """Create a new notification plan from attributes

        :param dict attrs: Keyword arguments which will be used to create a
                           :class:`~rackspace.monitoring.v1.notification_plan
                           .NotificationPlan`, comprised of the properties on
                           the NotificationPlan class.

        :returns: The results of notification plan creation
        :rtype: :class:`~rackspace.monitoring
                         .v1.notification_plan.NotificationPlan`
        """
        return self._create(_notification_plan.NotificationPlan, **attrs)

    def delete_notification_plan(self, notification_plan, ignore_missing=True):
        """Delete a notification plan

        :param notification_plan: The value can be the ID of a notification
                                  plan or a :class:`~rackspace.monitoring.v1.
                                  notification_plan.NotificationPlan` instance.
        :param bool ignore_missing: When set to ``False``
            :class:`~openstack.exceptions.ResourceNotFound` will be raised when
            the resource does not exist. When set to ``True``, ``None`` will be
            returned when attempting to find a nonexistent resource.

        :returns: ``None``
        """
        self._delete(_notification_plan.NotificationPlan, notification_plan,
                     ignore_missing=ignore_missing)

    def find_notification_plan(self, name_or_id, ignore_missing=True):
        """Find a single notification plan

        :param name_or_id: The name or ID of a notification plan.
        :param bool ignore_missing: When set to ``False``
            :class:`~openstack.exceptions.ResourceNotFound` will be raised when
            the resource does not exist. When set to ``True``, ``None`` will be
            returned when attempting to find a nonexistent resource.

        :returns: One :class:`~rackspace.monitoring.v1.notification_plan
                               .NotificationPlan` or `None`
        """
        return self._find(_notification_plan.NotificationPlan, name_or_id,
                          ignore_missing=ignore_missing)

    def get_notification_plan(self, notification_plan):
        """Get a single notification plan

        :param notification_plan: The value can be the ID of a notification
                                  plan or a :class:`~rackspace.monitoring.v1.
                                  notification_plan.NotificationPlan` instance.

        :returns: One :class:`~rackspace.monitoring.v1.notification_plan
                               .NotificationPlan`
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(_notification_plan.NotificationPlan,
                         notification_plan)

    def update_notification_plan(self, notification_plan, **attrs):
        """Update an notification plan

        :param notification_plan: The value can be the ID of a notification
                                  plan or a :class:`~rackspace.monitoring.v1.
                                  notification_plan.NotificationPlan` instance.
        :attrs kwargs: The attributes to update on the instance represented
                       by ``notification_plan``.

        :returns: The updated notification plan
        :rtype: :class:`~rackspace.monitoring
                         .v1.notification_plan.NotificationPlan`
        """
        return self._update(_notification_plan.NotificationPlan,
                            notification_plan, **attrs)

    def notification_types(self, **query):
        """Return a generator of notification types

        :param kwargs \*\*query: Optional query parameters to be sent to limit
                                 the resources being returned.

        :returns: A generator of notification types objects
        :rtype: :class:`~rackspace.monitoring.v1
                         .notification_type.NotificationType`
        """
        return self._list(_notification_type.NotificationType,
                          paginated=False, **query)

    def find_notification_type(self, name_or_id, ignore_missing=True):
        """Find a single notification type

        :param name_or_id: The name or ID of a notification type.
        :param bool ignore_missing: When set to ``False``
            :class:`~openstack.exceptions.ResourceNotFound` will be raised when
            the resource does not exist. When set to ``True``, ``None`` will be
            returned when attempting to find a nonexistent resource.

        :returns: One :class:`~rackspace.monitoring.v1
                               .notification_type.NotificationType` or `None`
        """
        return self._find(_notification_type.NotificationType, name_or_id,
                          ignore_missing=ignore_missing)

    def get_notification_type(self, notification_type):
        """Get a single notification type

        :param notification_type The value can be the ID of a notification
                                  type or a :class:`~rackspace.monitoring.v1.
                                  notification_type.NotificationType` instance.

        :returns: One :class:`~rackspace.monitoring
                               .v1.notification_type.NotificationType`
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(_notification_type.NotificationType,
                         notification_type)

    def overviews(self, **query):
        """Return an overview of entities and their checks and alarms

        :param kwargs \*\*query: Optional query parameters to be sent to limit
                                 the resources being returned.

        :returns: A generator of overview objects
        :rtype: :class:`~rackspace.monitoring.v1.overview.Overview`
        """
        return self._list(_overview.Overview, paginated=False, **query)

    def test_alarm(self, entity, check_data, criteria):
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

        :param entity: The value can be either the ID of an entity or a
            :class:`~rackspace.monitoring.v1.entity.Entity` instance.
        :param check_data: Metrics to check.
        :param criteria: The alarm DSL for describing alerting conditions.

        :returns: ``list``
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        entity = _entity.Entity.from_id(entity)
        return entity.test_alarm(self.session, check_data, criteria)

    def test_new_check(self, entity, attributes):
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

        :param entity: The value can be either the ID of an entity or a
            :class:`~rackspace.monitoring.v1.entity.Entity` instance.
        :param attributes: Valid set of attributes for check creation.

        :returns: ``list``
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        entity = _entity.Entity.from_id(entity)
        return entity.test_new_check(self.session, attributes)

    def test_notification(self, notification):
        """Test a notification

        :param notification: The value can be the ID of a notification or
          :class:`~rackspace.monitoring.v1.notification.Notification` instance.

        :returns: ``list``
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        notification = _notification.Notification.from_id(notification)
        return notification.test(self.session)

    def traceroute(self, monitoring_zone, target, target_resolver="IPv4"):
        """Issue a traceroute from a monitoring zone to a host

        :param monitoring_zone: The value can be either the ID of a monitoring
                                zone or an instance of :class:`~rackspace
                                .monitoring.v1.monitoring_zone.MonitoringZone`
                                instance.
        :param str target: Hostname or IP address
        :param str target_resolver: `IPv4` or `IPv6`

        :returns: ``list``
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        monitoring_zone = (
            _monitoring_zone.MonitoringZone.from_id(monitoring_zone))
        return monitoring_zone.traceroute(self.session,
                                          target, target_resolver)

    def suppressions(self, **query):
        """Return a generator of suppressions

        :param kwargs \*\*query: Optional query parameters to be sent to limit
                                 the resources being returned.

        :returns: A generator of suppression objects
        :rtype: :class:`~rackspace.monitoring.v1.suppression.Suppression`
        """
        return self._list(_suppression.Suppression, paginated=False, **query)

    def create_suppression(self, **attrs):
        """Create a new suppression from attributes

        :param dict attrs: Keyword arguments which will be used to create a
            :class:`~rackspace.monitoring.v1.suppression.Suppression`,
            comprised of the properties on the NotificationType class.

        :returns: The results of suppression creation
        :rtype: :class:`~rackspace.monitoring.v1.suppression.Suppression`
        """
        return self._create(_suppression.Suppression, **attrs)

    def delete_suppression(self, suppression, ignore_missing=True):
        """Delete an suppression

        :param suppression: The value can be either the ID of a suppression or
            a :class:`~rackspace.monitoring.v1.suppression.Suppression`
            instance.
        :param bool ignore_missing: When set to ``False``
            :class:`~openstack.exceptions.ResourceNotFound` will be raised when
            the resource does not exist. When set to ``True``, ``None`` will be
            returned when attempting to find a nonexistent resource.

        :returns: ``None``
        """
        self._delete(_suppression.Suppression, suppression,
                     ignore_missing=ignore_missing)

    def find_suppression(self, name_or_id, ignore_missing=True):
        """Find a single suppression

        :param name_or_id: The name or ID of a suppression.
        :param bool ignore_missing: When set to ``False``
            :class:`~openstack.exceptions.ResourceNotFound` will be raised when
            the resource does not exist. When set to ``True``, ``None`` will be
            returned when attempting to find a nonexistent resource.

        :returns: One :class:`~rackspace.monitoring
                               .v1.suppression.Suppression` or `None`
        """
        return self._find(_suppression.Suppression, name_or_id,
                          ignore_missing=ignore_missing)

    def get_suppression(self, suppression):
        """Get a single suppression

        :param suppression: The value can be either the ID of a suppression or
            a :class:`~rackspace.monitoring.v1.suppression.Suppression`
            instance.

        :returns: One :class:`~rackspace.monitoring
                               .v1.suppression.Suppression`
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(_suppression.Suppression, suppression)

    def update_suppression(self, suppression, **attrs):
        """Update an suppression

        :param suppression: The value can be either the ID of a suppression or
            a :class:`~rackspace.monitoring.v1.suppression.Suppression`
            instance.
        :attrs kwargs: The attributes to update on the instance represented
                       by ``value``.

        :returns: The updated suppression
        :rtype: :class:`~rackspace.monitoring.v1.suppression.Suppression`
        """
        return self._update(_suppression.Suppression, suppression, **attrs)

    def suppression_logs(self, **query):
        """Return a generator of suppression logs

        :param kwargs \*\*query: Optional query parameters to be sent to limit
                                 the resources being returned.

        :returns: A generator of suppression log objects
        :rtype: :class:`~rackspace.monitoring
                         .v1.suppression_log.SuppressionLog`
        """
        return self._list(_suppression_log.SuppressionLog,
                          paginated=False, **query)

    def find_suppression_log(self, name_or_id, ignore_missing=True):
        """Find a single suppression log

        :param name_or_id: The name or ID of a suppression log.
        :param bool ignore_missing: When set to ``False``
            :class:`~openstack.exceptions.ResourceNotFound` will be raised when
            the resource does not exist. When set to ``True``, ``None`` will be
            returned when attempting to find a nonexistent resource.

        :returns: One :class:`~rackspace.monitoring
                               .v1.suppression_log.SuppressionLog` or `None`
        """
        return self._find(_suppression_log.SuppressionLog, name_or_id,
                          ignore_missing=ignore_missing)
