"""
WebDriver Manager - Browser Driver Detection and Setup
=======================================================
Detects installed browsers (Chrome, Firefox) and manages WebDriver installation.

Key Changes from 2023 version:
  - Removed manual driver downloads (chromedriver.storage.googleapis.com is shut down)
  - Now uses webdriver-manager for automatic management
  - Simplified browser detection
  - Better platform/architecture detection

Usage:
    from __dwnldDrivers.versions import get_firefox_version, get_chrome_version
    from __dwnldDrivers.versions import setup_firefox_driver, setup_chrome_driver
    
    firefox_ver = get_firefox_version()
    if firefox_ver:
        setup_firefox_driver()  # Automatically downloads GeckoDriver

Python Version: 3.7+
Last Updated: September 2026
"""

import sys
import os
import subprocess
import platform as system_platform

######## This script is only for educational purpose ########
######## use it on your own RISK ########
######## I'm not responsible for any loss or damage ########
######## caused to you using this script ########

# ============================================
# IMPORTS
# ============================================

try:
    import requests
except ImportError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'requests', '-q'])
finally:
    import requests

# Import webdriver-manager (NEW - 2026)
try:
    from webdriver_manager.chrome import ChromeDriverManager
    from webdriver_manager.firefox import GeckoDriverManager
except ImportError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'webdriver-manager', '-q'])
finally:
    from webdriver_manager.chrome import ChromeDriverManager
    from webdriver_manager.firefox import GeckoDriverManager

# ============================================
# PLATFORM & ARCHITECTURE DETECTION
# ============================================

def get_platform():
    """
    Detect the operating system platform.
    
    Returns:
        str: 'linux', 'darwin' (macOS), or 'win' (Windows)
    """
    if sys.platform.startswith('linux'):
        return 'linux'
    elif sys.platform == 'darwin':
        return 'darwin'
    elif sys.platform.startswith('win'):
        return 'win'
    else:
        return None


def get_architecture():
    """
    Detect system architecture (32-bit or 64-bit).
    
    Returns:
        str: '32' or '64' (bit)
    """
    if sys.maxsize > 2 ** 32:
        return '64'
    else:
        return '32'


def get_os_info():
    """
    Get comprehensive OS information.
    
    Returns:
        dict: Contains platform, architecture, system name
    """
    return {
        'platform': get_platform(),
        'architecture': get_architecture(),
        'system': system_platform.system(),
        'release': system_platform.release(),
    }


# ============================================
# BROWSER VERSION DETECTION - FIREFOX
# ============================================

def get_firefox_version():
    """
    Detect installed Firefox browser version.
    
    Tries multiple methods depending on platform:
      - Linux: Run 'firefox --version' command
      - macOS: Check /Applications/Firefox.app/
      - Windows: Check registry (HKEY_CURRENT_USER\\Software\\Mozilla\\Mozilla Firefox)
    
    Returns:
        str: Firefox version (e.g., "115.0") or None if not found
    """
    platform = get_platform()
    
    try:
        if platform == 'linux':
            # Linux: Use 'firefox --version' command
            try:
                with subprocess.Popen(['firefox', '--version'], 
                                      stdout=subprocess.PIPE, 
                                      stderr=subprocess.PIPE) as proc:
                    output = proc.stdout.read().decode('utf-8')
                    version = output.replace('Mozilla Firefox', '').strip()
                    return version if version else None
            except FileNotFoundError:
                return None
        
        elif platform == 'darwin':
            # macOS: Check Firefox.app path
            try:
                process = subprocess.Popen(
                    ['/Applications/Firefox.app/Contents/MacOS/firefox', '--version'],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE
                )
                output = process.communicate()[0].decode('utf-8')
                version = output.replace('Mozilla Firefox', '').strip()
                return version if version else None
            except (FileNotFoundError, OSError):
                return None
        
        elif platform == 'win':
            # Windows: Check registry
            try:
                import winreg
                reg = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
                key = winreg.OpenKey(reg, r'Software\Mozilla\Mozilla Firefox')
                value, _ = winreg.QueryValueEx(key, 'CurrentVersion')
                winreg.CloseKey(key)
                return value if value else None
            except (ImportError, OSError, FileNotFoundError):
                return None
        
        else:
            return None
    
    except Exception as e:
        print(f"Error detecting Firefox version: {str(e)}")
        return None


