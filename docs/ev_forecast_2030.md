# EU Electric Vehicle Forecast 2030 & Economic Impact Analysis

**Based on:** EU27 BEV sales data 2016–2025 (see `evs_adoption.md`)  
**Date of analysis:** 2026-04-07  
**Methodology:** Trend extrapolation with regulatory scenario weighting; trade balance modelling

---

## Part 1 — Sales & Fleet Forecast to 2030

### Key Regulatory Drivers

- **EU CO2 fleet targets (Regulation 2019/631 amended):** 55% reduction in new car emissions by 2030 vs 2021 baseline. With the average ICE car at ~120g/km, this pushes manufacturers to target ~30–40% BEV share of new sales by 2030 to remain compliant.
- **2035 ICE ban:** Only zero-emission new cars may be sold after 2035, creating a hard runway for manufacturers who must retool production now.
- **Euro 7 emissions standard:** Higher compliance costs for ICE vehicles from 2026 onward reduce the cost gap relative to EVs.
- **Subsidy environment:** Following Germany's abrupt 2023 withdrawal, subsidy reliance is decreasing; forecasts assume no major new national subsidy programmes, with growth driven instead by price parity and infrastructure.

### Cost Parity Timeline

Battery costs (currently ~$110/kWh in 2025) are projected to reach $75–85/kWh by 2028–2030, the threshold at which BEVs reach sticker-price parity with equivalent ICE vehicles in the EU mid-segment. This is the single most important demand driver in the forecast.

### Three Scenarios

#### Scenario A — Conservative
Assumes persistent demand softness, slow infrastructure rollout, and no new major subsidies. Growth resumes gradually from the 2024–2025 trough.

#### Scenario B — Base Case (most likely)
Assumes battery price parity reached by 2028, steady charging infrastructure expansion (EU target: 1 million public chargers by 2025, 3.5 million by 2030), and moderate regulatory pressure on manufacturers.

#### Scenario C — Accelerated
Assumes early cost parity (2027), strong EU-level support measures (e.g., common charger deployment funds), and competitive pressure from Chinese EV imports driving prices down faster.

---

### Annual BEV Sales Forecast (EU27, thousands)

| Year | Scenario A | Scenario B | Scenario C |
|------|-----------|-----------|-----------|
| 2025 | 1,200 | 1,200 | 1,200 |
| 2026 | 1,300 | 1,450 | 1,650 |
| 2027 | 1,450 | 1,800 | 2,300 |
| 2028 | 1,650 | 2,300 | 3,100 |
| 2029 | 1,850 | 2,800 | 3,900 |
| 2030 | 2,100 | 3,200 | 4,600 |

**2030 BEV share of new car sales** (total EU market ~10M units/year):

| Scenario | 2030 BEV Sales | Share of New Sales |
|----------|---------------|--------------------|
| Conservative | 2.1M | ~21% |
| Base case | 3.2M | ~32% |
| Accelerated | 4.6M | ~46% |

---

### Cumulative Fleet in Circulation by 2030

Starting from ~6.8M BEVs in circulation at end-2025, and applying a blended ~97% annual survival rate (fleet remains very young through 2030):

| Scenario | Additional Sales 2026–2030 | 2025 Fleet Surviving | **Total Fleet 2030** |
|----------|---------------------------|----------------------|----------------------|
| Conservative | ~8.3M | ~6.6M | **~14.9M** |
| Base case | ~11.5M | ~6.6M | **~18.1M** |
| Accelerated | ~15.6M | ~6.6M | **~22.2M** |

**Base case estimate: ~18 million BEVs in circulation in the EU27 by end-2030.**

This would represent approximately **6.4% of the total EU passenger car fleet** (assuming the total fleet grows marginally to ~285M vehicles).

---

## Part 2 — Economic Impact Analysis

### Methodology & Assumptions

