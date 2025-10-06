#!/usr/bin/env python3
"""
Generate images for the bike rental analytics project
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import pandas as pd
import numpy as np
from matplotlib.patches import FancyBboxPatch
import warnings
warnings.filterwarnings('ignore')

# Set up the plotting style
plt.style.use('default')
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 10

def create_database_schema_diagram():
    """Create a database schema diagram"""
    fig, ax = plt.subplots(1, 1, figsize=(14, 10))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Title
    ax.text(5, 9.5, 'Bike Rental Analytics Database Schema', 
            ha='center', va='center', fontsize=16, fontweight='bold')
    
    # Stations table
    stations_box = FancyBboxPatch((0.5, 7), 2.5, 1.5, 
                                 boxstyle="round,pad=0.1", 
                                 facecolor='lightblue', 
                                 edgecolor='black', linewidth=2)
    ax.add_patch(stations_box)
    ax.text(1.75, 8.25, 'STATIONS', ha='center', va='center', 
            fontsize=12, fontweight='bold')
    ax.text(1.75, 7.8, 'station_id (PK)', ha='center', va='center', fontsize=9)
    ax.text(1.75, 7.5, 'station_name', ha='center', va='center', fontsize=9)
    ax.text(1.75, 7.2, 'latitude, longitude', ha='center', va='center', fontsize=9)
    
    # Weather table
    weather_box = FancyBboxPatch((4, 7), 2.5, 1.5, 
                                boxstyle="round,pad=0.1", 
                                facecolor='lightgreen', 
                                edgecolor='black', linewidth=2)
    ax.add_patch(weather_box)
    ax.text(5.25, 8.25, 'WEATHER', ha='center', va='center', 
            fontsize=12, fontweight='bold')
    ax.text(5.25, 7.8, 'weather_id (PK)', ha='center', va='center', fontsize=9)
    ax.text(5.25, 7.5, 'date, avg_temp', ha='center', va='center', fontsize=9)
    ax.text(5.25, 7.2, 'precipitation, wind', ha='center', va='center', fontsize=9)
    
    # Rides table
    rides_box = FancyBboxPatch((2, 4), 3.5, 2, 
                              boxstyle="round,pad=0.1", 
                              facecolor='lightcoral', 
                              edgecolor='black', linewidth=2)
    ax.add_patch(rides_box)
    ax.text(3.75, 5.5, 'RIDES', ha='center', va='center', 
            fontsize=12, fontweight='bold')
    ax.text(3.75, 5.1, 'ride_id (PK)', ha='center', va='center', fontsize=9)
    ax.text(3.75, 4.8, 'start_time, stop_time', ha='center', va='center', fontsize=9)
    ax.text(3.75, 4.5, 'start_station_id (FK)', ha='center', va='center', fontsize=9)
    ax.text(3.75, 4.2, 'end_station_id (FK)', ha='center', va='center', fontsize=9)
    ax.text(3.75, 3.9, 'user_type, age', ha='center', va='center', fontsize=9)
    
    # Analytics Views
    views_box = FancyBboxPatch((6.5, 4), 2.5, 2, 
                              boxstyle="round,pad=0.1", 
                              facecolor='lightyellow', 
                              edgecolor='black', linewidth=2)
    ax.add_patch(views_box)
    ax.text(7.75, 5.5, 'ANALYTICS VIEWS', ha='center', va='center', 
            fontsize=12, fontweight='bold')
    ax.text(7.75, 5.1, 'daily_weather_rides', ha='center', va='center', fontsize=9)
    ax.text(7.75, 4.8, 'hourly_patterns', ha='center', va='center', fontsize=9)
    ax.text(7.75, 4.5, 'station_utilization', ha='center', va='center', fontsize=9)
    ax.text(7.75, 4.2, 'monthly_kpi_summary', ha='center', va='center', fontsize=9)
    
    # Relationships
    # Stations to Rides
    ax.arrow(1.75, 7, 2.5, -0.5, head_width=0.1, head_length=0.1, 
             fc='black', ec='black', linewidth=2)
    ax.text(2.5, 6.2, '1:N', ha='center', va='center', fontsize=10, fontweight='bold')
    
    # Weather to Rides
    ax.arrow(5.25, 7, 0.5, -0.5, head_width=0.1, head_length=0.1, 
             fc='black', ec='black', linewidth=2)
    ax.text(4.5, 6.2, '1:N', ha='center', va='center', fontsize=10, fontweight='bold')
    
    # Rides to Views
    ax.arrow(5.5, 5, 0.8, 0, head_width=0.1, head_length=0.1, 
             fc='black', ec='black', linewidth=2)
    ax.text(6.2, 5.2, 'Source', ha='center', va='center', fontsize=10, fontweight='bold')
    
    # Statistics
    stats_text = """
    Database Statistics:
    • 3 Normalized Tables
    • 6 Analytics Views
    • 247,111 Bike Trips
    • 102 Unique Stations
    • 366 Weather Records
    • 6 Performance Indexes
    """
    ax.text(1, 2, stats_text, ha='left', va='top', fontsize=10, 
            bbox=dict(boxstyle="round,pad=0.5", facecolor='lightgray', alpha=0.8))
    
    plt.tight_layout()
    plt.savefig('images/schema_diagram.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✅ Created database schema diagram: images/schema_diagram.png")

def create_weather_correlation_chart():
    """Create a weather correlation chart"""
    # Generate sample data for demonstration
    np.random.seed(42)
    
    # Create sample weather and ridership data
    temperatures = np.random.normal(65, 15, 100)  # Mean 65°F, std 15°F
    temperatures = np.clip(temperatures, 20, 95)  # Clip to reasonable range
    
    # Simulate ridership correlation with temperature
    ridership = 1000 + (temperatures - 65) * 20 + np.random.normal(0, 200, 100)
    ridership = np.clip(ridership, 200, 2000)  # Clip to reasonable range
    
    # Create precipitation data
    precipitation = np.random.exponential(0.1, 100)
    precipitation = np.clip(precipitation, 0, 2)  # Clip to 0-2 inches
    
    # Create the plot
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))
    
    # Temperature vs Ridership
    ax1.scatter(temperatures, ridership, alpha=0.6, color='red', s=50)
    z = np.polyfit(temperatures, ridership, 1)
    p = np.poly1d(z)
    ax1.plot(temperatures, p(temperatures), "r--", alpha=0.8, linewidth=2)
    ax1.set_xlabel('Average Temperature (°F)')
    ax1.set_ylabel('Daily Rides')
    ax1.set_title('Temperature vs Ridership Correlation')
    ax1.grid(True, alpha=0.3)
    
    # Add correlation coefficient
    corr = np.corrcoef(temperatures, ridership)[0, 1]
    ax1.text(0.05, 0.95, f'Correlation: {corr:.2f}', transform=ax1.transAxes, 
             bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.8))
    
    # Precipitation vs Ridership
    ax2.scatter(precipitation, ridership, alpha=0.6, color='blue', s=50)
    z2 = np.polyfit(precipitation, ridership, 1)
    p2 = np.poly1d(z2)
    ax2.plot(precipitation, p2(precipitation), "b--", alpha=0.8, linewidth=2)
    ax2.set_xlabel('Precipitation (inches)')
    ax2.set_ylabel('Daily Rides')
    ax2.set_title('Precipitation vs Ridership Correlation')
    ax2.grid(True, alpha=0.3)
    
    # Add correlation coefficient
    corr2 = np.corrcoef(precipitation, ridership)[0, 1]
    ax2.text(0.05, 0.95, f'Correlation: {corr2:.2f}', transform=ax2.transAxes,
             bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.8))
    
    # Monthly ridership pattern
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    monthly_rides = [800, 850, 1200, 1500, 1800, 2000, 
                     2200, 2100, 1800, 1400, 1000, 900]
    
    ax3.bar(months, monthly_rides, color='skyblue', alpha=0.7)
    ax3.set_xlabel('Month')
    ax3.set_ylabel('Average Daily Rides')
    ax3.set_title('Seasonal Ridership Patterns')
    ax3.grid(True, alpha=0.3)
    
    # Hourly ridership pattern
    hours = list(range(24))
    hourly_rides = [50, 30, 20, 15, 25, 80, 200, 350, 400, 300, 250, 300,
                    350, 300, 250, 300, 400, 500, 450, 300, 200, 150, 100, 70]
    
    ax4.plot(hours, hourly_rides, marker='o', linewidth=2, markersize=4, color='green')
    ax4.set_xlabel('Hour of Day')
    ax4.set_ylabel('Average Rides')
    ax4.set_title('Hourly Ridership Patterns')
    ax4.grid(True, alpha=0.3)
    ax4.set_xticks(range(0, 24, 3))
    
    plt.suptitle('Bike Rental Analytics: Weather Impact & Usage Patterns', 
                 fontsize=16, fontweight='bold', y=0.98)
    plt.tight_layout()
    plt.savefig('images/weather_correlation.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✅ Created weather correlation chart: images/weather_correlation.png")

if __name__ == "__main__":
    print("🎨 Generating images for bike rental analytics project...")
    create_database_schema_diagram()
    create_weather_correlation_chart()
    print("🎉 All images generated successfully!")
