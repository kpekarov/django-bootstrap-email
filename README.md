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

    <html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <title>[REPLACE THIS WITH YOUR TITLE]</title>
            <style media="all" type="text/css">
            {% bootstrap_email %}
            {# or use bootstrap_email_min for stripped file #}
        </style>
    </head>
    <body>
        <table cellspacing="0" cellpadding="0" border="0" width="100%">
            <tr>
                <td class="navbar navbar-inverse" align="center">
                    <!-- This setup makes the nav background stretch the whole width of the screen. -->
                    <table width="650px" cellspacing="0" cellpadding="3" class="container">
                        <tr class="navbar navbar-inverse">
                            <td colspan="4"><a class="brand" href="[YOUR WEB URL]">Bootstrap For Email</a></td>
                            <td><ul class="nav pull-right"><li><a href="[YOUR LOGIN URL]">Log On</a></li></ul></td>
                        </tr>
                    </table>
                </td>
            </tr>
            <tr>
                <td bgcolor="#FFFFFF" align="center">
                    <table width="650px" cellspacing="0" cellpadding="3" class="container">
                        <tr>
                            <td>[BODY CONTENT GOES HERE]</td>
                        </tr>
                    </table>
                </td>
            </tr>
            <tr>
                <td bgcolor="#FFFFFF" align="center">
                    <table width="650px" cellspacing="0" cellpadding="3" class="container">
                        <tr>
                            <td>
                                <hr>
                                <p>[PUT YOUR COPYRIGHT OR OTHER FOOTERY GOODNESS HERE]</p>
                            </td>
                        </tr>
                    </table>
                </td>
            </tr>
        </table>
    </body>
    </html>

Bugs and requests
-----------------

If you have found a bug or a request for additional functionality, please use the issue tracker on GitHub.

https://github.com/kpekarov/django-bootstrap-email/issues

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