| Parameter | Value | Source/Basis |
|-----------|-------|--------------|
| Average annual km driven per car | 12,000 km | Eurostat transport statistics |
| Average ICE fuel consumption | 7.0 L/100km | EEA fleet average (mixed petrol/diesel) |
| Average EV energy consumption | 20 kWh/100km | Industry average (including charging losses) |
| Crude oil price assumption | $75–85/barrel | IEA 2025–2030 range; ~$80 used |
| Crude-to-motor-fuel yield | ~65% (blended petrol+diesel) | IEA refining statistics |
| EU wholesale electricity price | €65–75/MWh | ENTSO-E forward curves |
| EU domestic electricity generation share | ~80% | IEA; accounts for interconnections |

---

### 2.1 — Oil Import Displacement

Each BEV replacing an ICE vehicle avoids the import of approximately:

```
12,000 km × 7 L/100km = 840 L of motor fuel per year
840 L ÷ 0.65 (refinery yield) ÷ 159 L/barrel = ~8.1 barrels of crude oil per year
8.1 barrels × $80 = ~$648 (~€600) in crude oil imports per car per year
```

#### Annual Oil Import Savings by Fleet Size

| Fleet Size | Fuel Displaced (B litres) | Crude Displaced (M barrels) | Import Savings (€B/year) |
|-----------|--------------------------|----------------------------|--------------------------|
| 6.8M (2025) | 5.7 | 46 | ~€2.8B |
| 14.9M (2030 conservative) | 12.5 | 101 | ~€6.1B |
| 18.1M (2030 base case) | 15.2 | 123 | ~€7.4B |
| 22.2M (2030 accelerated) | 18.6 | 150 | ~€9.0B |

**Context:** The EU imports approximately €150–200B of crude oil per year (2024 prices). The base-case 2030 scenario would displace **~4–5% of total EU crude oil imports** from the passenger car segment alone.

---

### 2.2 — Electricity Cost Offset

Charging EVs replaces oil imports with electricity — the vast majority of which (~80%) is generated domestically within the EU from nuclear, hydro, wind, and solar. This is the mechanism by which the trade balance improves.

#### Additional Electricity Demand from EVs

```
Per EV: 12,000 km × 20 kWh/100km = 2,400 kWh/year
18.1M EVs (base 2030): 18.1M × 2,400 kWh = 43.4 TWh/year
```

| Fleet Size | Additional Electricity Demand | % of EU Generation (2,800 TWh) | Electricity Cost (€70/MWh) |
|-----------|------------------------------|-------------------------------|---------------------------|
| 6.8M (2025) | 16.3 TWh | 0.6% | ~€1.1B |
| 18.1M (2030 base) | 43.4 TWh | 1.5% | ~€3.0B |
| 22.2M (2030 accel.) | 53.3 TWh | 1.9% | ~€3.7B |

The additional electricity demand is manageable — **less than 2% of current EU generation** even under the accelerated scenario — and is expected to be absorbed primarily by renewable capacity additions already planned under REPowerEU.

---

### 2.3 — Net Trade Balance Impact

The trade balance gain comes from substituting imported crude oil with domestically generated electricity:

| Scenario (2030) | Oil Import Savings | Electricity Cost (80% domestic) | **Net Trade Balance Improvement** |
|----------------|--------------------|---------------------------------|----------------------------------|
| Conservative | €6.1B | €0.5B (20% imported) | **+€5.6B/year** |
| Base case | €7.4B | €0.6B | **+€6.8B/year** |
| Accelerated | €9.0B | €0.7B | **+€8.3B/year** |

*Electricity import cost = 20% of total electricity cost (the non-domestic share).*

**Cumulative trade balance improvement 2026–2030 (base case):** approximately **€25–30B** over the five-year period, as savings ramp up with fleet growth.

---

### 2.4 — Energy Market Structural Effects

