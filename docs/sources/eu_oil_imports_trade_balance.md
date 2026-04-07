# Source: EU Oil Imports & Energy Trade Balance

**Publishers:**
- Eurostat — dataset `nrg_ti_oil` (oil imports by product and partner country)
- IEA — Oil Market Report, World Energy Outlook
- European Commission DG Energy — Weekly Oil Bulletin

**URLs:**
- https://ec.europa.eu/eurostat/databrowser/product/view/NRG_TI_OIL
- https://www.iea.org/reports/oil-market-report
- https://energy.ec.europa.eu/data-and-analysis/weekly-oil-bulletin_en

**Data retrieved:** Training data knowledge cutoff (early 2025); not live-fetched

---

## EU27 Oil Import Overview (2024 estimates)

| Metric | Value |
|--------|-------|
| Total crude oil imports | ~3.0–3.5 million barrels/day |
| Annual crude oil imports | ~1.1–1.3 billion barrels/year |
| Import value (at $80/barrel) | ~€90–105B/year (crude only) |
| Total energy import bill (all fuels) | ~€300–400B/year |
| Transport share of oil consumption | ~30–35% |
| Passenger car share of transport fuel | ~55–60% |
| Passenger car crude oil demand | ~180–270 million barrels/year |

*Note: EU energy import bill peaked at ~€600B in 2022 following Russia-Ukraine war energy shock; normalised significantly by 2024.*

---

## Per-Vehicle Oil Consumption Parameters

| Parameter | Value | Basis |
|-----------|-------|-------|
| Average annual km (EU passenger car) | 12,000 km | Eurostat transport statistics |
| Average fuel consumption (EU fleet avg.) | 7.0 L/100km | EEA CO2 monitoring data (blended petrol/diesel) |
| Annual fuel use per ICE car | 840 litres | Derived |
| Crude-to-motor-fuel refinery yield | ~65% (blended) | IEA refining statistics |
| Crude oil equivalent per car | ~8.1 barrels/year | Derived (840L ÷ 0.65 ÷ 159L/barrel) |
| Import cost per car at $80/bbl | ~€600/year | Derived |

---

## Oil Displacement by EV Fleet Size

| BEV Fleet | Annual Fuel Displaced | Crude Displaced | Import Savings (€80/bbl) |
|-----------|----------------------|-----------------|--------------------------|
| 6.8M (2025) | 5.7B litres | 46M barrels | ~€2.8B |
| 14.9M (2030 conservative) | 12.5B litres | 101M barrels | ~€6.1B |
| 18.1M (2030 base case) | 15.2B litres | 123M barrels | ~€7.4B |
| 22.2M (2030 accelerated) | 18.6B litres | 150M barrels | ~€9.0B |

---

## Oil Price Assumptions

| Scenario | Price Used | Basis |
|----------|------------|-------|
| Central | $80/barrel (Brent crude) | IEA Stated Policies Scenario 2025–2030 |
| Low | $65/barrel | IEA Sustainable Development Scenario |
| High | $100/barrel | Supply disruption / OPEC+ constraint scenario |

---

## How to Verify

1. **Eurostat oil imports:** https://ec.europa.eu/eurostat/databrowser/product/view/NRG_TI_OIL
   - Filter: product = crude oil, reporter = EU27, time = annual
2. **IEA data:** https://www.iea.org/data-and-statistics
   - "Oil supply" > "Imports" > filter OECD Europe
3. **Weekly oil prices:** https://energy.ec.europa.eu/data-and-analysis/weekly-oil-bulletin_en
