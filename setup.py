from setuptools import setup

# Setup
setup(
    name='django-bootstrap-email',
    version='0.0.1',
    url='https://github.com/kpekarov/django-bootstrap-email',
    author='Kirill Pekarov',
    author_email='kpekarov@gmail.com',
    license='Apache License 2.0',
    packages=['bootstrap_email', 'bootstrap_email.templatetags'],
    include_package_data=True,
    description='Bootstrap e-mail support for Django projects',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
        "Environment :: Web Environment",
        "Framework :: Django",
    ],
)
