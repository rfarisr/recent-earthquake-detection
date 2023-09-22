"""
Recent Earthquake Detection Application
MODULARIZATION WITH FUNCTION
"""

import recentearthquake

if __name__ == '__main__':
    print("Main Application")
    result = recentearthquake.data_extraction()
    recentearthquake.display_data(result)
