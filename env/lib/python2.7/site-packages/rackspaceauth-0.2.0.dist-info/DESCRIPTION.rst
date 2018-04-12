keystoneauth plugin for Rackspace authentication
================================================

.. image:: https://travis-ci.org/rackerlabs/python-rackspace-auth.svg
    :target: https://travis-ci.org/rackerlabs/python-rackspace-auth

This package provides plugins to
`keystoneauth1 <https://pypi.python.org/pypi/keystoneauth1/>`_,
the OpenStack Keystone authentication library, for Rackspace's supported
authentication methods: API key, password, and token.

Usage
-----

The following example authenticates Mayor McCheese with his API key,
as found in his `control panel <https://mycloud.rackspace.com/>`_. ::

    from rackspaceauth import v2
    from keystoneauth1 import session

    auth = v2.APIKey(username="Mayor McCheese",
                     key="OMGCHEESEISGREAT")

    sess = session.Session(auth=auth)
    sess.get_token()



