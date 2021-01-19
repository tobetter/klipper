from setuptools import setup, find_packages

setup(
        name = 'klippy',
        version = '0.1',
        description = 'Klipper server',
        author = 'Dongjin Kim',
        author_email = 'tobetter@gmail.com',
        license = 'MIT',
        packages = find_packages(),
        install_requires = [
            'greenlet == 0.4.15',
            'cffi == 1.12.2',
            'pyserial == 3.4',
            'jinja2 >= 2.10.1',
            ],
        include_package_data = True,
        zip_safe = False)
