"""
Banner Display Module for EduMail Generator 2026
=================================================
This module creates an ASCII art banner with random colors
for the application startup screen.

Compatibility: Python 3.7+, Colorama 0.4.x
Last Updated: September 2026
"""

import colorama
import random
import sys

def bannerTop():
    """
    Generate a colorful ASCII art banner for the application.
    
    Returns:
        str: Colored ASCII banner string with random color assignment
        
    Description:
        - Creates a decorative ASCII art banner
        - Each character is assigned a random bright color
        - Uses Colorama for cross-platform color support
        - Includes GitHub repository link
        
    Example:
        >>> banner = bannerTop()
        >>> print(banner)
        # Displays: Rainbow-colored EduMail banner
    """
    
    # ASCII Art Banner - Main Logo
    banner = '''
 _____    _         __  __       _ _    ____
| ____|__| |_   _  |  \/  | __ _(_) |  / ___| ___ _ __
|  _| / _` | | | | | |\/| |/ _` | | | | |  _ / _ \ '_ \\
| |__| (_| | |_| | | |  | | (_| | | | | |_| |  __/ | | |_
|_____\__,_|\__,_| |_|  |_|\__,_|_|_|  \____|\___|_| |_(_)
       Github Repo - https://github.com/NirajShr3stha\n\n
'''
    
    # Define colors to exclude (these don't look good)
    bad_colors = ['BLACK', 'WHITE', 'LIGHTBLACK_EX', 'RESET']
    
    # Get all available colors from colorama.Fore
    codes = vars(colorama.Fore)
    
    # Filter and create a list of usable colors
    colors = [codes[color] for color in codes if color not in bad_colors]
    
    # Assign a random color to each character in the banner
    colored_chars = [random.choice(colors) + char for char in banner]
    
    # Combine all colored characters into a single string
    return ''.join(colored_chars)


# ============================================
# Optional: Alternative banner styles
# ============================================

def bannerSimple():
    """
    Simple text banner without ASCII art.
    
    Returns:
        str: Simple colored banner text
    """
    banner = "=== EduMail Generator 2026 ===\n"
    bad_colors = ['BLACK', 'WHITE', 'LIGHTBLACK_EX', 'RESET']
    codes = vars(colorama.Fore)
    colors = [codes[color] for color in codes if color not in bad_colors]
    colored_chars = [random.choice(colors) + char for char in banner]
    return ''.join(colored_chars)


def bannerMinimal():
    """
    Minimal banner for quiet mode.
    
    Returns:
        str: Minimal banner text
    """
    return "\n[*] EduMail Generator 2026 - Starting...\n"
