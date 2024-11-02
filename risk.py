import numpy as np
import matplotlib.pyplot as plt

# Define the data for the years
years = np.arange(2022, 2033)  # From 2022 to 2032
risk_per_infection = 0.13  # 13% risk per infection

# Adjusted parameters for initial infection rate and starting LC prevalence
initial_infection_rate = 0.075  # Starting midpoint of 5-10% infected by 2022 (7.5%)
initial_LC_rate = initial_infection_rate * risk_per_infection  # Starting baseline LC prevalence (0.975%)

# Define different infection rate scenarios
annual_infection_rates = {
    "0.5 infections/year": 0.5,
    "1 infection/year": 1.0,
    "3 infections/year": 3.0
}

# Dictionary to store results for each scenario
all_scenarios_risk = {}

# Calculate for each scenario
for scenario, infection_rate in annual_infection_rates.items():
    cumulative_LC_risk = [initial_LC_rate]
    
    for n in range(1, len(years)):
        # Calculate new infections based on the annual rate
        remaining_uninfected = 1 - cumulative_LC_risk[-1]
        new_LC_risk = remaining_uninfected * (1 - (1 - risk_per_infection) ** infection_rate)
        cumulative_LC_risk.append(cumulative_LC_risk[-1] + new_LC_risk)
    
    all_scenarios_risk[scenario] = np.array(cumulative_LC_risk) * 100

# Plotting with enhanced styling
plt.style.use('seaborn-v0_8')  # Use seaborn style for better aesthetics
fig, ax = plt.subplots(figsize=(12, 8), dpi=300)  # Higher resolution and larger figure

# Plot with enhanced styling
colors = ['#27AE60', '#2E86C1', '#E74C3C']  # Green (slow), Blue (medium), Red (fast)

for (scenario, risk_values), color in zip(all_scenarios_risk.items(), colors):
    line = ax.plot(years, risk_values, 
            marker='o', 
            linestyle='-', 
            color=color,
            linewidth=2.5,
            markersize=8,
            label=scenario)
    
    # Add data labels for each point
    for x, y in zip(years, risk_values):
        ax.annotate(f'{y:.1f}%', 
                    (x, y),
                    textcoords="offset points",
                    xytext=(0,10),
                    ha='center',
                    fontsize=9)

# Add legend
ax.legend(fontsize=10, loc='upper left')

# Enhance grid and spines
ax.grid(True, linestyle='--', alpha=0.7)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Improve labels and title
ax.set_xlabel("Year", fontsize=12, fontweight='bold')
ax.set_ylabel("Cumulative Long COVID Risk (%)", fontsize=12, fontweight='bold')
ax.set_title("Projected Cumulative Long COVID Risk by Infection Rate\n(5-10% Initial Infection Rate in 2022)", 
         fontsize=14, 
         fontweight='bold', 
         pad=20)

# Adjust layout and save
plt.tight_layout()
plt.savefig('cumulative_long_covid_risk.png', 
            bbox_inches='tight', 
            dpi=300)
