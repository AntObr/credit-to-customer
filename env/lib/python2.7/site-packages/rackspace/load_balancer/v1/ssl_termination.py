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
from openstack import resource2

from rackspace.load_balancer import load_balancer_service


class SSLTermination(resource2.Resource):
    resource_key = "sslTermination"
    base_path = "/loadbalancers/%(load_balancer_id)s/ssltermination"
    service = load_balancer_service.LoadBalancerService()

    allow_get = True
    allow_update = True
    allow_delete = True

    load_balancer_id = resource2.URI("load_balancer_id")

    #: The private key for the SSL certificate. The private key is
    #: validated and verified against the provided certificates.
    private_key = resource2.Body("privateKey")
    #: The certificate used for SSL termination. The certificate is
    #: validated and verified against the key and intermediate certificate
    #: if provided.
    certificate = resource2.Body("certificate")
    #: The intermediate certificate for the user that is used for SSL
    #: termination. The intermediate certificate is validated and verified
    #: against the key and certificate credentials provided. A user may
    #: only provide an intermediateCertificate when accompanied by a
    #: certificate, private key, and securePort. It may not be added
    #: to an existing SSL configuration as a single attribute in a
    #: future request.
    intermediate_certificate = resource2.Body("intermediateCertificate")
    #: Determines if the load balancer is enabled to terminate SSL traffic.
    #: If is_enabled = False, the load balancer retains its specified
    #: SSL attributes but does not terminate SSL traffic.
    is_enabled = resource2.Body("enabled", type=format.BoolStr)
    #: Determines if the load balancer can accept only secure traffic.
    #: If only_secure_traffic = True, the load balancer does not accept
    #: non-secure traffic.
    only_secure_traffic = resource2.Body("secureTrafficOnly",
                                         type=format.BoolStr)
    #: The port on which the SSL termination load balancer listens for
    #: secure traffic. The secure port must be unique to the existing
    #: LB protocol/port combination. For example, port 443.
    secure_port = resource2.Body("securePort", type=int)
    #: Specifies the security protocol name and the security protocol status.
    #: This is a list of dictionaries, where each dictionary has the keys
    #: `securityProtocolName` and `securityProtocolStatus`.
    #: Currently, the only `securityProtocolName` accepted is "TLS_10".
    #: `securityProtocolStatus` can be DISABLED or ENABLED (the default).
    security_protocols = resource2.Body("securityProtocols", type=list)

    def _prepare_request(self, requires_id=True, prepend_key=False):
        # SSLTermination has no sort of ID as there can only be one
        # configuration per load balancer. We need to force the base
        # class to ignore any `requires_id` that comes through while
        # attempting to GET a single one.
        return super(SSLTermination, self)._prepare_request(
            requires_id=False, prepend_key=prepend_key)
