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

from openstack.tests.unit import test_proxy_base
from rackspace.monitoring.v1 import _proxy

from rackspace.monitoring.v1 import agent
from rackspace.monitoring.v1 import agent_token
from rackspace.monitoring.v1 import alarm
from rackspace.monitoring.v1 import check
from rackspace.monitoring.v1 import check_type
from rackspace.monitoring.v1 import entity
from rackspace.monitoring.v1 import monitoring_zone
from rackspace.monitoring.v1 import notification
from rackspace.monitoring.v1 import notification_plan
from rackspace.monitoring.v1 import notification_type
from rackspace.monitoring.v1 import overview
from rackspace.monitoring.v1 import suppression
from rackspace.monitoring.v1 import suppression_log


class TestMonitoringProxy(test_proxy_base.TestProxyBase):

    def setUp(self):
        super(TestMonitoringProxy, self).setUp()
        self.proxy = _proxy.Proxy(self.session)

    def test_agents(self):
        self.verify_list(self.proxy.agents, agent.Agent, paginated=False)

    def test_agent_connections(self):
        self._verify("rackspace.monitoring.v1.agent.Agent.connections",
                     self.proxy.agent_connections, method_args=["value"])

    def test_agent_host_info_types(self):
        self._verify("rackspace.monitoring.v1.agent.Agent.host_info_types",
                     self.proxy.agent_host_info_types, method_args=["value"])

    def test_agent_host_cpus(self):
        self._verify("rackspace.monitoring.v1.agent.Agent.host_cpus",
                     self.proxy.agent_host_cpus, method_args=["value"])

    def test_agent_host_disks(self):
        self._verify("rackspace.monitoring.v1.agent.Agent.host_disks",
                     self.proxy.agent_host_disks, method_args=["value"])

    def test_agent_host_filesystems(self):
        self._verify("rackspace.monitoring.v1.agent.Agent.host_filesystems",
                     self.proxy.agent_host_filesystems, method_args=["value"])

    def test_agent_host_memory(self):
        self._verify("rackspace.monitoring.v1.agent.Agent.host_memory",
                     self.proxy.agent_host_memory, method_args=["value"])

    def test_agent_host_nics(self):
        self._verify("rackspace.monitoring.v1.agent.Agent.host_nics",
                     self.proxy.agent_host_nics, method_args=["value"])

    def test_agent_host_processes(self):
        self._verify("rackspace.monitoring.v1.agent.Agent.host_processes",
                     self.proxy.agent_host_processes, method_args=["value"])

    def test_agent_host_system(self):
        self._verify("rackspace.monitoring.v1.agent.Agent.host_system",
                     self.proxy.agent_host_system, method_args=["value"])

    def test_agent_host_users(self):
        self._verify("rackspace.monitoring.v1.agent.Agent.host_users",
                     self.proxy.agent_host_users, method_args=["value"])

    def test_agent_find(self):
        self.verify_find(self.proxy.find_agent, agent.Agent)

    def test_agent_get(self):
        self.verify_get(self.proxy.get_agent, agent.Agent)

    def test_agent_tokens(self):
        self.verify_list(
            self.proxy.agent_tokens, agent_token.AgentToken, paginated=False)

    def test_agent_token_create(self):
        self.verify_create(
            self.proxy.create_agent_token, agent_token.AgentToken)

    def test_agent_token_delete(self):
        self.verify_delete(
            self.proxy.delete_agent_token, agent_token.AgentToken, False)

    def test_agent_token_delete_ignore(self):
        self.verify_delete(
            self.proxy.delete_agent_token, agent_token.AgentToken, True)

    def test_agent_token_find(self):
        self.verify_find(self.proxy.find_agent_token, agent_token.AgentToken)

    def test_agent_token_get(self):
        self.verify_get(self.proxy.get_agent_token, agent_token.AgentToken)

    def test_agent_token_update(self):
        self.verify_update(
            self.proxy.update_agent_token, agent_token.AgentToken)

    def test_alarms(self):
        self.verify_list(
            self.proxy.alarms, alarm.Alarm, paginated=False,
            method_args=["test_id"],
            expected_kwargs={"path_args": {"entity_id": "test_id"}})

    def test_alarm_changelog(self):
        self._verify(
            "rackspace.monitoring.v1.entity.Entity.alarm_changelog",
            self.proxy.alarm_changelog, method_args=["value"])

    def test_alarm_notification_history(self):
        self._verify(
            "rackspace.monitoring.v1.alarm.Alarm.notification_history",
            self.proxy.alarm_notification_history, method_args=["value"])

    def test_alarm_create(self):
        self.verify_create(
            self.proxy.create_alarm, alarm.Alarm,
            method_kwargs={"entity": "test_id"},
            expected_kwargs={"path_args": {"entity_id": "test_id"}})

    def test_alarm_delete(self):
        test_alarm = alarm.Alarm.from_id("test_alarm_id")
        test_alarm.entity_id = "test_entity_id"

        # Case1: Alarm instance is provided as value
        self._verify2("openstack.proxy.BaseProxy._delete",
                      self.proxy.delete_alarm,
                      method_args=[test_alarm, "test_entity_id"],
                      expected_args=[alarm.Alarm, test_alarm],
                      expected_kwargs={"path_args": {
                          "entity_id": "test_entity_id"},
                          "ignore_missing": True})

        # Case2: Alarm ID is provided as value
        self._verify2("openstack.proxy.BaseProxy._delete",
                      self.proxy.delete_alarm,
                      method_args=["test_alarm_id", "test_entity_id"],
                      expected_args=[alarm.Alarm, "test_alarm_id"],
                      expected_kwargs={"path_args": {
                          "entity_id": "test_entity_id"},
                          "ignore_missing": True})

    def test_alarm_delete_ignore(self):
        self.verify_delete(
            self.proxy.delete_alarm, alarm.Alarm, True,
            {"entity": "test_id"}, {"entity_id": "test_id"})

    def test_alarm_find(self):
        test_alarm = alarm.Alarm.from_id("test_alarm_id")
        test_alarm.entity_id = "test_entity_id"

        # Case1: Alarm instance is provided as value
        self._verify2("openstack.proxy.BaseProxy._find",
                      self.proxy.find_alarm,
                      method_args=[test_alarm, "test_entity_id"],
                      expected_args=[alarm.Alarm, test_alarm],
                      expected_kwargs={"path_args": {
                                       "entity_id": "test_entity_id"},
                                       "ignore_missing": True})

        # Case2: Alarm ID is provided as value
        self._verify2("openstack.proxy.BaseProxy._find",
                      self.proxy.find_alarm,
                      method_args=["test_alarm_id", "test_entity_id"],
                      expected_args=[alarm.Alarm, "test_alarm_id"],
                      expected_kwargs={"path_args": {
                                       "entity_id": "test_entity_id"},
                                       "ignore_missing": True})

    def test_alarm_get(self):
        test_alarm = alarm.Alarm.from_id("test_alarm_id")
        test_alarm.entity_id = "test_entity_id"

        # Case1: Alarm instance is provided as value
        self._verify2("openstack.proxy.BaseProxy._get",
                      self.proxy.get_alarm,
                      method_args=[test_alarm, "test_entity_id"],
                      expected_args=[alarm.Alarm, test_alarm],
                      expected_kwargs={"path_args": {
                          "entity_id": "test_entity_id"}})

        # Case2: Alarm ID is provided as value
        self._verify2("openstack.proxy.BaseProxy._get",
                      self.proxy.get_alarm,
                      method_args=["test_alarm_id", "test_entity_id"],
                      expected_args=[alarm.Alarm, "test_alarm_id"],
                      expected_kwargs={"path_args": {
                          "entity_id": "test_entity_id"}})

    def test_alarm_update(self):
        test_alarm = alarm.Alarm.from_id("test_alarm_id")
        test_alarm.entity_id = "test_entity_id"

        # Case1: Alarm instance is provided as value
        self._verify2("openstack.proxy.BaseProxy._update",
                      self.proxy.update_alarm,
                      method_args=[test_alarm, "test_entity_id"],
                      expected_args=[alarm.Alarm, test_alarm],
                      expected_kwargs={"path_args": {
                          "entity_id": "test_entity_id"}})

        # Case2: Alarm ID is provided as value
        self._verify2("openstack.proxy.BaseProxy._update",
                      self.proxy.update_alarm,
                      method_args=["test_alarm_id", "test_entity_id"],
                      expected_args=[alarm.Alarm, "test_alarm_id"],
                      expected_kwargs={"path_args": {
                          "entity_id": "test_entity_id"}})

    def test_checks(self):
        test_entity = "test_entity_id"
        checks_body = []

        for i in range(3):
            checks_body.append({"name": "object%d" % i})

        # Returned check bodies have their entity inserted.
        returned_checks = []
        for chk in checks_body:
            chk["entity_id"] = test_entity
            returned_checks.append(chk)
        self.assertEqual(len(checks_body), len(returned_checks))

    def test_check_metrics(self):
        test_check = check.Check.from_id("test_check_id")
        test_check.entity_id = "test_entity_id"

        self._verify(
            "rackspace.monitoring.v1.check.Check.metrics",
            self.proxy.check_metrics, method_args=[test_check])

    def test_check_test(self):
        test_check = check.Check.from_id("test_check_id")
        test_check.entity_id = "test_entity_id"

        self._verify(
            "rackspace.monitoring.v1.check.Check.test",
            self.proxy.check_test, method_args=[test_check])

    def test_check_create(self):
        self.verify_create(
            self.proxy.create_check, check.Check,
            method_kwargs={"entity": "test_id"},
            expected_kwargs={"path_args": {"entity_id": "test_id"}})

    def test_check_delete(self):
        self.verify_delete(
            self.proxy.delete_check, check.Check, False,
            {"entity": "test_id"}, {"entity_id": "test_id"})

    def test_check_delete_ignore(self):
        self.verify_delete(
            self.proxy.delete_check, check.Check, True,
            {"entity": "test_id"}, {"entity_id": "test_id"})

    def test_check_find(self):
        test_check = check.Check.from_id("test_check_id")
        test_entity = "test_entity_id"

        # Case1: Check instance is provided as value
        self._verify2("openstack.proxy.BaseProxy._find",
                      self.proxy.find_check,
                      method_args=[test_check, test_entity],
                      expected_args=[check.Check, test_check],
                      expected_kwargs={"path_args": {
                                       "entity_id": test_entity},
                                       "ignore_missing": True})

        # Case2: Check ID is provided as value
        self._verify2("openstack.proxy.BaseProxy._find",
                      self.proxy.find_check,
                      method_args=["test_check_id", test_entity],
                      expected_args=[check.Check, "test_check_id"],
                      expected_kwargs={"path_args": {
                                       "entity_id": test_entity},
                                       "ignore_missing": True})

    def test_check_get(self):
        test_check = check.Check.from_id("test_check_id")
        test_entity = "test_entity_id"

        # Case1: Check instance is provided as value
        self._verify2("openstack.proxy.BaseProxy._get",
                      self.proxy.get_check,
                      method_args=[test_check, test_entity],
                      expected_args=[check.Check, test_check],
                      expected_kwargs={"path_args": {
                                       "entity_id": test_entity}})

        # Case2: Check ID is provided as value
        self._verify2("openstack.proxy.BaseProxy._get",
                      self.proxy.get_check,
                      method_args=["test_check_id", test_entity],
                      expected_args=[check.Check, "test_check_id"],
                      expected_kwargs={"path_args": {
                                       "entity_id": test_entity}})

    def test_check_update(self):
        test_check = check.Check.from_id("test_check_id")
        test_entity = "test_entity_id"

        # Case1: Check instance is provided as value
        self._verify2("openstack.proxy.BaseProxy._update",
                      self.proxy.update_check,
                      method_args=[test_check, test_entity],
                      expected_args=[check.Check, test_check],
                      expected_kwargs={"path_args": {
                                       "entity_id": test_entity}})

        # Case2: Check ID is provided as value
        self._verify2("openstack.proxy.BaseProxy._update",
                      self.proxy.update_check,
                      method_args=["test_check_id", test_entity],
                      expected_args=[check.Check, "test_check_id"],
                      expected_kwargs={"path_args": {
                                       "entity_id": test_entity}})

    def test_check_types(self):
        self.verify_list(self.proxy.check_types, check_type.CheckType,
                         paginated=False)

    def test_check_type_targets(self):
        test_checktype = check_type.CheckType.from_id("test_checktype_id")
        test_entity = "test_entity_id"

        # Case1: CheckType instance is provided as value
        self._verify("rackspace.monitoring.v1.check_type.CheckType.targets",
                     self.proxy.check_type_targets,
                     method_args=[test_checktype, test_entity],
                     expected_args=[test_entity])

        # Case2: CheckType ID is provided as value
        self._verify("rackspace.monitoring.v1.check_type.CheckType.targets",
                     self.proxy.check_type_targets,
                     method_args=["test_checktype_id", test_entity],
                     expected_args=[test_entity])

    def test_check_type_find(self):
        self.verify_find(self.proxy.find_check_type, check_type.CheckType)

    def test_check_type_get(self):
        self.verify_get(self.proxy.get_check_type, check_type.CheckType)

    def test_entities(self):
        self.verify_list(self.proxy.entities, entity.Entity, paginated=False)

    def test_entity_create(self):
        self.verify_create(self.proxy.create_entity, entity.Entity)

    def test_entity_delete(self):
        self.verify_delete(self.proxy.delete_entity, entity.Entity, False)

    def test_entity_delete_ignore(self):
        self.verify_delete(self.proxy.delete_entity, entity.Entity, True)

    def test_entity_find(self):
        self.verify_find(self.proxy.find_entity, entity.Entity)

    def test_entity_get(self):
        self.verify_get(self.proxy.get_entity, entity.Entity)

    def test_entity_update(self):
        self.verify_update(self.proxy.update_entity, entity.Entity)

    def test_monitoring_zones(self):
        self.verify_list(self.proxy.monitoring_zones,
                         monitoring_zone.MonitoringZone, paginated=False)

    def test_monitoring_zone_find(self):
        self.verify_find(self.proxy.find_monitoring_zone,
                         monitoring_zone.MonitoringZone)

    def test_monitoring_zone_get(self):
        self.verify_get(self.proxy.get_monitoring_zone,
                        monitoring_zone.MonitoringZone)

    def test_notifications(self):
        self.verify_list(self.proxy.notifications,
                         notification.Notification, paginated=False)

    def test_notification_create(self):
        self.verify_create(self.proxy.create_notification,
                           notification.Notification)

    def test_notification_delete(self):
        self.verify_delete(self.proxy.delete_notification,
                           notification.Notification, False)

    def test_notification_delete_ignore(self):
        self.verify_delete(self.proxy.delete_notification,
                           notification.Notification, True)

    def test_notification_find(self):
        self.verify_find(self.proxy.find_notification,
                         notification.Notification)

    def test_notification_get(self):
        self.verify_get(self.proxy.get_notification,
                        notification.Notification)

    def test_notification_update(self):
        self.verify_update(self.proxy.update_notification,
                           notification.Notification)

    def test_notification_plans(self):
        self.verify_list(self.proxy.notification_plans,
                         notification_plan.NotificationPlan, paginated=False)

    def test_notification_plan_create(self):
        self.verify_create(self.proxy.create_notification_plan,
                           notification_plan.NotificationPlan)

    def test_notification_plan_delete(self):
        self.verify_delete(self.proxy.delete_notification_plan,
                           notification_plan.NotificationPlan, False)

    def test_notification_plan_delete_ignore(self):
        self.verify_delete(self.proxy.delete_notification_plan,
                           notification_plan.NotificationPlan, True)

    def test_notification_plan_find(self):
        self.verify_find(self.proxy.find_notification_plan,
                         notification_plan.NotificationPlan)

    def test_notification_plan_get(self):
        self.verify_get(self.proxy.get_notification_plan,
                        notification_plan.NotificationPlan)

    def test_notification_plan_update(self):
        self.verify_update(self.proxy.update_notification_plan,
                           notification_plan.NotificationPlan)

    def test_notification_types(self):
        self.verify_list(self.proxy.notification_types,
                         notification_type.NotificationType, paginated=False)

    def test_notification_type_find(self):
        self.verify_find(self.proxy.find_notification_type,
                         notification_type.NotificationType)

    def test_notification_type_get(self):
        self.verify_get(self.proxy.get_notification_type,
                        notification_type.NotificationType)

    def test_suppressions(self):
        self.verify_list(self.proxy.suppressions,
                         suppression.Suppression, paginated=False)

    def test_overviews(self):
        self.verify_list(
            self.proxy.overviews, overview.Overview, paginated=False)

    def test_alarm_test(self):
        test_entity_id = "test_entity_id"
        example_check_data = "check_data"
        example_criteria = "criteria"

        self._verify(
            "rackspace.monitoring.v1.entity.Entity.test_alarm",
            self.proxy.test_alarm,
            method_args=[test_entity_id, example_check_data, example_criteria],
            expected_args=["check_data", "criteria"])

    def test_new_check_test(self):
        test_entity_id = "test_entity_id"
        example_attributes = "attributes"

        self._verify(
            "rackspace.monitoring.v1.entity.Entity.test_new_check",
            self.proxy.test_new_check,
            method_args=[test_entity_id, example_attributes],
            expected_args=["attributes"])

    def test_notification_test(self):
        self._verify(
            "rackspace.monitoring.v1.notification.Notification.test",
            self.proxy.test_notification, method_args=["value"])

    def test_traceroute(self):
        test_monitoring_zone = "test_monitoring_zone"
        example_target = "www.rackspace.com"
        example_target_resolver = "IPv6"

        self._verify(
            "rackspace.monitoring.v1"
            ".monitoring_zone.MonitoringZone.traceroute",
            self.proxy.traceroute, method_args=[
                test_monitoring_zone, example_target, example_target_resolver],
            expected_args=["www.rackspace.com", "IPv6"])

    def test_suppression_create(self):
        self.verify_create(self.proxy.create_suppression,
                           suppression.Suppression)

    def test_suppression_delete(self):
        self.verify_delete(self.proxy.delete_suppression,
                           suppression.Suppression, False)

    def test_suppression_delete_ignore(self):
        self.verify_delete(self.proxy.delete_suppression,
                           suppression.Suppression, True)

    def test_suppression_find(self):
        self.verify_find(self.proxy.find_suppression, suppression.Suppression)

    def test_suppression_get(self):
        self.verify_get(self.proxy.get_suppression, suppression.Suppression)

    def test_suppression_update(self):
        self.verify_update(self.proxy.update_suppression,
                           suppression.Suppression)

    def test_suppression_logs(self):
        self.verify_list(self.proxy.suppression_logs,
                         suppression_log.SuppressionLog, paginated=False)

    def test_suppression_log_find(self):
        self.verify_find(self.proxy.find_suppression_log,
                         suppression_log.SuppressionLog)
