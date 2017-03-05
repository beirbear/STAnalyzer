from setuptools import setup

setup(name='harmonicIO',
      version='0.1.0',
      install_requires=['urllib3'],
      packages=['basic'],
      entry_points={
          'console_scripts': [
              'basic = basic.__main__:main'
          ]
      }
      )