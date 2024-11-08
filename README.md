### MBIO691I Mini-Project

This repository contains the final mini-project for the MBIO 691I course.

---

### Project Overview
This project investigates projected declines in tropical coral cover over the 21st century. The dataset `coral_model.csv` contains simulation outputs for approximately 52,000 sites, comparing coral cover predictions from 2010-2020 and 2090-2100 under 12 different simulation configurations, each with slightly different future climate change predictions (due to uncertainty in future warming/ocean acidification).

Three figures will be created to visually summarise the output of these simulations and exported as SVG files to meet publication image quality expectations.
---

### Data Description
The dataset `coral_model.csv` includes the following columns (described by Noam):

- **coral_cover_2020/2100**: Simulation estimates of tropical coral cover averaged across 2010-2020, and 2090-2100 respectively (km $^2$).
- **SST_2020/SST_2100**: Mean SST (sea-surface temperature) averaged across 2010-2020, and 2090-2100 respectively (degrees C).
- **SST_seasonal**: Amplitude of the seasonal SST cycle, i.e. difference between summer and winter SST (degrees C).
- **pH_2020/pH_2100**: Mean pH averaged across 2010-2020, and 2090-2100 respectively.
- **PAR**: Benthic Photosynthetically Available Radiation (mol m $^{-2}$ d $^{-1}$ ).
- **longitude/latitude**: Longitude/latitude of the site.
- **model**: Simulation configuration, numbered 0-11.

---

### Libraries to Install
To reproduce the analysis and plots, install the following Python libraries:
- **pandas**
- **matplotlib**
- **seaborn**
- **numpy**
---

### Plots

#### Plot 1: Mean SST for 2020 and 2100 by model
This line plot visualizes mean sea surface temperature (SST) predictions from 2020 to 2100 across 12 different models. The x-axis represents the different models, while the y-axis shows the mean SST. The blue line shows the measured SST in 2020 and minimal difference between the models can be observed. The red line depticts SST levels under different prediction scenarios for each model. A clear increase in SST can be observed across models with differences in SST predictions for 2100 between the models.

#### Plot 2: Average predicted change in coral cover relative to PAR levels from 2020 to 2100
This scatter plot shows the average predicted percentage change in coral cover (from 2020 to 2100) on the y-axis, in relationship to Photosynthetically Available Radiation (PAR) values on the x-axis. Each point represents a different simulation model, with distinct colors assigned to each model. This visualization helps explore how variations in PAR may correlate with changes in coral cover across multiple future climate scenarios. Models predicting medium levels of PAR exhibit lowest levels change in coral cover, while the highest levels of change in coral cover can be observed at the lower and upper range of PAR levels.

#### Plot 3: Average predicted change in coral cover relative to pH levels from 2020 to 2100
This scatter plot shows the relationship between the average predicted percentage change in coral cover (from 2020 to 2100) on the y-axis, in relation to pH values on the x-axis. Each point represents a different simulation model, with distinct colors assigned to each model. This visualization helps explore how variations in pH may correlate with changes in coral cover across multiple future climate scenarios. Models predicting moderate pH levels exhibit the lowest levels of change in coral cover, while the highest levels of change in coral cover can be observed at the lower and upper ranges of pH levels.

---

