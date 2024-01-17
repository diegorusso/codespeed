from setuptools import setup, find_packages

setup(
    name='codespeed',
    version='0.13.0',
    author='Miquel Torres',
    author_email='tobami@gmail.com',
    url='https://github.com/tobami/codespeed',
    download_url="https://github.com/tobami/codespeed/tags",
    license='GNU Lesser General Public License version 2.1',
    keywords=['benchmarking', 'visualization'],
    install_requires=['django', 'isodate', 'matplotlib'],
    packages=find_packages(exclude=['ez_setup', 'sample_project']),
    long_description='README.md',
    long_description_content_type="text/markdown",
    description='A web application to monitor and analyze the performance of your code',
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v2 (LGPLv2)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
    ]
)

