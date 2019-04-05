# winapps - Python library for managing installed applications on Windows
[![License](https://img.shields.io/pypi/l/winapps.svg)](https://www.apache.org/licenses/LICENSE-2.0)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/winapps.svg)
[![PyPI](https://img.shields.io/pypi/v/winapps.svg)](https://pypi.org/project/winapps/)

## Installation
To install `winapps` from PyPI run:
```shell
$ pip install winapps
```

## Usage
### Printing installed applications
```python
import winapps

for app in winapps.list_installed():
    print(app)
# InstalledApplication(name='7-Zip 19.00 (x64)', version='19.00', install_date=None, install_location=WindowsPath('C:/Program Files/7-Zip'), install_source=None, modify_path=None, publisher='Igor Pavlov', uninstall_string='C:\\Program Files\\7-Zip\\Uninstall.exe')
# InstalledApplication(name='Mozilla Firefox 66.0.2 (x64 ru)', version='66.0.2', install_date=None, install_location=WindowsPath('C:/Program Files/Mozilla Firefox'), install_source=None, modify_path=None, publisher='Mozilla', uninstall_string='"C:\\Program Files\\Mozilla Firefox\\uninstall\\helper.exe"')
# InstalledApplication(name='Mozilla Maintenance Service', version='66.0.2', install_date=None, install_location=None, install_source=None, modify_path=None, publisher='Mozilla', uninstall_string='"C:\\Program Files (x86)\\Mozilla Maintenance Service\\uninstall.exe"')
# InstalledApplication(name='Oracle VM VirtualBox Guest Additions 6.0.4', version='6.0.4.0', install_date=None, install_location=None, install_source=None, modify_path=None, publisher='Oracle Corporation', uninstall_string='C:\\Program Files\\Oracle\\VirtualBox Guest Additions\\uninst.exe')
# InstalledApplication(name='Python 3.7.1 (Miniconda3 4.5.12 64-bit)', version='4.5.12', install_date=None, install_location=None, install_source=None, modify_path=None, publisher='Anaconda, Inc.', uninstall_string='"C:\\ProgramData\\Miniconda3\\Uninstall-Miniconda3.exe"')
# InstalledApplication(name='TortoiseHg 4.9.0 (x64)', version='4.9.0', install_date=datetime.date(2019, 4, 3), install_location=WindowsPath('C:/Program Files/TortoiseHg'), install_source=WindowsPath('C:/Users/Roman Inflianskas/Downloads'), modify_path='MsiExec.exe /I{9DF3A4E8-0C61-49CC-9170-79B0DE20EF25}', publisher='Steve Borho and others', uninstall_string='MsiExec.exe /I{9DF3A4E8-0C61-49CC-9170-79B0DE20EF25}')
# ...
```

### Searching and uninstalling application
```python
import winapps

for app in winapps.search_installed('tortoisehg'):
    app.uninstall()
```

### Installing and uninstalling using .exe installer
```python
import winapps

installer_path = r'D:\wix311.exe'

winapps.install(installer_path, quiet=True)
winapps.uninstall(installer_path, quiet=True)
installer_command = winapps.installer_command(installer_path, log_path=r'D:\installer.log')
installer_command()
winapps.uninstall(installer_command, quiet=False)
```

## Caveats
The library currently lookups only for software installed for all users. Only Windows Installer 3.0 .exe installers are
supported in `installer_command`, `install`, and `uninstall` are supported.

## Credits
This library is heavily inspired by `win_pkg` SaltStack module.