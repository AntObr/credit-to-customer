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

import mock
import unittest2

from rackspace import connection


class TestConnection(unittest2.TestCase):

    def test_no_region(self):
        with self.assertRaises(ValueError):
            connection.Connection()

    @mock.patch("rackspace.connection.Connection._open")
    def test_with_region(self, mock_open=lambda: None):
        prof = mock.Mock()
        region = "BEN"

        connection.Connection(region=region, profile=prof,
                              username="test", api_key="test")

        prof.set_region.assert_called_with(prof.ALL, region)