# ============================================
# BROWSER VERSION DETECTION - CHROME
# ============================================

def get_chrome_version():
    """
    Detect installed Google Chrome browser version.
    
    Tries multiple methods depending on platform:
      - Linux: Run 'google-chrome --version' command
      - macOS: Check /Applications/Google Chrome.app/
      - Windows: Check registry (HKEY_CURRENT_USER\\Software\\Google\\Chrome\\BLBeacon)
    
    Returns:
        str: Chrome version (e.g., "120.0.0.0") or None if not found
    """
    platform = get_platform()
    
    try:
        if platform == 'linux':
            # Linux: Use 'google-chrome --version' command
            try:
                with subprocess.Popen(['google-chrome', '--version'],
                                      stdout=subprocess.PIPE,
                                      stderr=subprocess.PIPE) as proc:
                    output = proc.stdout.read().decode('utf-8')
                    version = output.replace('Google Chrome', '').replace('Chromium', '').strip()
                    return version if version else None
            except FileNotFoundError:
                try:
                    # Try 'chromium' command as fallback
                    with subprocess.Popen(['chromium', '--version'],
                                          stdout=subprocess.PIPE,
                                          stderr=subprocess.PIPE) as proc:
                        output = proc.stdout.read().decode('utf-8')
                        version = output.replace('Chromium', '').strip()
                        return version if version else None
                except FileNotFoundError:
                    return None
        
        elif platform == 'darwin':
            # macOS: Check Chrome.app path
            try:
                process = subprocess.Popen(
                    ['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', '--version'],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE
                )
                output = process.communicate()[0].decode('utf-8')
                version = output.replace('Google Chrome', '').strip()
                return version if version else None
            except (FileNotFoundError, OSError):
                return None
        
        elif platform == 'win':
            # Windows: Check registry
            try:
                import winreg
                reg = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
                key = winreg.OpenKey(reg, r'Software\Google\Chrome\BLBeacon')
                version, _ = winreg.QueryValueEx(key, 'version')
                winreg.CloseKey(key)
                return version if version else None
            except (ImportError, OSError, FileNotFoundError):
                return None
        
        else:
            return None
    
    except Exception as e:
        print(f"Error detecting Chrome version: {str(e)}")
        return None


# ============================================
# WEBDRIVER SETUP - FIREFOX (NEW - 2026)
# ============================================

def setup_firefox_driver():
    """
    Setup and download GeckoDriver for Firefox automatically.
    
    Uses webdriver-manager to:
      1. Detect platform and architecture
      2. Download correct GeckoDriver version
      3. Cache for future use
      4. Return path to driver executable
    
    Returns:
        str: Path to GeckoDriver executable
        
    Raises:
        Exception: If download or setup fails
        
    Example:
        >>> driver_path = setup_firefox_driver()
        >>> print(driver_path)
        '/home/user/.wdm/drivers/geckodriver/linux64/v0.33.3/geckodriver'
    """
    try:
        print(f"Setting up GeckoDriver for Firefox...")
        
        # webdriver-manager handles everything automatically
        driver_path = GeckoDriverManager().install()
        
        print(f"✓ GeckoDriver setup complete: {driver_path}")
        return driver_path
    
    except Exception as e:
        print(f"✗ Error setting up GeckoDriver: {str(e)}")
        raise


# ============================================
# WEBDRIVER SETUP - CHROME (NEW - 2026)
# ============================================

