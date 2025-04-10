from setuptools import find_packages, setup

package_name = 'my_turtle_square'

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
    description='A turtle simulation that makes the turtle move in a square',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'turtle_square=my_turtle_square.turtle_square:main',
            'turtle_large_square=my_turtle_square.turtle_large_square:main',
        ],
    },
)
