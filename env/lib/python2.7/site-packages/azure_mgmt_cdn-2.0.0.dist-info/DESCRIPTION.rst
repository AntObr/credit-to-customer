Microsoft Azure SDK for Python
==============================

This is the Microsoft Azure CDN Management Client Library.

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

For code examples, see `CDN Resource Management 
<https://azure-sdk-for-python.readthedocs.org/en/latest/resourcemanagementcdn.html>`__
on readthedocs.org.


Provide Feedback
================

If you encounter any bugs or have suggestions, please file an issue in the
`Issues <https://github.com/Azure/azure-sdk-for-python/issues>`__
section of the project.


.. :changelog:

Release History
===============

2.0.0 (2017-10-26)
++++++++++++++++++

**Features**

- Add probe operations and in some models
- Add list_supported_optimization_types

**Breaking changes**

- move resource_usage into its own operation group
- move operations list into its own operation group

Api version changed from 2016-10-02 to 2017-04-02

1.0.0 (2017-06-30)
++++++++++++++++++

**Features**

- Add disable_custom_https and enable_custom_https

**Breaking changes**

- Rename check_resource_usage to list_resource_usage
- list EdgeNode now returns an iterator of EdgeNode, 
  not a EdgenodeResult instance with an attribute "value" being a list of EdgeNode

0.30.3 (2017-05-15)
+++++++++++++++++++

* This wheel package is now built with the azure wheel extension

0.30.2 (2016-12-22)
+++++++++++++++++++

* Fix EdgeNode attributes content

0.30.1 (2016-12-15)
+++++++++++++++++++

* Fix list EdgeNodes method return type

0.30.0 (2016-12-14)
+++++++++++++++++++

* Initial preview release (API Version 2016-10-02)
* Major breaking changes from 0.30.0rc6

0.30.0rc6 (2016-09-02)
++++++++++++++++++++++

* Initial alpha release (API Version 2016-04-02)


