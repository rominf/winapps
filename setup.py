# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['winapps']

package_data = \
{'': ['*']}

install_requires = \
['plumbum>=1.6,<2.0']

extras_require = \
{':python_version >= "3.6" and python_version < "3.7"': ['dataclasses>=0.6.0,<0.7.0']}

setup_kwargs = {
    'name': 'winapps',
    'version': '0.1.1',
    'description': 'Python library for managing installed applications on Windows',
    'long_description': '# winapps - Python library for managing installed applications on Windows\n[![License](https://img.shields.io/pypi/l/winapps.svg)](https://www.apache.org/licenses/LICENSE-2.0)\n![PyPI - Python Version](https://img.shields.io/pypi/pyversions/winapps.svg)\n[![PyPI](https://img.shields.io/pypi/v/winapps.svg)](https://pypi.org/project/winapps/)\n\n## Installation\nTo install `winapps` from PyPI run:\n```shell\n$ pip install winapps\n```\n\n## Usage\n### Printing installed applications\n```python\nimport winapps\n\nfor app in winapps.list_installed():\n    print(app)\n# InstalledApplication(name=\'7-Zip 19.00 (x64)\', version=\'19.00\', install_date=None, install_location=WindowsPath(\'C:/Program Files/7-Zip\'), install_source=None, modify_path=None, publisher=\'Igor Pavlov\', uninstall_string=\'C:\\\\Program Files\\\\7-Zip\\\\Uninstall.exe\')\n# InstalledApplication(name=\'Mozilla Firefox 66.0.2 (x64 ru)\', version=\'66.0.2\', install_date=None, install_location=WindowsPath(\'C:/Program Files/Mozilla Firefox\'), install_source=None, modify_path=None, publisher=\'Mozilla\', uninstall_string=\'"C:\\\\Program Files\\\\Mozilla Firefox\\\\uninstall\\\\helper.exe"\')\n# InstalledApplication(name=\'Mozilla Maintenance Service\', version=\'66.0.2\', install_date=None, install_location=None, install_source=None, modify_path=None, publisher=\'Mozilla\', uninstall_string=\'"C:\\\\Program Files (x86)\\\\Mozilla Maintenance Service\\\\uninstall.exe"\')\n# InstalledApplication(name=\'Oracle VM VirtualBox Guest Additions 6.0.4\', version=\'6.0.4.0\', install_date=None, install_location=None, install_source=None, modify_path=None, publisher=\'Oracle Corporation\', uninstall_string=\'C:\\\\Program Files\\\\Oracle\\\\VirtualBox Guest Additions\\\\uninst.exe\')\n# InstalledApplication(name=\'Python 3.7.1 (Miniconda3 4.5.12 64-bit)\', version=\'4.5.12\', install_date=None, install_location=None, install_source=None, modify_path=None, publisher=\'Anaconda, Inc.\', uninstall_string=\'"C:\\\\ProgramData\\\\Miniconda3\\\\Uninstall-Miniconda3.exe"\')\n# InstalledApplication(name=\'TortoiseHg 4.9.0 (x64)\', version=\'4.9.0\', install_date=datetime.date(2019, 4, 3), install_location=WindowsPath(\'C:/Program Files/TortoiseHg\'), install_source=WindowsPath(\'C:/Users/Roman Inflianskas/Downloads\'), modify_path=\'MsiExec.exe /I{9DF3A4E8-0C61-49CC-9170-79B0DE20EF25}\', publisher=\'Steve Borho and others\', uninstall_string=\'MsiExec.exe /I{9DF3A4E8-0C61-49CC-9170-79B0DE20EF25}\')\n# ...\n```\n\n### Searching and uninstalling application\n```python\nimport winapps\n\nfor app in winapps.search_installed(\'tortoisehg\'):\n    app.uninstall()\n```\n\n### Installing and uninstalling using .exe installer\n```python\nimport winapps\n\ninstaller_path = r\'D:\\wix311.exe\'\n\nwinapps.install(installer_path, quiet=True)\nwinapps.uninstall(installer_path, quiet=True)\ninstaller_command = winapps.installer_command(installer_path, log_path=r\'D:\\installer.log\')\ninstaller_command()\nwinapps.uninstall(installer_command, quiet=False)\n```\n\n## Caveats\nThe library currently lookups only for software installed for all users. Only Windows Installer 3.0 .exe installers are\nsupported in `installer_command`, `install`, and `uninstall` are supported.\n\n## Credits\nThis library is heavily inspired by `win_pkg` SaltStack module.',
    'author': 'Roman Inflianskas',
    'author_email': 'infroma@gmail.com',
    'url': 'https://github.com/rominf/winapps',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
