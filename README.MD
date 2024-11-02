# Long COVID Risk Projection (2022-2032)

This project visualizes the projected cumulative risk of Long COVID (LC) in the U.S. population over the period from 2022 to 2032. The analysis models the cumulative risk based on infection rates and per-infection LC risk estimates, using data sourced from reputable sources on COVID-19 infections and population estimates.

## Overview

The purpose of this project is to estimate the cumulative portion of the population at risk of Long COVID over time, given that repeated COVID-19 infections increase the likelihood of developing LC. This model assumes that, on average, individuals are infected once per year post-2022 and that each infection presents a consistent risk of developing LC.

## Data Sources

The data and assumptions in this project are drawn from the following sources:

1. **Long COVID Risk per Infection**  
   - Risk estimates:
      - **13%** after the first infection
      - **23%** cumulative after a second infection
      - **37%** cumulative after a third infection  
   - **Source:** [Institut national de santé publique du Québec](https://www.inspq.qc.ca/publications/3510)

2. **Canadian COVID-19 Infection Statistics**  
   - Approximately **5%** of the Canadian population was infected by early 2022.  
   - **Source:** [COVID-19 Immunity Task Force](https://www.covid19immunitytaskforce.ca/seroprevalence-in-canada/)

3. **Estimated U.S. Infections Post-2022**  
   - Total U.S. infections to date: **1,300 million**.
   - **80%** of these infections (1,040 million) occurred after 2022.  
   - **Source:** [World Population Review](https://worldpopulationreview.com/countries/united-states)

4. **U.S. Population Estimate (2024)**  
   - Current U.S. population: **346 million**.  
   - **Source:** [World Population Review](https://worldpopulationreview.com/countries/united-states)

5. **Average Infections per Person per Year**  
   - Average rate assumed at **1 infection per person per year** from 2022 to 2032.

## Model Assumptions

The model uses the following assumptions to project the cumulative risk:

- **Per-Infection LC Risk**: Each infection has a consistent 13% risk of causing LC.
- **Independence of Infections**: Infections are treated as independent events, allowing us to use a cumulative risk formula.
- **Average Infections per Year**: We assume each person is infected once per year post-2022.
- **Starting Point**: By the beginning of 2022, everyone has been infected at least once, with an initial LC risk of 13%.

## Methodology

The model calculates the cumulative risk of developing Long COVID for each person based on the probability of avoiding LC across multiple infections. The formula used is:

\[
P(n) = 1 - (1 - p)^n
\]

Where:
- \( P(n) \) is the cumulative probability of having LC after \( n \) infections.
- \( p \) is the per-infection risk (13% or 0.13).
- \( n \) is the cumulative number of infections.

The cumulative risk of LC increases each year as the number of infections grows, reflecting the rising likelihood of developing LC over repeated exposures.

## Results

The key results of the model, as visualized in the included plot, show the estimated cumulative LC risk over time:

- **2022**: 13% risk after the first infection.
- **2026**: Approximately 50% risk after five infections.
- **2032**: Approximately 78% risk after ten infections.

## Limitations

This model is a simplified projection and is based on the following limitations:

1. **Constant Risk per Infection**: The model assumes a stable 13% LC risk per infection, though real-world factors (e.g., virus mutations, public health measures, vaccinations) may affect this rate.
2. **Infection Rate Uniformity**: We assume everyone is infected once per year, which may not reflect actual individual variation.
3. **Population Behavior and Immunity**: Changes in public health, immunity duration, and individual behaviors could influence infection rates and LC risk in unpredictable ways.

## Conclusion

The results suggest that, under the given assumptions, a significant portion of the population may face a cumulative risk of developing Long COVID over a ten-year period. This projection underscores the potential long-term impact of COVID-19 on public health and highlights the importance of ongoing public health efforts to mitigate transmission and manage LC risks.
