## Milestone 2 — Feature Engineering & Data Wrangling

The cleaned dataset was enriched with additional features to prepare it for machine learning modeling.

### Features Added:
- DayOfWeek: Captures weekly demand patterns
- Month: Represents seasonal trends
- IsWeekend: Indicates weekend demand spikes
- Lag1 and Lag7: Previous day and previous week demand values
- RollingMean7 and RollingStd7: 7-day demand trends
- Spike: Identifies unusually high demand days

The final dataset was transformed into a model-ready format with consistent schema and time granularity.