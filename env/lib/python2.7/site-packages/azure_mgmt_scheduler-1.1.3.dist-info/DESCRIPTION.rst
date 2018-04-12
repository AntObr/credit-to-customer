Microsoft Azure SDK for Python
==============================

This is the Microsoft Azure Scheduler Management Client Library.

Azure Resource Manager (ARM) is the next generation of management APIs that
replace the old Azure Service Management (ASM).

This package has been tested with Python 2.7, 3.3, 3.4, 3.5 and 3.6.

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

For code examples, see `Scheduler Resource Management 
<https://azure-sdk-for-python.readthedocs.org/en/latest/resourcemanagementscheduler.html>`__
on readthedocs.org.


Provide Feedback
================

If you encounter any bugs or have suggestions, please file an issue in the
`Issues <https://github.com/Azure/azure-sdk-for-python/issues>`__
section of the project.


.. :changelog:

Release History
===============

1.1.3 (2017-09-07)
++++++++++++++++++

**Bug fixes**

- jobs.get function fails if custom retry policy is set (#1358)

1.1.2 (2017-04-18)
++++++++++++++++++

This wheel package is now built with the azure wheel extension

1.1.1 (2017-01-13)
++++++++++++++++++

* Fix `time_to_live` attribute type for correct parsing

1.1.0 (2016-11-14)
++++++++++++++++++

**breaking changes**

* Simplify `jobs.create_or_update` parameters
* Simplify `jobs.patch` parameters

1.0.0 (2016-08-30)
++++++++++++++++++

* Initial Release (API Version 2016-03-01)


