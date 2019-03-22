import setuptools

version = "0.0.19"

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='PyFineract',
    version=version,
    author='Mobidev Kenya',
    author_email='projects@devs.mobi',
    description='A fineract API wrapper',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/mobidevke/PyFineract',
    packages=[
        'fineract', 'fineract.objects'
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent'
    ],
    install_requires=[
        'requests>=2.21.0',
        'six==1.12.0'
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'pytest-cov', 'pytest-mock']
)
