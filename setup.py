from setuptools import setup, find_packages

setup(
    name='perfutils',
    version='1.0',
    description='Utilities for TSNE perf comparisions',
    author='Dan Rapp',
    author_email='rappdw@gmail.com',
    license='MIT',
    keywords='library',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Python :: Library',
        'License :: MIT',
        'Programming Language :: Python :: 3.6',
    ],
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    include_package_data=True,
    install_requires=[
        "matplotlib"
    ],

    extras_require={
    },

    package_data={
    },

    entry_points={
    },
    scripts=[
    ]

)
