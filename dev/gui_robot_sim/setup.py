from setuptools import find_packages, setup

package_name = 'gui_robot_sim'

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
    description='Simple 2D GUI robot simulation using pygame and ROS 2',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'robot_simulator = gui_robot_sim.robot_simulator:main',
        ],
    },
)
