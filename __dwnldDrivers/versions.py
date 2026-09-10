"""
WebDriver Version Manager for EduMail Generator 2026
=====================================================
This module manages browser driver (ChromeDriver, GeckoDriver) downloads
and installation based on installed browser versions.

IMPORTANT: This module uses webdriver-manager library (Python 3.7+)
which automatically downloads and manages drivers - much simpler than the old system.

Compatibility: Python 3.7+, webdriver-manager 4.x
Last Updated: September 2026
"""

import sys
import os
import subprocess
import platform

# Try to import webdriver_manager, install if not available
try:
    from webdriver_manager.chrome import ChromeDriverManager
    from webdriver_manager.firefox import GeckoDriverManager
    from webdriver_manager.core.utils import ChromeType
except ImportError:
    print("[!] Installing webdriver-manager...")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'webdriver-manager'])
    from webdriver_manager.chrome import ChromeDriverManager
    from webdriver_manager.firefox import GeckoDriverManager
    from webdriver_manager.core.utils import ChromeType

######## This script is only for educational purpose ########
######## use it on your own RISK ########
######## I'm not responsible for any loss or damage ########
######## caused to you using this script ########

# ============================================
# PLATFORM AND ARCHITECTURE DETECTION
# ============================================

def get_os_info():
    """
    Detect current operating system and architecture.
    
    Returns:
        dict: {os_name: 'windows'/'linux'/'darwin', arch: '32'/'64'}
    """
    system = platform.system().lower()
    architecture = '64' if sys.maxsize > 2**32 else '32'
    
    if system == 'windows':
        return {'os_name': 'windows', 'arch': architecture}
    elif system == 'darwin':
        return {'os_name': 'mac', 'arch': '64'}  # macOS is always 64-bit
    else:
        return {'os_name': 'linux', 'arch': architecture}


def get_browser_version(browser_name):
    """
    Detect installed browser version.
    
    Args:
        browser_name (str): 'chrome' or 'firefox'
        
    Returns:
        str: Browser version string or None if not found
    """
    try:
        if browser_name.lower() == 'chrome':
            return _get_chrome_version()
        elif browser_name.lower() == 'firefox':
            return _get_firefox_version()
    except Exception as e:
        print(f"[!] Error detecting {browser_name} version: {str(e)}")
        return None


def _get_chrome_version():
    """
    Get Google Chrome/Chromium version for current OS.
    
    Returns:
        str: Chrome version or None
    """
    system = platform.system().lower()
    
    try:
        if system == 'windows':
            # Windows: Query registry for Chrome version
            result = subprocess.run(
                ['reg', 'query', 'HKEY_CURRENT_USER\\Software\\Google\\Chrome\\BLBeacon', 
                 '/v', 'version'],
                capture_output=True,
                text=True
            )
            if result.returncode == 0:
                version = result.stdout.strip().split()[-1]
                return version.split('.')[0]  # Return major version
                
        elif system == 'darwin':
            # macOS: Check app version
            result = subprocess.run(
                ['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', '--version'],
                capture_output=True,
                text=True
            )
            if result.returncode == 0:
                return result.stdout.strip().split()[-1].split('.')[0]
                
        elif system == 'linux':
            # Linux: Check installed version
            result = subprocess.run(
                ['google-chrome', '--version'],
                capture_output=True,
                text=True
            )
            if result.returncode == 0:
                return result.stdout.strip().split()[-1].split('.')[0]
    except Exception:
        pass
    
    return None


def _get_firefox_version():
    """
    Get Firefox version for current OS.
    
    Returns:
        str: Firefox version or None
    """
    system = platform.system().lower()
    
    try:
        if system == 'windows':
            paths = [
                'C:\\Program Files\\Mozilla Firefox\\firefox.exe',
                'C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe'
            ]
            for path in paths:
                if os.path.exists(path):
                    result = subprocess.run(
                        [path, '--version'],
                        capture_output=True,
                        text=True
                    )
                    if result.returncode == 0:
                        return result.stdout.strip().split()[-1].split('.')[0]
                        
        elif system == 'darwin':
            # macOS
            result = subprocess.run(
                ['/Applications/Firefox.app/Contents/MacOS/firefox', '--version'],
                capture_output=True,
                text=True
            )
            if result.returncode == 0:
                return result.stdout.strip().split()[-1].split('.')[0]
                
        elif system == 'linux':
            # Linux
            result = subprocess.run(
                ['firefox', '--version'],
                capture_output=True,
                text=True
            )
            if result.returncode == 0:
                return result.stdout.strip().split()[-1].split('.')[0]
    except Exception:
        pass
    
    return None


