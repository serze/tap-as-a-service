# Copyright (c) 2015 Midokura SARL
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from tempest import config
from tempest import test

from neutron_taas.tests.tempest_plugin.tests.api import base

CONF = config.CONF


class TaaSExtensionTestJSON(base.BaseTaaSTest):

    @classmethod
    def resource_setup(cls):
        super(TaaSExtensionTestJSON, cls).resource_setup()
        if not test.is_extension_enabled('taas', 'network'):
            msg = "TaaS Extension not enabled."
            raise cls.skipException(msg)

    @test.idempotent_id('b993c14e-797a-4c91-b4da-8cb1a450aa2f')
    def test_dummy(self):
        pass