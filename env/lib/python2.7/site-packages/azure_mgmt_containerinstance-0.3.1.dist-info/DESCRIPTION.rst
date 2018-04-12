Microsoft Azure SDK for Python
==============================

This is the Microsoft Azure Container Instance Client Library.

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

For code examples, see `Container Instance
<https://docs.microsoft.com/python/api/overview/azure/containerinstance>`__
on docs.microsoft.com.


Provide Feedback
================

If you encounter any bugs or have suggestions, please file an issue in the
`Issues <https://github.com/Azure/azure-sdk-for-python/issues>`__
section of the project.


.. :changelog:

Release History
===============

0.3.1 (2018-02-05)
++++++++++++++++++

* Fix dnsnamelabel to dns_name_label

0.3.0 (2018-02-01)
++++++++++++++++++

* Add dnsnamelabel
* Add fqdn
* Add container_group_usage operation groups
* Add git_repo and secret to volumes
* Add container_groups.update

API version is now 2018-02-01-preview

0.2.0 (2017-10-20)
++++++++++++++++++

* Added on-failure/never container group retry policy
* Added container volumes mount support
* Added operations API
* Added container group instance view
* Renamed event class

0.1.0 (2017-07-27)
++++++++++++++++++

* Initial preview release


