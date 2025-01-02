from setuptools import setup

setup(
    name='teleop_twist_keyboard',
    version='0.0.0',
    packages=[],
    py_modules=['teleop_twist_keyboard'],
    install_requires=['setuptools'],
    maintainer='Rohan Agrawal',
    maintainer_email='rohan@osrfoundation.org',
    keywords=['ROS'],
    data_files=[
    ('share/ament_index/resource_index/packages',
     ['resource/teleop_twist_keyboard']),
    ('share/teleop_twist_keyboard', ['package.xml']),
],

    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description=(
        'Teleop from the keyboard.'
    ),
    entry_points={
        'console_scripts': [
            'teleop_twist_keyboard = teleop_twist_keyboard:main'
        ],
    },
)
