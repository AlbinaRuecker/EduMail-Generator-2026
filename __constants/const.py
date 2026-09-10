"""
Constants and Configuration Module for EduMail Generator 2026
==============================================================
This module contains all configuration data, college information,
and generates fake student data using Faker library.

Compatibility: Python 3.7+, Faker 8.x+
Last Updated: September 2026
"""

from faker import Faker
import random

######## This script is only for educational purpose ########
######## use it on your own RISK ########
######## I'm not responsible for any loss or damage ########
######## caused to you using this script ########

# ============================================
# COLLEGE REGISTRATION URLS AND DATA
# ============================================

# Base URL for college application portal
start_url = 'https://www.opencccapply.net/gateway/apply?cccMisCode='

# College identification codes (used in URL: start_url + clg_id)
clg_ids = [
    '941',   # MSJC College
    '311',   # Contra Costa College
    '361',   # City College
    '233'    # Sacramento College
]

# Full college names (displayed to user)
allColleges = [
    'MSJC College',
    'Contra Costa College',
    'City College',
    'Sacramento College'
]

# ============================================
# PHONE NUMBER CONFIGURATION
# ============================================

# Valid country codes for phone numbers
# These are used as area codes (first 3 digits)
country_codes = [
    '855',   # Cambodia (for randomness)
    '561',   # Florida, USA
    '800',   # Toll-free
    '325',   # Texas, USA
    '330',   # Ohio, USA
    '229'    # Georgia, USA
]

# ============================================
# FAKE DATA GENERATION USING FAKER
# ============================================

# Initialize Faker with US locale for realistic US addresses and names
fake = Faker('en_US')

# Generate a fake name and split it into first and last name
fake_name = fake.name().split(' ')

firstName = fake_name[0]      # First name
LastName = fake_name[1] if len(fake_name) > 1 else 'Smith'  # Last name (with fallback)

# Generate a fake US address
studentAddress = fake.address()

# Generate random birth date (between 1996-1999, age 25-30 in 2026)
randomMonth = random.randint(1, 12)
randomDay = random.randint(1, 27)   # 1-27 to avoid invalid dates like Feb 29/30
randomYear = random.randint(1996, 1999)

# Generate random high school graduation date
randomEduMonth = random.randint(1, 12)
randomEduDay = random.randint(1, 27)

# High school graduation years (2019 or 2020)
eduYears = [2019, 2020]
randomEduYear = random.choice(eduYears)

# ============================================
# DATA VALIDATION HELPERS
# ============================================

def validate_college_id(college_id):
    """
    Validate if the college ID is valid.
    
    Args:
        college_id (int): College ID (1-4)
        
    Returns:
        bool: True if valid, False otherwise
    """
    return 1 <= college_id <= len(allColleges)


def get_college_info(index):
    """
    Get college information by index.
    
    Args:
        index (int): College index (0-3)
        
    Returns:
        dict: College information {name, id, url}
    """
    if 0 <= index < len(allColleges):
        return {
            'name': allColleges[index],
            'id': clg_ids[index],
            'url': start_url + clg_ids[index]
        }
    return None


def regenerate_student_data():
    """
    Regenerate all fake student data (useful for retries).
    
    Returns:
        dict: New student data {firstName, lastName, address, birthDate, eduDate}
    """
    global firstName, LastName, studentAddress
    global randomMonth, randomDay, randomYear
    global randomEduMonth, randomEduDay, randomEduYear
    
    # Regenerate name
    fake_name = fake.name().split(' ')
    firstName = fake_name[0]
    LastName = fake_name[1] if len(fake_name) > 1 else 'Smith'
    
    # Regenerate address
    studentAddress = fake.address()
    
    # Regenerate birth date
    randomMonth = random.randint(1, 12)
    randomDay = random.randint(1, 27)
    randomYear = random.randint(1996, 1999)
    
    # Regenerate education dates
    randomEduMonth = random.randint(1, 12)
    randomEduDay = random.randint(1, 27)
    randomEduYear = random.choice(eduYears)
    
    return {
        'firstName': firstName,
        'lastName': LastName,
        'address': studentAddress,
        'birthDate': f"{randomMonth}/{randomDay}/{randomYear}",
        'eduDate': f"{randomEduMonth}/{randomEduDay}/{randomEduYear}"
    }


# ============================================
# DEBUG/TEST DATA
# ============================================

if __name__ == "__main__":
    """Test module by printing generated data"""
    print("=" * 50)
    print("EduMail Generator - Constants Module Test")
    print("=" * 50)
    print(f"\nStudent Information:")
    print(f"  Name: {firstName} {LastName}")
    print(f"  Address: {studentAddress}")
    print(f"  Birth Date: {randomMonth}/{randomDay}/{randomYear}")
    print(f"  Education: {randomEduMonth}/{randomEduDay}/{randomEduYear}")
    print(f"\nAvailable Colleges:")
    for i, college in enumerate(allColleges, 1):
        print(f"  {i}. {college}")
    print("=" * 50)
