from setuptools import setup

requirements = [
    # TODO: put your package requirements here
]

test_requirements = [
    'pytest',
    'pytest-cov',
    'pytest-faulthandler',
    'pytest-mock',
    'pytest-qt',
    'pytest-xvfb',
]

setup(
    name='ECN_Creator_3',
    version='0.0.1',
    description="A program to take a list of PDF files in a directory structure and create a formatted ECN list.",
    author="Jim West",
    author_email='yuanchueh@gmail.com',
    url='https://github.com/yuanchueh/ECN_Creator_3',
    packages=['ecn_creator_3', 'ecn_creator_3.images',
              'ecn_creator_3.tests'],
    package_data={'ecn_creator_3.images': ['*.png']},
    entry_points={
        'console_scripts': [
            'ECN_Creator_3=ecn_creator_3.create_ecn:main'
        ]
    },
    install_requires=requirements,
    zip_safe=False,
    keywords='ECN_Creator_3',
    classifiers=[
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
