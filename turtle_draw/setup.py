from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'turtle_draw'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(),
    data_files=[
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ragesh',
    maintainer_email='ragesh.ramachandran@node-robotics.com',
    description='Package to draw ROBOTAIR using TurtleSim',
    license='Apache-2.0',
    tests_require=['pytest'],
    test_suite='test',
    entry_points={
        'console_scripts': [
            'draw_robotair = turtle_draw.main:main',
        ],
    },
)
