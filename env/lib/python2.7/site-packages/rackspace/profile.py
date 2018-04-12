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

from openstack import profile


class Profile(profile.Profile):

    def __init__(self, region, plugins=None, **kwargs):
        super(Profile, self).__init__(plugins=plugins or ['rackspace'])

        self.set_region(self.ALL, region)

        global_services = ('cloudMetrics', 'cloudMetricsIngest',
                           'cloudMonitoring', 'rackCDN')

        for service in self.get_services():
            if service.service_name in global_services:
                service.region = None
