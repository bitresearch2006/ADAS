from setuptools import find_packages, setup

package_name = 'gui_robot_straight'

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
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'straight_simulator = gui_robot_straight.straight_simulator:main',
        ],
    },
)
