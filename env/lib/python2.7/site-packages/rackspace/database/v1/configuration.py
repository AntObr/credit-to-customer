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
from rackspace.database import database_service


class Configuration(resource.Resource):
    base_path = '/configurations'
    resource_key = "configuration"
    resources_key = "configurations"
    service = database_service.DatabaseService()

    # capabilities
    allow_create = True
    allow_delete = True
    allow_list = True
    allow_retrieve = True
    allow_update = True
    patch_update = True

    # Properties
    #: The name of this configuration
    name = resource.prop("name")
    #: The id of this configuration
    id = resource.prop("id")
    #: Dictionary of datastore details, with  `type` and `version` keys
    datastore = resource.prop("datastore", type=dict)
    #: The values for the configuration.
    values = resource.prop("values", type=dict)
    #: The name of the datastore
    datastore_name = resource.prop("datastore_name")
    #: The version name of the datastore
    datastore_version_name = resource.prop("datastore_version_name")
    #: The version id of the datastore
    datastore_version_id = resource.prop("datastore_version_id")
    #: The last time this configuration was updated
    updated_at = resource.prop("updated")
    #: The time when this configuration was created
    created_at = resource.prop("created")
    #: A description of this datastore
    description = resource.prop("description")

    def update(self, session, prepend_key=True, has_body=False):
        # Only try to update if we actually have anything to update.
        if not any([self._body.dirty, self._header.dirty]):
            return self

        request = self._prepare_request(prepend_key=prepend_key)

        response = session.patch(request.uri, endpoint_filter=self.service,
                                 json=request.body, headers=request.headers)

        self._translate_response(response, has_body=has_body)
        return self

    def instances(self):
        yield