#### Oil Market
- 123M barrels/year displaced by 2030 (base case) is modest relative to global consumption (~35B barrels/year), but significant at the EU level.
- Combined with similar EV growth globally (IEA projects ~20M EV sales globally by 2030), total oil demand suppression from passenger EVs could reach **1.5–2.5 million barrels per day** globally by 2030 — placing downward pressure on oil prices.
- A 10% oil price reduction (plausible under IEA's Stated Policies Scenario) would generate an additional **€15–20B/year in savings** for the EU economy beyond the direct EV displacement effect.

#### Electricity Markets
- EV charging is expected to be largely **smart/off-peak** by 2028–2030, incentivised by time-of-use tariffs. This benefits grid operators by absorbing overnight renewable surplus (solar/wind curtailment reduction).
- 43 TWh of additional flexible demand acts as a **virtual battery** for the grid, reducing the need for expensive peaking capacity and supporting renewable integration.
- Estimated grid balancing value: €1–3B/year by 2030 (ENTSO-E flexibility studies).

#### Geopolitical Energy Dependency
- The EU spent ~€600B on energy imports in 2022 (post-Ukraine war spike). Electrification reduces structural dependency on OPEC+ and Russian pipeline alternatives.
- Every 1M BEVs on EU roads reduces oil import dependency by approximately **€0.4B/year** at $80/barrel, compounding as the fleet grows.

---

### 2.5 — Carbon Market Impact

Each BEV avoids approximately **2.0–2.5 tonnes of CO2 per year** vs the EU average ICE car (well-to-wheel, accounting for EU grid carbon intensity of ~250 gCO2/kWh in 2025, declining to ~180 gCO2/kWh by 2030 as renewables grow).

| Fleet (2030 base) | Annual CO2 Avoided | At €65/tonne EU ETS price |
|-------------------|--------------------|---------------------------|
| 18.1M EVs | ~39 Mt CO2/year | **€2.5B/year in avoided ETS costs** |

This reduces compliance costs for manufacturers and energy-intensive industries covered by EU ETS, with secondary positive effects on trade competitiveness.

---

## Summary Table

| Metric | 2025 (current) | 2030 Conservative | 2030 Base Case | 2030 Accelerated |
|--------|---------------|-------------------|----------------|------------------|
| BEV fleet (M) | 6.8 | 14.9 | 18.1 | 22.2 |
| Share of car fleet | ~2.4% | ~5.2% | ~6.4% | ~7.8% |
| Annual BEV sales (M) | 1.2 | 2.1 | 3.2 | 4.6 |
| Oil displaced (M barrels/yr) | 46 | 101 | 123 | 150 |
| Oil import savings (€B/yr) | €2.8B | €6.1B | €7.4B | €9.0B |
| Additional electricity demand (TWh) | 16.3 | 35.8 | 43.4 | 53.3 |
| Net trade balance gain (€B/yr) | €1.7B | €5.6B | €6.8B | €8.3B |
| CO2 avoided (Mt/yr) | ~15 | ~33 | ~39 | ~49 |

---

## Key Risks to the Base Case

| Risk | Direction | Impact |
|------|-----------|--------|
| Subsidy removal in more member states | Downside | Lower sales volumes; fleet growth slows |
| Chinese EV import tariffs (EU imposed 2024) | Mixed | Reduces competition, keeps prices higher for consumers; slows adoption |
| Charging infrastructure gaps | Downside | Consumer range anxiety persists in southern/eastern EU |
| Battery raw material supply (lithium, cobalt) | Downside | Could delay cost parity timeline by 1–2 years |
| Oil price collapse (<$60/barrel) | Downside | Reduces economic incentive for EV adoption |
| Grid capacity constraints | Downside | Could slow smart charging rollout |
| 2035 ICE ban political reversal | Downside | Reduces manufacturer commitment to EV investment |
| Faster renewable deployment | Upside | Improves EV grid carbon intensity; strengthens economic case |

---

## Data Sources

- EU27 BEV sales 2016–2025: ACEA, EAFO (see `evs_adoption.md`)
- EU oil import volumes and values: Eurostat, IEA Oil Market Report
- EU electricity generation mix and prices: ENTSO-E, IEA World Energy Outlook 2024
- EU ETS carbon price: European Energy Exchange (EEX)
- EV energy consumption benchmarks: Transport & Environment, WLTP homologation data
- Battery cost trajectory: BloombergNEF Electric Vehicle Outlook 2024
- CO2 fleet targets: EU Regulation 2019/631 as amended by Regulation 2023/851
- IEA Global EV Outlook 2024
