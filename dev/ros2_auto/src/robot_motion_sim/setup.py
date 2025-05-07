from setuptools import find_packages, setup

package_name = 'robot_motion_sim'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='mahasreeki_23',
    maintainer_email='mahasreeki_23@todo.todo',
    description='Simulation of a 4-wheeled robot using LIDAR and IMU',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'motion_node = robot_motion_sim.motion_node:main',
            'sensor_simulator = robot_motion_sim.sensor_simulator:main',
        ],
    },
)
