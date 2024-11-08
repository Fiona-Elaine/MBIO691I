#load all necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import matplotlib.cm as cm
import svgutils.transform as sg
from svgutils.compose import Figure

#load data
crl = pd.read_csv('coral_forecast.csv')

## Plot 1

# Calculate the mean SST for 2020 and 2100 for each model
mean_SST_2020 = crl.groupby('model')['SST_2020'].mean()
mean_SST_2100 = crl.groupby('model')['SST_2100'].mean()

# Prepare the data for plotting
models = mean_SST_2020.index
sst_2020_values = mean_SST_2020.values
sst_2100_values = mean_SST_2100.values

# Create the line plot
plt.figure(figsize=(8, 6))
plt.plot(models, sst_2020_values, marker='o', label='2020 SST', color='b')
plt.plot(models, sst_2100_values, marker='o', label='2100 SST', color='r')

# Add labels, title, and legend
plt.xlabel('Model')
plt.ylabel('Mean SST (°C)')
plt.title('Mean SST for 2020 and 2100 by Model')
plt.legend(title='Year', bbox_to_anchor=(1.05, 1), loc='upper left')

# Add caption and adjust its position
caption = ("Figure 1: This line plot visualizes mean sea surface temperature (SST) predictions from 2020 to 2100 "
           "across 12 different models. The x-axis represents the different models, while the y-axis shows "
           "the mean SST. The blue line shows the measured SST in 2020, and minimal difference between the models "
           "can be observed. The red line depicts SST levels under different prediction scenarios for each model. "
           "A clear difference in SST predictions for 2100 can be observed between the models.")

# Adjust caption position
plt.figtext(0.5, 0.05, caption, wrap=True, horizontalalignment='center', fontsize=10)

# Adjust layout to give more space for caption
plt.tight_layout(rect=[0, 0.2, 1, 0.95])

# Save the figure as an SVG file
plt.savefig('MeanSST_by_model.svg', format='svg', bbox_inches='tight')

plt.show()



## Plot 2 

# Calculate percentage change in coral cover
crl['coral_cover_change'] = ((crl['coral_cover_2100'] - crl['coral_cover_2020']) / crl['coral_cover_2020']) * 100

# Averaging across sites and grouping by model
averaged_data = crl.groupby('model')[['coral_cover_change', 'PAR']].mean().reset_index()

# Generate 12 distinct colors from 'tab20' colormap
cmap = plt.colormaps['tab20']
colors = [cmap(i) for i in range(12)]

# Scatter Plot with different colors for each model
plt.figure(figsize=(8, 6))

# Plot each model with a different color
for i, model in enumerate(averaged_data['model'].unique()):
    # Filter data for each model
    model_data = averaged_data[averaged_data['model'] == model]
    
    # Scatter plot for each model with a different color
    plt.scatter(model_data['PAR'], model_data['coral_cover_change'], 
                label=f'Model {model}', color=colors[i])  # Use color from list

# Adding title and labels
plt.title('Average Predicted Change in Coral Cover vs PAR')
plt.xlabel('PAR')
plt.ylabel('Average Percentage Change in Coral Cover')

# Show grid and place legend outside the plot on the right
plt.grid(True)
plt.legend(title='Models', loc='center left', bbox_to_anchor=(1.05, 0.5))

# Add caption
caption = ("Figure 2: This scatter plot shows the relationship between the average predicted percentage change "
           "in coral cover (from 2020 to 2100) on the y-axis, in relation to Photosynthetically Available Radiation (PAR) values on the x-axis. "
           "Each point represents a different simulation model, with distinct colors assigned to each model. This "
           "visualization helps explore how variations in PAR may correlate with changes in coral cover across "
           "multiple future climate scenarios. Models predicting medium levels of PAR exhibit the lowest levels of change "
           "in coral cover, while the highest levels of change in coral cover can be observed at the lower and "
           "upper ranges of PAR levels.")

# Adjust the text position and layout in figure
plt.figtext(0.5, 0.05, caption, wrap=True, horizontalalignment='center', fontsize=10)
plt.tight_layout(rect=[0, 0.2, 1, 0.95])  

# Save the figure as an SVG file
plt.savefig('coral_cover_vs_PAR.svg', format='svg', bbox_inches='tight')

# Show the plot
plt.show()



## Plot 3: 

# Calculate percentage change in coral cover
crl['coral_cover_change'] = ((crl['coral_cover_2100'] - crl['coral_cover_2020']) / crl['coral_cover_2020']) * 100

# Averaging across sites and grouping by model
averaged_data = crl.groupby('model')[['coral_cover_change', 'pH_2100']].mean().reset_index()

# Generate 12 distinct colors from 'tab20' colormap
cmap = plt.colormaps['tab20']
colors = [cmap(i) for i in range(12)]

# Scatter Plot with different colors for each model
plt.figure(figsize=(8, 6))

# Plot each model with a different color
for i, model in enumerate(averaged_data['model'].unique()):
    # Filter data for each model
    model_data = averaged_data[averaged_data['model'] == model]
    
    # Scatter plot for each model with a different color
    plt.scatter(model_data['pH_2100'], model_data['coral_cover_change'], 
                label=f'Model {model}', color=colors[i])  

# Adding title and labels
plt.title('Average Predicted Change in Coral Cover vs pH (2100)')
plt.xlabel('pH (2100)')
plt.ylabel('Average Percentage Change in Coral Cover')

# Show grid and legend outside the plot
plt.grid(True)
plt.legend(title='Models', bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

# Add caption
caption = ("Figure: This scatter plot shows the relationship between the average predicted percentage change "
           "in coral cover (from 2020 to 2100) on the y-axis, in relation to pH values on the x-axis. "
           "Each point represents a different simulation model, with distinct colors assigned to each model. "
           "This visualization helps explore how variations in pH may correlate with changes in coral cover across "
           "multiple future climate scenarios. Models predicting moderate pH levels exhibit the lowest levels of change "
           "in coral cover, while the highest levels of change in coral cover can be observed at the lower and "
           "upper ranges of pH levels.")

# Adjust the text position and layout in figure
plt.figtext(0.5, 0.05, caption, wrap=True, horizontalalignment='center', fontsize=10)
plt.tight_layout(rect=[0, 0.2, 1, 0.95])  

# Save the figure as an SVG file
plt.savefig('coral_cover_vs_pH.svg', format='svg', bbox_inches='tight')

# Show the plot
plt.show()



