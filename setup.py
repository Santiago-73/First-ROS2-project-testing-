from setuptools import find_packages, setup

package_name = 'mi_primer_paquete'

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
    maintainer='user',
    maintainer_email='user@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            # comando_en_terminal = paquete.archivo_python:funcion_main
            'saludar = mi_primer_paquete.simple_node:main',
            'mover = mi_primer_paquete.mover_tortuga:main',
            'inteligente = mi_primer_paquete.tortuga_inteligente:main',
            'invocar = mi_primer_paquete.cliente_tortuga:main',
        ],
    },
)
