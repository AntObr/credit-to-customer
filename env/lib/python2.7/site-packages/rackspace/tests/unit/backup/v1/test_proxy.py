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
from rackspace.backup.v1 import _proxy
from rackspace.backup.v1 import activity
from rackspace.backup.v1 import agent
from rackspace.backup.v1 import backup_configuration
from rackspace.backup.v1 import restore_configuration


class TestBackupProxy(test_proxy_base.TestProxyBase):
    def setUp(self):
        super(TestBackupProxy, self).setUp()
        self.proxy = _proxy.Proxy(self.session)

    def test_activities(self):
        self.verify_list(self.proxy.activities, activity.Activity,
                         paginated=False)

    def test_agents(self):
        self.verify_list(self.proxy.agents, agent.Agent,
                         paginated=False)

    def test_agent_delete(self):
        self.verify_delete(self.proxy.delete_agent, agent.Agent, False)

    def test_agent_delete_ignore(self):
        self.verify_delete(self.proxy.delete_agent, agent.Agent, True)

    def test_backup_configurations(self):
        self.verify_list(self.proxy.backup_configurations,
                         backup_configuration.BackupConfiguration,
                         paginated=False)

    def test_backup_configuration_create(self):
        self.verify_create(self.proxy.create_backup_configuration,
                           backup_configuration.BackupConfiguration)

    def test_backup_configuration_delete(self):
        self.verify_delete(self.proxy.delete_backup_configuration,
                           backup_configuration.BackupConfiguration, False)

    def test_backup_configuration_delete_ignore(self):
        self.verify_delete(self.proxy.delete_backup_configuration,
                           backup_configuration.BackupConfiguration, True)

    def test_backup_configuration_find(self):
        self.verify_find(self.proxy.find_backup_configuration,
                         backup_configuration.BackupConfiguration)

    def test_backup_configuration_get(self):
        self.verify_get(self.proxy.get_backup_configuration,
                        backup_configuration.BackupConfiguration)

    def test_backup_configuration_update(self):
        self.verify_update(self.proxy.update_backup_configuration,
                           backup_configuration.BackupConfiguration)

    def test_restore_configuration_create(self):
        self.verify_create(self.proxy.create_restore_configuration,
                           restore_configuration.RestoreConfiguration)

    def test_restore_configuration_update(self):
        self.verify_update(self.proxy.update_restore_configuration,
                           restore_configuration.RestoreConfiguration)
