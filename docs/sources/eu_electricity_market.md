# Source: EU Electricity Market — Generation, Prices & EV Demand

**Publishers:**
- ENTSO-E (European Network of Transmission System Operators for Electricity)
- Eurostat — dataset `nrg_cb_pem` (electricity production)
- IEA — World Energy Outlook, Electricity Market Report
- European Energy Exchange (EEX) — wholesale electricity prices

**URLs:**
- https://www.entsoe.eu/data/power-stats/
- https://ec.europa.eu/eurostat/databrowser/product/view/NRG_CB_PEM
- https://www.iea.org/reports/electricity-market-report
- https://www.eex.com/en/market-data/power

**Data retrieved:** Training data knowledge cutoff (early 2025); not live-fetched

---

## EU27 Electricity Generation Overview (2024)

| Metric | Value |
|--------|-------|
| Total EU27 electricity generation | ~2,750–2,850 TWh/year |
| Renewables share | ~47% (wind 18%, solar 9%, hydro 12%, bio 8%) |
| Nuclear share | ~23% |
| Fossil fuels share | ~30% (declining) |
| Grid carbon intensity (EU avg.) | ~250 gCO2/kWh (2025 est.) |
| Projected grid carbon intensity (2030) | ~180 gCO2/kWh (REPowerEU trajectory) |

---

## Electricity Price Assumptions

| Segment | Price | Basis |
|---------|-------|-------|
| Wholesale (day-ahead) | €65–75/MWh | ENTSO-E / EEX 2025 averages |
| Retail (household) | €0.25–0.35/kWh | Eurostat energy price statistics |
| Off-peak (EV smart charging) | €0.10–0.18/kWh | Estimated; time-of-use tariff ranges |

*Central assumption used in analysis: €70/MWh wholesale (~€0.07/kWh)*

---

## EV Electricity Demand Parameters

| Parameter | Value | Basis |
|-----------|-------|-------|
| Average EV energy consumption | 20 kWh/100km | Industry WLTP average (incl. charging losses) |
| Annual km per EV | 12,000 km | Eurostat |
| Annual electricity per EV | 2,400 kWh/year | Derived |
| Domestic generation share | ~80% | IEA; accounts for cross-border imports |

---

## Additional EV Electricity Demand by Fleet Size

| BEV Fleet | Additional Demand (TWh) | % of EU Generation | Annual Cost (€70/MWh) |
|-----------|------------------------|--------------------|-----------------------|
| 6.8M (2025) | 16.3 TWh | 0.6% | ~€1.1B |
| 14.9M (2030 conservative) | 35.8 TWh | 1.3% | ~€2.5B |
| 18.1M (2030 base case) | 43.4 TWh | 1.6% | ~€3.0B |
| 22.2M (2030 accelerated) | 53.3 TWh | 1.9% | ~€3.7B |

---

## EV Grid Integration Notes

- **Smart charging potential:** ENTSO-E estimates that 80–90% of EV charging could be shifted to off-peak hours (22:00–06:00) by 2030 if smart charging mandates (EU AFIR regulation) are fully implemented.
- **Vehicle-to-Grid (V2G):** Pilot programmes underway in Netherlands, Germany, France. Not material at scale before 2030 but represents upside for grid flexibility.
- **Curtailment absorption:** 43 TWh of flexible EV demand could absorb a significant fraction of the ~30–50 TWh of wind/solar curtailment projected for 2030, improving renewable economics.
- **Grid reinforcement costs:** Estimated €10–20B in EU-wide distribution grid upgrades needed by 2030 to handle EV charging concentrations in residential areas (ENTSO-E TYNDP 2024).

---

## CO2 Impact of Grid Electrification

| Year | EU Grid Carbon Intensity | CO2 per EV per year (2,400 kWh) | CO2 avoided vs ICE (~2,100 kg/yr) |
|------|--------------------------|----------------------------------|-----------------------------------|
| 2025 | ~250 gCO2/kWh | ~600 kg CO2 | ~1,500 kg/yr |
| 2028 | ~210 gCO2/kWh | ~504 kg CO2 | ~1,596 kg/yr |
| 2030 | ~180 gCO2/kWh | ~432 kg CO2 | ~1,668 kg/yr |

*ICE reference: 7L/100km × 12,000km × ~2.5 kg CO2/L (well-to-wheel) = ~2,100 kg CO2/year*

---

## How to Verify

1. **ENTSO-E generation data:** https://transparency.entsoe.eu/ → Generation → Installed capacity / actual generation
2. **Eurostat electricity:** https://ec.europa.eu/eurostat/databrowser/product/view/NRG_CB_PEM
3. **Carbon intensity:** https://app.electricitymaps.com/zone/EU (real-time) or EEA grid intensity dataset
4. **EEX wholesale prices:** https://www.eex.com/en/market-data/power → Day-ahead auction
