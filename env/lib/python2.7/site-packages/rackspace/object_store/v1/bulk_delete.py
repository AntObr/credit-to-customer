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

from openstack.object_store import object_store_service
from openstack import resource


class BulkDelete(resource.Resource):
    base_path = "/?bulk-delete"
    service = object_store_service.ObjectStoreService()

    allow_delete = True

    #: The number of items that weren't found
    not_found = resource.prop("Number Not Found")
    #: The response code returned by the bulk delete operation
    response_code = resource.prop("Response Status")
    #: A list of errors that occurred
    errors = resource.prop("Errors")
    #: The number of objects deleted
    deleted = resource.prop("Number Deleted")
    #: Any additional response body
    response_body = resource.prop("Response Body")

    @classmethod
    def delete(cls, session, body):
        """Issue a delete call on the session

        :param str body: The body of the bulk delete request.
            The API works on a text/plain list of lines in the
            format /container_name (to delete empty containers)
            or /container_name/object_name (to delete objects
            in a container)

        :rtype:`~rackspace.object_store.v1.bulk_delete.BulkDelete`
        """
        resp = session.delete(cls.base_path, service=cls.service,
                              data=body).body
        return cls.existing(**resp)
