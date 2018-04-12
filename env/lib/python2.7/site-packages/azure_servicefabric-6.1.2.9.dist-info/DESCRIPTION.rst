Microsoft Azure SDK for Python
==============================

This is the Microsoft Azure Service Fabric Client Library.

Azure Resource Manager (ARM) is the next generation of management APIs that
replace the old Azure Service Management (ASM).

This package has been tested with Python 2.7, 3.4, 3.5 and 3.6.

For the older Azure Service Management (ASM) libraries, see
`azure-servicemanagement-legacy <https://pypi.python.org/pypi/azure-servicemanagement-legacy>`__ library.

For a more complete set of Azure libraries, see the `azure <https://pypi.python.org/pypi/azure>`__ bundle package.


Compatibility
=============

**IMPORTANT**: If you have an earlier version of the azure package
(version < 1.0), you should uninstall it before installing this package.

You can check the version using pip:

.. code:: shell

    pip freeze

If you see azure==0.11.0 (or any version below 1.0), uninstall it first:

.. code:: shell

    pip uninstall azure


Usage
=====

For code examples, see `Service Fabric
<https://docs.microsoft.com/python/api/overview/azure/servicefabric/clientlibrary>`__
on docs.microsoft.com.


Provide Feedback
================

If you encounter any bugs or have suggestions, please file an issue in the
`Issues <https://github.com/Azure/azure-sdk-for-python/issues>`__
section of the project.


.. :changelog:

Release History
===============

6.1.2.9 (2018-02-05)
++++++++++++++++++++

**Bugfixes**

- Numerous fixes to descriptions and help text of entities

**Features**

- Chaos service now supports a target filter
- Application types can now be provisioned and created in external stores
- Added Orchestration Service internal support APIs
- Added container deployment management APIs

6.1.1.9 (2018-01-23)
++++++++++++++++++++

This version was broken and has been removed from PyPI.

6.0.2 (2017-10-26)
++++++++++++++++++

**Bugfixes**

- remove application_type_version in get_application_type_info_list_by_name
- fix application_type_definition_kind_filter default value from 65535 to 0

**Features**

- add create_name, get_name_exists_info, delete_name, get_sub_name_info_list,
  get_property_info_list, put_property, get_property_info, delete_property,
  submit_property_batch

6.0.1 (2017-09-28)
++++++++++++++++++

**Bug fix**

- Fix some unexpected exceptions

6.0 (2017-09-22)
++++++++++++++++

* Stable 6.0 api

6.0.0rc1 (2017-09-16)
+++++++++++++++++++++

* Release candidate for Service Fabric 6.0 runtime

5.6.130 (2017-05-04)
++++++++++++++++++++

* Initial Release


