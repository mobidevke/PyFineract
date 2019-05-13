import textwrap

import setuptools

version = "0.0.39"

if __name__ == '__main__':
    setuptools.setup(
        name='PyFineract',
        version=version,
        author='Mobidev Kenya',
        author_email='projects@devs.mobi',
        description='A fineract API wrapper',
        long_description=textwrap.dedent("""
            Tutorial (Short)
            ----------------
            
            First create a Fineract instance::
            
                from fineract import Fineract
            
                # First create a Fineract instance
            
                # using username, password, tenant and base url
                f = Fineract("mifos", "password", "default, "https://localhost/fineract-provider/api/v1")
            
            Then work with your Fineract objects::
            
                for client in f.get_clients():
                    print(client.full_name)
    
        """),
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