# ============================================
# DRIVER SETUP (NEW SYSTEM - webdriver-manager)
# ============================================

def setup_chrome_driver():
    """
    Setup ChromeDriver using webdriver-manager.
    Automatically downloads the correct version for your Chrome browser.
    
    Returns:
        str: Path to chromedriver executable or None if failed
    """
    try:
        print("[*] Detecting Chrome version...")
        chrome_version = get_browser_version('chrome')
        
        if chrome_version:
            print(f"[✓] Chrome version detected: {chrome_version}")
        else:
            print("[!] Chrome not found, trying to download latest driver...")
        
        print("[*] Downloading ChromeDriver...")
        driver_path = ChromeDriverManager().install()
        print(f"[✓] ChromeDriver installed: {driver_path}")
        return driver_path
        
    except Exception as e:
        print(f"[!] Error setting up ChromeDriver: {str(e)}")
        return None


def setup_firefox_driver():
    """
    Setup GeckoDriver (Firefox) using webdriver-manager.
    Automatically downloads the correct version for your Firefox browser.
    
    Returns:
        str: Path to geckodriver executable or None if failed
    """
    try:
        print("[*] Detecting Firefox version...")
        firefox_version = get_browser_version('firefox')
        
        if firefox_version:
            print(f"[✓] Firefox version detected: {firefox_version}")
        else:
            print("[!] Firefox not found, trying to download latest driver...")
        
        print("[*] Downloading GeckoDriver...")
        driver_path = GeckoDriverManager().install()
        print(f"[✓] GeckoDriver installed: {driver_path}")
        return driver_path
        
    except Exception as e:
        print(f"[!] Error setting up GeckoDriver: {str(e)}")
        return None


# ============================================
# LEGACY FUNCTION COMPATIBILITY
# ============================================

def get_firefox_version():
    """
    Legacy function for backward compatibility.
    
    Returns:
        str: Firefox version or None
    """
    return _get_firefox_version()


def get_chrome_version():
    """
    Legacy function for backward compatibility.
    
    Returns:
        str: Chrome version or None
    """
    return _get_chrome_version()


def setup_Firefox(firefox_ver=None):
    """
    Legacy function for backward compatibility with old setup.py.
    
    Args:
        firefox_ver (str): Firefox version (optional, auto-detected if not provided)
        
    Returns:
        str: Path to geckodriver
    """
    return setup_firefox_driver()


def setup_Chrome(chrome_ver=None):
    """
    Legacy function for backward compatibility with old setup.py.
    
    Args:
        chrome_ver (str): Chrome version (optional, auto-detected if not provided)
        
    Returns:
        str: Path to chromedriver
    """
    return setup_chrome_driver()


# ============================================
# DEBUG/TEST FUNCTIONS
# ============================================

def test_driver_setup():
    """
    Test driver detection and download.
    """
    print("=" * 60)
    print("WebDriver Manager - Test Mode")
    print("=" * 60)
    
    os_info = get_os_info()
    print(f"\n[*] Operating System: {os_info['os_name'].upper()}")
    print(f"[*] Architecture: {os_info['arch']}-bit")
    
    print("\n[*] Checking browsers...")
    chrome_ver = get_browser_version('chrome')
    firefox_ver = get_browser_version('firefox')
    
    if chrome_ver:
        print(f"[✓] Chrome found: v{chrome_ver}")
    else:
        print("[!] Chrome not found")
    
    if firefox_ver:
        print(f"[✓] Firefox found: v{firefox_ver}")
    else:
        print("[!] Firefox not found")
    
    print("\n" + "=" * 60)


if __name__ == "__main__":
    test_driver_setup()
