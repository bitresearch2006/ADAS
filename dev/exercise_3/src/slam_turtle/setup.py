from setuptools import find_packages, setup

package_name = 'slam_turtle'

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
    maintainer='nand_mahasreeki_23',
    maintainer_email='nand_mahasreeki_23@todo.todo',
    description='A basic SLAM-like simulation using Turtlesim in ROS 2',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'slam_like_node = slam_turtle.slam_like_node:main',
            'random_mover = slam_turtle.random_movement:main', 
            'free_mover = slam_turtle.free_movement:main',
        ],
    },
)
