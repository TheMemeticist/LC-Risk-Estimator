# Long COVID Risk Projection (2022-2032)
![LC infections over time](https://github.com/TheMemeticist/LC-Risk-Estimator/blob/main/cumulative_long_covid_risk.png?raw=true)
This project visualizes the projected cumulative risk of Long COVID (LC) in the U.S. population over the period from 2022 to 2032. The analysis models the cumulative risk based on infection rates and per-infection LC risk estimates, using data sourced from reputable sources on COVID-19 infections and population estimates.

## Overview

The purpose of this project is to estimate the cumulative portion of the population at risk of Long COVID over time, given that repeated COVID-19 infections increase the likelihood of developing LC. This model assumes that, on average, individuals are infected once per year post-2022 and that each infection presents a consistent risk of developing LC.

## Data Sources

The data and assumptions in this project are drawn from the following sources:


- **Long COVID Risk per Infection**  
   - Risk estimates:
      - **13%** after the first infection
      - **23%** cumulative after a second infection
      - **37%** cumulative after a third infection  
   - **Source:** [Institut national de santé publique du Québec](https://www.inspq.qc.ca/publications/3510)

- **Increased Risk with Re-infections**  
   - Statistics Canada findings:
      - Canadians with **one infection**: 14.6% reported prolonged symptoms
      - Canadians with **two infections**: 25.4% (1.7 times higher risk than one infection)
      - Canadians with **three or more infections**: 37.9% (2.6 times higher risk than one infection)  
   - **Source:** [Statistics Canada](https://www150.statcan.gc.ca/n1/pub/75-006-x/2023001/article/00015-eng.htm)

- China Survey Says Up to 30% of Adults Felt Long Covid Symptoms. **Source:**[The Lancet](https://www.thelancet.com/journals/lanwpc/article/PIIS2666-6065(24)00212-8/fulltext)


1. **Canadian COVID-19 Infection Statistics**  
   - Approximately **5%** of the Canadian population was infected by early 2022.  
   - **Source:** [COVID-19 Immunity Task Force](https://www.covid19immunitytaskforce.ca/seroprevalence-in-canada/)

2. **Estimated U.S. Infections Post-2022**  
   - Total U.S. infections to date: **1,300 million**.
   - **80%** of these infections (1,040 million) occurred after 2022.  
   - **Source:** [World Population Review](https://worldpopulationreview.com/countries/united-states)

3. **Average Infections per Person per Year**  
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

## The Long COVID Risk

The most severe potential outcome of Long COVID involves several interconnected risks that could create a downward spiral of health and economic consequences:
Scale and Growth
The global burden could exceed 400 million cases by late 2023, with numbers continuing to grow due to reinfections and new variants. This [estimate is likely conservative](https://www.nature.com/articles/s41591-024-03173-6) as it doesn't account for asymptomatic infections.
Medical Challenges
The condition remains poorly understood, with multiple proposed mechanisms including viral persistence, immune dysregulation, and mitochondrial dysfunction. Limited research funding and lack of standardized diagnostic tools hinder treatment development. Without clear understanding of its subtypes, developing targeted therapies remains difficult.
Disability Impact
Studies show concerning low recovery rates, with many cases potentially becoming chronic conditions. A significant portion of affected individuals experience reduced work capacity or complete disability, leading to long-term dependence on support systems.
Economic Consequences
The estimated annual global cost could reach $1 trillion through:

Reduced workforce participation
Increased healthcare costs
Lost productivity
Strain on public finances
Potential labor shortages

Social and Development Impact

Marginalized communities face disproportionate effects and barriers to care
Progress toward Sustainable Development Goals could be undermined
Existing health inequalities may worsen
Access to healthcare and poverty reduction efforts could be reversed

Without effective prevention and treatment strategies, this scenario could result in a significant portion of the population facing chronic illness and disability. The cascading effects would impact all aspects of society, creating a future marked by widespread health challenges and economic hardship.



## Limitations

This model is a simplified projection and is based on the following limitations:

1. **Constant Risk per Infection**: The model assumes a stable 13% LC risk per infection, though real-world factors (e.g., virus mutations, public health measures, vaccinations) may affect this rate.
2. **Infection Rate Uniformity**: We assume everyone is infected once per year, which may not reflect actual individual variation.
3. **Population Behavior and Immunity**: Changes in public health, immunity duration, and individual behaviors could influence infection rates and LC risk in unpredictable ways.

## Conclusion

The results suggest that, under the given assumptions, a significant portion of the population may face a cumulative risk of developing Long COVID over a ten-year period. This projection underscores the potential long-term impact of COVID-19 on public health and highlights the importance of ongoing public health efforts to mitigate transmission and manage LC risks.
