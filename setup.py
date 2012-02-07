from distutils.core import setup
from setuptools import find_packages

f = open('README')
readme = f.read()
f.close()

setup(
    name='afinn',
    version='0.1',
    description='AFINN but in Django, you see?',
    long_description=readme,
    author='Steve Yeago',
    author_email='subsume@gmail.com',
    url='http://github.com/subsume/AFINN-Django/tree/master',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    package_data = {
    },
    zip_safe=False
)
