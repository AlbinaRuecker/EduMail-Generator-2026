"""
Color Configuration Module for EduMail Generator 2026
======================================================
This module defines terminal color variables using Colorama library
for consistent colored output across the application.

Compatibility: Python 3.7+, Colorama 0.4.x
Last Updated: September 2026
"""

from colorama import init, Fore, Back, Style

# Initialize colorama with autoreset enabled
# This means each print statement will reset colors automatically
init(autoreset=True)

# ============================================
# FOREGROUND COLORS (Text Color)
# ============================================
fc = Fore.CYAN              # Cyan - Primary accent color
fg = Fore.GREEN             # Green - Success/positive messages
fw = Fore.WHITE             # White - Default text
fr = Fore.RED               # Red - Error/warning messages
fb = Fore.BLUE              # Blue - Information messages
fy = Fore.YELLOW            # Yellow - Progress/status messages
fm = Fore.MAGENTA           # Magenta - Highlight color

# ============================================
# BACKGROUND COLORS (Background Color)
# ============================================
bc = Back.CYAN              # Cyan background
bg = Back.GREEN             # Green background
bw = Back.WHITE             # White background
br = Back.RED               # Red background
bb = Back.BLUE              # Blue background
by = Back.YELLOW            # Yellow background
bm = Back.MAGENTA           # Magenta background

# ============================================
# TEXT STYLES (Font Style)
# ============================================
sd = Style.DIM              # Dim/faint text style
sn = Style.NORMAL           # Normal text style (default)
sb = Style.BRIGHT           # Bright/bold text style
