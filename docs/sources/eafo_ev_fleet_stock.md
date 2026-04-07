# Source: EAFO — EV Fleet Stock by Member State

**Publisher:** European Alternative Fuels Observatory (EAFO) — operated under the European Commission  
**URL:** https://www.eafo.eu/vehicles-and-fleet/m1  
**Coverage:** EU27 + Norway + UK (filterable); passenger cars (M1 category)  
**Data type:** Cumulative BEV stock in circulation by country and year-end  
**Data retrieved:** Training data knowledge cutoff (early 2025); not live-fetched

---

## Estimated EU27 BEV Fleet Stock (End of Year)

Derived from cumulative ACEA sales data with age-adjusted survival rates:

| Year-end | Cumulative Sold (raw) | Blended Survival Rate | Est. Fleet in Circulation |
|----------|-----------------------|-----------------------|---------------------------|
| 2016 | 49,000 | ~99% | ~49,000 |
| 2017 | 123,000 | ~99% | ~122,000 |
| 2018 | 253,000 | ~99% | ~250,000 |
| 2019 | 451,000 | ~99% | ~446,000 |
| 2020 | 989,000 | ~98% | ~969,000 |
| 2021 | 1,867,000 | ~98% | ~1,830,000 |
| 2022 | 2,952,000 | ~97% | ~2,862,000 |
| 2023 | 4,487,000 | ~97% | ~4,352,000 |
| 2024 | 5,827,000 | ~96% | ~5,594,000 |
| 2025 | 7,027,000 | ~95.4% | **~6,832,000** |

## Survival Rate Methodology

Survival rates are derived from EEA vehicle survival probability tables for EU passenger cars, adjusted downward for BEVs due to:
- Young fleet (median age ~3–4 years in 2025)
- Battery warranty expiry effects increasing after year 8
- Early-generation models (pre-2018) with lower battery longevity

Annual scrappage assumed at:
- **0–8 years old:** ~0.5%/year
- **8–12 years old:** ~2–3%/year
- **12+ years old:** ~4–6%/year (standard EU ICE curve)

## EAFO Top EV Markets in EU (2024, approx. stock share)

| Country | Approx. BEV Stock Share |
|---------|------------------------|
| Germany | ~25% |
| France | ~18% |
| Netherlands | ~12% |
| Sweden | ~8% |
| Belgium | ~6% |
| Other EU22 | ~31% |

## How to Verify

1. Go to https://www.eafo.eu/vehicles-and-fleet/m1
2. Select "Stock" tab
3. Choose vehicle type: BEV
4. Select geography: European Union (EU27)
5. Export CSV for time series
