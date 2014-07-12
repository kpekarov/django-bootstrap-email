Django Bootstrap Email
================================================

[![PyPi version](https://pypip.in/v/django-bootstrap-email/badge.png)](https://crate.io/packages/django-bootstrap-email/)

[![PyPi downloads](https://pypip.in/d/django-bootstrap-email/badge.png)](https://crate.io/packages/django-bootstrap-email/)

Using Twitter Bootstrap v2.3.2 for emails

Based on
--------
* BootstrapForEmail https://github.com/advancedrei/BootstrapForEmail

Installation
------------
1. Install using pip:

        pip install django-bootstrap-email

2. Add to INSTALLED_APPS:

        'bootstrap_email',

Use in templates
----------------

    {% load bootstrap_email %}

    <!DOCTYPE html>
    <html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <title>{{ subject }}</title>
        <style media="all" type="text/css">
            {% bootstrap_email %}
        </style>
    </head>

Bugs and requests
-----------------

If you have found a bug or a request for additional functionality, please use the issue tracker on GitHub.

https://github.com/dyve/django-bootstrap-email/issues

About
-----

django-bootstrap-email is packaged by Kirill Pekarov https://github.com/kpekarov


TODO
----

Empty


History
-------

Empty


Copyright and license
---------------------

Copyright 2014 Kirill Pekarov, AdvancedREI, LLC, and Twitter, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this work except in compliance with the License.
You may obtain a copy of the License in the LICENSE file, or at:

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.