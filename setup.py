from setuptools import setup, find_packages

# https://pypi.org/pypi?%3Aaction=list_classifiers

setup(
    name='relpath',
    packages=find_packages(),
    version='1.0.0',
    description='Get relative path.',
    long_description='Get relative-path even when it is not in subdirectory tree.',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries',
        'Typing :: Typed'
    ],
    author='Josef Fuchs <josef.fuchs@j-fuchs.at>',
    license='MIT',
    setup_requires=['pathlib'],
    test_suite='pytest',
    tests_require=['pytest'],
)
