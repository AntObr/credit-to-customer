# Copyright 2016 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""This is a sample Hello World API implemented using Google Cloud
Endpoints."""

# [START imports]
import endpoints
from protorpc import message_types
from protorpc import messages
from protorpc import remote
import manager
# [END imports]

mgr = manager.Manager('data.json')

# [START messages]
class EchoRequest(messages.Message):
    content = messages.StringField(1)


class EchoResponse(messages.Message):
    """A proto Message that contains a simple string field."""
    content = messages.StringField(1)


ECHO_RESOURCE = endpoints.ResourceContainer(
    EchoRequest,
    n=messages.IntegerField(2, default=1)
)

GET_EMAIL_RESOURCE = endpoints.ResourceContainer(
    message_types.VoidMessage,
    trailingDigits = messages.IntegerField(1, default = 1, required=True),
    leadingDigits = messages.IntegerField(2, default = 1, required=True)
)
# [END messages]


# [START echo_api]
@endpoints.api(name='echo', version='v1')
class EchoApi(remote.Service):

    @endpoints.method(
        # This method takes a ResourceContainer defined above.
        ECHO_RESOURCE,
        # This method returns an Echo message.
        EchoResponse,
        path='echo',
        http_method='PUT',
        name='echo')
    def echo(self, request):
        mgr.load()
        print(request.content)
        mgr.add(request.content)
        if (isinstance(request.content, str())):
            out = "string"
        else:
            out = mgr.getDataDumps()
        return EchoResponse(content = out)

    @endpoints.method(
        GET_EMAIL_RESOURCE,
        # message_types.VoidMessage,
        EchoResponse,
        # path='echo/getEmails/{i}',
        path='echo/getEmails',
        http_method='GET',
        name='echo_get_emails'
    )
    def echo_get_emails(self, request):
        query = {
            "startDate": 12.08,
            "trailingDigits": 3456,
            "endDate": 15.08,
            "cardType": "MasterCard",
            "leadingDigits": 5407
        }
        out = mgr.search(query)
        return EchoResponse(content = out)

# [END echo_api]


# [START api_server]
api = endpoints.api_server([EchoApi])
# [END api_server]