def setup_chrome_driver():
    """
    Setup and download ChromeDriver for Chrome automatically.
    
    Uses webdriver-manager to:
      1. Detect platform and architecture
      2. Detect Chrome version
      3. Download matching ChromeDriver version
      4. Cache for future use
      5. Return path to driver executable
    
    Returns:
        str: Path to ChromeDriver executable
        
    Raises:
        Exception: If download or setup fails
        
    Example:
        >>> driver_path = setup_chrome_driver()
        >>> print(driver_path)
        '/home/user/.wdm/drivers/chromedriver/linux64/120.0.0.0/chromedriver'
    """
    try:
        print(f"Setting up ChromeDriver for Chrome...")
        
        # webdriver-manager handles everything automatically
        driver_path = ChromeDriverManager().install()
        
        print(f"✓ ChromeDriver setup complete: {driver_path}")
        return driver_path
    
    except Exception as e:
        print(f"✗ Error setting up ChromeDriver: {str(e)}")
        raise


# ============================================
# UTILITY FUNCTIONS
# ============================================

def get_driver_info():
    """
    Get information about installed drivers.
    
    Returns:
        dict: Information about detected browsers and available drivers
    """
    firefox_version = get_firefox_version()
    chrome_version = get_chrome_version()
    os_info = get_os_info()
    
    return {
        'firefox_version': firefox_version,
        'chrome_version': chrome_version,
        'os_info': os_info,
        'firefox_available': firefox_version is not None,
        'chrome_available': chrome_version is not None,
    }


def print_driver_info():
    """
    Print formatted information about detected browsers.
    Useful for debugging.
    """
    info = get_driver_info()
    os_info = info['os_info']
    
    print("\n" + "="*50)
    print("System Information:")
    print(f"  OS: {os_info['system']} ({os_info['release']})")
    print(f"  Architecture: {os_info['architecture']}-bit")
    print("\nBrowser Versions:")
    
    if info['firefox_available']:
        print(f"  ✓ Firefox: {info['firefox_version']}")
    else:
        print(f"  ✗ Firefox: Not installed")
    
    if info['chrome_available']:
        print(f"  ✓ Chrome: {info['chrome_version']}")
    else:
        print(f"  ✗ Chrome: Not installed")
    
    print("="*50 + "\n")


# ============================================
# DEPRECATED FUNCTIONS (KEPT FOR COMPATIBILITY)
# ============================================

def setup_Chrome(version):
    """
    DEPRECATED: Use setup_chrome_driver() instead.
    
    This function is kept for backward compatibility but is no longer
    used in the new webdriver-manager based system.
    
    Args:
        version (str): Chrome version (ignored, webdriver-manager detects it)
    """
    import warnings
    warnings.warn(
        "setup_Chrome() is deprecated. Use setup_chrome_driver() instead.",
        DeprecationWarning,
        stacklevel=2
    )
    try:
        return setup_chrome_driver()
    except Exception as e:
        print(f"Error: {str(e)}")
        return None


def setup_Firefox(firefox_ver):
    """
    DEPRECATED: Use setup_firefox_driver() instead.
    
    This function is kept for backward compatibility but is no longer
    used in the new webdriver-manager based system.
    
    Args:
        firefox_ver (str): Firefox version (ignored, webdriver-manager detects it)
    """
    import warnings
    warnings.warn(
        "setup_Firefox() is deprecated. Use setup_firefox_driver() instead.",
        DeprecationWarning,
        stacklevel=2
    )
    try:
        return setup_firefox_driver()
    except Exception as e:
        print(f"Error: {str(e)}")
        return None


# ============================================
# MODULE USAGE EXAMPLE
# ============================================

if __name__ == '__main__':
    """
    Example usage when running this script directly.
    """
    print_driver_info()
    
    firefox_version = get_firefox_version()
    chrome_version = get_chrome_version()
    
    if firefox_version:
        print(f"Setting up Firefox driver...")
        try:
            gecko_path = setup_firefox_driver()
            print(f"Firefox driver ready at: {gecko_path}")
        except Exception as e:
            print(f"Failed to setup Firefox driver: {str(e)}")
    
    if chrome_version:
        print(f"\nSetting up Chrome driver...")
        try:
            chrome_path = setup_chrome_driver()
            print(f"Chrome driver ready at: {chrome_path}")
        except Exception as e:
            print(f"Failed to setup Chrome driver: {str(e)}")
