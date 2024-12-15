import datetime
from typing import List, Dict
import matplotlib.pyplot as plt
import numpy as np

def flood_graph(data: List[Dict[str, float]]):
    """
    Visualize river discharge, rainfall, and flood risk data.
    
    Args:
        data (List[Dict[str, float]]): List of dicts with keys 'date', 'discharge', 'rainfall', 'predictedDischarge', 'dangerLevel'.
    """
    # Calculate if there's flood risk
    has_flood_risk = any(point['predictedDischarge'] >= point['dangerLevel'] for point in data)

    # Create figure and axis 
    fig, ax1 = plt.subplots(figsize=(12, 6))
    ax2 = ax1.twinx()

    # Plot discharge and predicted discharge
    dates = [datetime.datetime.strptime(point['date'], '%Y-%m-%d') for point in data]
    ax1.plot(dates, [point['discharge'] for point in data], color='#2563eb', label='Current Discharge')
    ax1.plot(dates, [point['predictedDischarge'] for point in data], color='#7c3aed', linestyle='--', label='Predicted Discharge')
    ax1.plot(dates, [point['dangerLevel'] for point in data], color='#dc2626', linestyle='-', label='Danger Level')
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Discharge (m³/s)', color='#2563eb')
    ax1.tick_params('y', colors='#2563eb')

    # Plot rainfall
    ax2.bar(dates, [point['rainfall'] for point in data], color='#0891b2', label='Rainfall (mm)')
    ax2.set_ylabel('Rainfall (mm)', color='#0891b2')
    ax2.tick_params('y', colors='#0891b2')

    # Add legend and title
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
    ax1.set_title('River Discharge & Rainfall')

    # Show flood risk alert if applicable
    if has_flood_risk:
        print('Flood risk detected! River discharge is predicted to reach danger levels.')

    plt.show()

# Sample data
data = [
    {'date': '2024-01-01', 'discharge': 35000, 'rainfall': 45, 'predictedDischarge': 36000, 'dangerLevel': 45000},
    {'date': '2024-01-02', 'discharge': 37000, 'rainfall': 65, 'predictedDischarge': 39000, 'dangerLevel': 45000},
    {'date': '2024-01-03', 'discharge': 42000, 'rainfall': 85, 'predictedDischarge': 44000, 'dangerLevel': 45000},
    {'date': '2024-01-04', 'discharge': 43000, 'rainfall': 75, 'predictedDischarge': 45000, 'dangerLevel': 45000},
    {'date': '2024-01-05', 'discharge': 41000, 'rainfall': 55, 'predictedDischarge': 42000, 'dangerLevel': 45000},
    {'date': '2024-01-06', 'discharge': 38000, 'rainfall': 35, 'predictedDischarge': 39000, 'dangerLevel': 45000},
    {'date': '2024-01-07', 'discharge': 36000, 'rainfall': 25, 'predictedDischarge': 37000, 'dangerLevel': 45000}
]

flood_graph(data)
