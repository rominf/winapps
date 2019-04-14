import re
from pathlib import Path
from tempfile import TemporaryDirectory
from time import sleep
from typing import Optional, Callable
from urllib.request import urlretrieve

import pytest
from plumbum.machines import local

import winapps
from winapps import InstalledApplication


NPP_NAME = 'Notepad++ (32-bit x86)'
NPP_VERSION = '7.6.6'
NPP_PUBLISHER = 'Notepad++ Team'


@pytest.fixture
def installers_temporary_directory() -> TemporaryDirectory:
    return TemporaryDirectory('_winapps-tests')


@pytest.fixture
def npp_installer_path(installers_temporary_directory) -> Path:
    url = 'http://notepad-plus-plus.org/repository/7.x/7.6.6/npp.7.6.6.Installer.exe'
    result = Path(installers_temporary_directory.name) / url.rpartition('/')[2]
    if not result.exists():
        urlretrieve(url=url, filename=str(result))
        assert result.exists()
    return result


def search_installed_npp() -> Optional[InstalledApplication]:
    try:
        return next(winapps.search_installed(re.escape(NPP_NAME)))
    except StopIteration:
        return None


@pytest.fixture
def npp_installed_app(npp_installer_path) -> InstalledApplication:
    quiet_arg = '/S'
    local[str(npp_installer_path)](quiet_arg)
    result = search_installed_npp()
    assert result is not None
    yield result
    result.uninstall(quiet_arg)
    sleep(1)  # By some reason registry is not updated after uninstalling without the sleep
    assert search_installed_npp() is None


def skip_if_npp_is_installed(f: Callable) -> Callable:
    decorator = pytest.mark.skipif(
        condition='search_installed_npp() is not None',
        reason="Installed Notepad++ found. Aborting to not break the system."
    )
    return decorator(f)


@skip_if_npp_is_installed
def test_npp(npp_installed_app):
    assert npp_installed_app.name == NPP_NAME
    assert npp_installed_app.version == NPP_VERSION
    assert npp_installed_app.publisher == NPP_PUBLISHER
