from setuptools import setup

package_name = 'rob_controler'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='balu',
    maintainer_email='balu@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'first_node=rob_controler.first_node:main',
            'draw_circle=rob_controler.draw_circle:main',
            'pose_subs=rob_controler.pose_subs:main',
            'key_control=rob_controler.key_control:main'
        ],
    },
)
