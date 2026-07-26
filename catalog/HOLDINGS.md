# ARK-CIVIC · Holdings

**Captured:** 2026-07-25T20:50:25Z
**Held in this repository:** 613 datasets · 827 files · 2,756,484 records · 455 MB
**Held in part:** 89 layers are shorter than the publisher's own row count and each says so
**Instance:** `midwest-lenexa`

Every file below is in `catalog/data/`, gzipped, pulled from the publisher's own
endpoint. Nothing here is fetched at page load. If every upstream endpoint were
withdrawn tomorrow, all of it would still be here.

Every count was read back off the stored file after trimming, not carried over
from the fetch. 89 layers are held in part rather than whole — an ArcGIS
service answers with one page at a time, and files over this repository's 4 MB
ceiling were cut. Each of those carries a `truncated` field in `pull_status.json`
stating both numbers. **A partial holding presented as a whole one is a quiet
falsehood, so none of them are counted as complete.**

| State | Datasets | Meaning |
|---|---:|---|
| **PULLED** | 613 | contents held in this repository |
| **SCHEMA** | 812 | endpoint reachable, structure and row count held, contents not mirrored |
| **WITHHELD** | 79 | reachable and deliberately not requested — person-level screen |
| **BLOCKED** | 251 | could not be pulled; every reason named in [`LOCK-INS.md`](LOCK-INS.md) |

**WITHHELD is a choice, not a failure.** Those 79 datasets were never
requested — not fetched and discarded. The canon forbids person-level data in this
repository and the screen runs before any content request is made.

## Held datasets by publisher

| Publishing authority | Datasets held | Records held |
|---|---:|---:|
| Kansas Data Access & Support Center | 250 | 1,880,580 |
| City of Kansas City, Missouri | 207 | 647,182 |
| Mid-America Regional Council | 99 | 143,054 |
| Johnson County AIMS | 33 | 70,087 |
| City of Lenexa, Kansas | 24 | 15,581 |

## Largest holdings

| Dataset | Publisher | Records | Endpoint |
|---|---|---:|---|
| Tiger 2020 Roads | Kansas Data Access & Support Cente | 236,256 | [`endpoint`](https://hub.kansasgis.org/api/download/v1/items/9f16300a3f254ceca7a5a93afc9d4848/csv?layers=0) |
| USNG 10000m | Kansas Data Access & Support Cente | 111,408 | [`endpoint`](https://hub.kansasgis.org/api/download/v1/items/c3fe0b263a5c4c5ebc3ef676ed811ad9/csv?layers=2) |
| National Wetland Inventory Polygons | Kansas Data Access & Support Cente | 100,119 | [`endpoint`](https://hub.kansasgis.org/api/download/v1/items/f26f882007ec478fba7df02e5a6cec06/csv?layers=0) |
| KDHE Environmental Interest Data | Kansas Data Access & Support Cente | 96,642 | [`endpoint`](https://hub.kansasgis.org/api/download/v1/items/f4b0c83c6a2f4ea6989e7d79ddb03889/csv?layers=0) |
| Tiger 2020 Blocks | Kansas Data Access & Support Cente | 95,139 | [`endpoint`](https://hub.kansasgis.org/api/download/v1/items/e9b7eebd6e304675b9ae217f72d3084a/csv?layers=0) |
| Playa Lakes Joint Venture - Probable Playas, v5 (11/5/2019) | Kansas Data Access & Support Cente | 71,848 | [`endpoint`](https://hub.kansasgis.org/api/download/v1/items/145f9876d9ac4760beb708ed17c72627/csv?layers=0) |
| KBS Potential Wetland Areas & Possible Playas - Western Kansas | Kansas Data Access & Support Cente | 60,496 | [`endpoint`](https://hub.kansasgis.org/api/download/v1/items/417e81f0dfca41bf86165bcf7aa46cb7/csv?layers=0) |
| KDHE Regulated Solid Waste Facilities Tonnage Table | Kansas Data Access & Support Cente | 56,563 | [`endpoint`](https://hub.kansasgis.org/api/download/v1/items/724affbd22ac4599b4b3f21ef56246c4/geojson?layers=5) |
| Major Floodplains of Eastern Kansas | Kansas Data Access & Support Cente | 54,500 | [`endpoint`](https://hub.kansasgis.org/api/download/v1/items/a19f8e59c50b47678c87adcda7a57676/csv?layers=0) |
| Southern & Central High Plains Aquifer Center Pivot Irrigation | Kansas Data Access & Support Cente | 50,116 | [`endpoint`](https://hub.kansasgis.org/api/download/v1/items/e553e7527603490aa49456d6e4ad788e/csv?layers=0) |
| National Wetland Inventory Lines | Kansas Data Access & Support Cente | 49,135 | [`endpoint`](https://hub.kansasgis.org/api/download/v1/items/72f1e8e3c6874da1919a27ca1fe30e46/csv?layers=0) |
| Catchments for KBS Potential Wetland Areas & Possible Playas - Western | Kansas Data Access & Support Cente | 48,338 | [`endpoint`](https://hub.kansasgis.org/api/download/v1/items/1c7e2bc4455548f08f09f591f8f44b87/csv?layers=0) |
| Kansas Irrigated Cropland c.2007 | Kansas Data Access & Support Cente | 44,063 | [`endpoint`](https://hub.kansasgis.org/api/download/v1/items/cb3ea07d8b0647008ce40a5158054288/csv?layers=0) |
| Kansas Stream Order 3-9 | Kansas Data Access & Support Cente | 42,972 | [`endpoint`](https://hub.kansasgis.org/api/download/v1/items/00683d63239e4237bfc1878ce97ec156/csv?layers=0) |
| USNG 100000m | Kansas Data Access & Support Cente | 40,935 | [`endpoint`](https://hub.kansasgis.org/api/download/v1/items/c3fe0b263a5c4c5ebc3ef676ed811ad9/csv?layers=1) |
| Melvern DTM 2ft contours LiDAR 2018 | Kansas Data Access & Support Cente | 40,566 | [`endpoint`](https://hub.kansasgis.org/api/download/v1/items/18ce2f5f0d0c4255b3540924899e1a23/csv?layers=1) |
| KDHE Regulated Storage Tank Details | Kansas Data Access & Support Cente | 37,356 | [`endpoint`](https://hub.kansasgis.org/api/download/v1/items/d4899a909a374c6cbb746eb83f95e23a/geojson?layers=1) |
| high plains aquifer bedrock wells | Kansas Data Access & Support Cente | 37,026 | [`endpoint`](https://hub.kansasgis.org/api/download/v1/items/c5972ca2f402437bb33f25221acd41f4/geojson?layers=2) |
| Partial Statewide Historical Geology Contacts | Kansas Data Access & Support Cente | 37,022 | [`endpoint`](https://hub.kansasgis.org/api/download/v1/items/17a6bdd3d1654ba5a85d41a4f3e6ce5e/csv?layers=1) |
| Cheney DTM 2ft contours LiDAR 2018 | Kansas Data Access & Support Cente | 36,180 | [`endpoint`](https://hub.kansasgis.org/api/download/v1/items/2c97a5ba0907416bb36bd1ec564f5afd/csv?layers=1) |
| High Plains Aquifer Section Properties | Kansas Data Access & Support Cente | 33,190 | [`endpoint`](https://hub.kansasgis.org/api/download/v1/items/223ec510fbb044e88b0d147196ae42a5/csv?layers=0) |
| KDHE Reported Spills | Kansas Data Access & Support Cente | 32,548 | [`endpoint`](https://hub.kansasgis.org/api/download/v1/items/32867c632bfe4a4c844aadfcf75f2f27/csv?layers=0) |
| Class II Wells | Kansas Data Access & Support Cente | 32,124 | [`endpoint`](https://hub.kansasgis.org/api/download/v1/items/a570398574804430ae92ae2b6a6b7df7/csv?layers=0) |
| USGS Geographic Names Information System | Kansas Data Access & Support Cente | 31,063 | [`endpoint`](https://hub.kansasgis.org/api/download/v1/items/034ea683a48a4f009fe61888b90253cc/geojson?layers=0) |
| Bridges | Mid-America Regional Council | 30,740 | [`endpoint`](https://opendata-marc-gis.hub.arcgis.com/api/download/v1/items/f285b2841fff4cf3a9c25174eb2d0bc9/csv?layers=0) |
| Clinton DTM 2ft contours LiDAR 2015 | Kansas Data Access & Support Cente | 30,648 | [`endpoint`](https://hub.kansasgis.org/api/download/v1/items/372162d9527f4da8a2ebc5e8d52bdf17/csv?layers=1) |
| Guardrails - Mobile LiDAR (2023) | Kansas Data Access & Support Cente | 30,358 | [`endpoint`](https://hub.kansasgis.org/api/download/v1/items/306ab8526db545f3873218a777569c4c/csv?layers=1) |
| FY 2023-2024 Line Item Budget - Expenditures | City of Kansas City, Missouri | 29,647 | [`endpoint`](https://data.kcmo.org/resource/ygzn-3xmu.json) |
| Business License Holder Map | City of Kansas City, Missouri | 28,245 | [`endpoint`](https://data.kcmo.org/resource/ja2w-8d3v.json) |
| businesses | City of Kansas City, Missouri | 28,245 | [`endpoint`](https://data.kcmo.org/resource/ezdv-33zs.json) |
| Business License Holders | City of Kansas City, Missouri | 28,245 | [`endpoint`](https://data.kcmo.org/resource/pnm4-68wg.json) |
| KCMO Business License Holders | City of Kansas City, Missouri | 28,245 | [`endpoint`](https://data.kcmo.org/resource/96my-yprt.json) |
| Out of State Business License Holders | City of Kansas City, Missouri | 28,245 | [`endpoint`](https://data.kcmo.org/resource/uwwp-6sdi.json) |
| Illegal Dumping and Trash in 311 Requests | City of Kansas City, Missouri | 27,914 | [`endpoint`](https://data.kcmo.org/resource/p227-55mh.json) |
| Open Illegal Dumping and Trash 311 Requests | City of Kansas City, Missouri | 27,914 | [`endpoint`](https://data.kcmo.org/resource/i4yb-fibq.json) |
| FY 2021-2022 Line Item Budget | City of Kansas City, Missouri | 27,095 | [`endpoint`](https://data.kcmo.org/resource/yv26-kkua.json) |
| Intersections - Mobile LiDAR (2023) | Kansas Data Access & Support Cente | 25,724 | [`endpoint`](https://services1.arcgis.com/q2CglofYX6ACNEeu/arcgis/rest/services/Intersections_2023/FeatureServer/1) |
| KCMO FY 2019-20 Adopted and Submitted Expenditures | City of Kansas City, Missouri | 24,385 | [`endpoint`](https://data.kcmo.org/resource/y2h3-scv9.json) |
| Non State Bridges | Kansas Data Access & Support Cente | 19,291 | [`endpoint`](https://hub.kansasgis.org/api/download/v1/items/9b5032d8d36e47079f24b748a3602d70/csv?layers=0) |
| Oil Production by Section | Kansas Data Access & Support Cente | 19,290 | [`endpoint`](https://services2.arcgis.com/ZOdjAzAQ2B0f85zi/arcgis/rest/services/Oil_Production_by_Section/FeatureServer/0) |

## Every held dataset (613)

| Dataset | Publisher | Records | Files |
|---|---|---:|---:|
| 2010 MARC Population and Employment Forecasts for Census Tracts | City of Kansas City, Missouri | 579 | 1 |
| 2012-2020 Submitted, Adopted, and Actuals with Codes- Rev | City of Kansas City, Missouri | 11,713 | 1 |
| 2013-2017 American Community Survey Detailed Census Tract Data | City of Kansas City, Missouri | 574 | 1 |
| 2014 Building Permit Listing | City of Kansas City, Missouri | 15,538 | 1 |
| 2015-2019 American Community Survey Basic Census Tract Data | City of Kansas City, Missouri | 574 | 1 |
| 2015-2019 American Community Survey Detailed Census Tract Data | City of Kansas City, Missouri | 574 | 1 |
| 2017 MARC Population 20-Year Forecasts | City of Kansas City, Missouri | 551 | 1 |
| 2017 MARC Population and Household 20-Year Forecasts for Census Tracts | City of Kansas City, Missouri | 551 | 1 |
| 2018 Kansas City Energy and Water Consumption Benchmarking for City-Owned Buil | City of Kansas City, Missouri | 153 | 1 |
| 2018 Kansas City Energy and Water Consumption Benchmarking for Community-Wide  | City of Kansas City, Missouri | 500 | 1 |
| 2019 Kansas City Energy and Water Consumption Benchmarking for City-Owned Buil | City of Kansas City, Missouri | 174 | 1 |
| 2019 Kansas City Energy and Water Consumption Benchmarking for Community-Wide  | City of Kansas City, Missouri | 595 | 1 |
| 2019 Pothole Requests from 311 | City of Kansas City, Missouri | 19,160 | 1 |
| 2020 Building Permit Listing | City of Kansas City, Missouri | 17,323 | 1 |
| 2020 MARC Population and Employment Forecasts for Census Tracts | City of Kansas City, Missouri | 551 | 1 |
| 2021 Kansas City Energy and Water Consumption Benchmarking for City-Owned Buil | City of Kansas City, Missouri | 141 | 1 |
| 2021 Kansas City Energy and Water Consumption Benchmarking for Community-Wide  | City of Kansas City, Missouri | 772 | 1 |
| 2022 Kansas City Energy and Water Consumption Benchmarking for City-Owned Buil | City of Kansas City, Missouri | 138 | 1 |
| 2022 Kansas City Energy and Water Consumption Benchmarking for Community-Wide  | City of Kansas City, Missouri | 1,465 | 1 |
| 2023 Kansas City Energy and Water Consumption Benchmarking for City Buildings | City of Kansas City, Missouri | 354 | 1 |
| 2023 Kansas City Energy and Water Consumption Benchmarking for Community Build | City of Kansas City, Missouri | 1,441 | 1 |
| 2024 MVA Update | City of Kansas City, Missouri | 498 | 1 |
| 311 Monthly Call Volume | City of Kansas City, Missouri | 112 | 1 |
| 311 Reported Issues - City Planning | City of Kansas City, Missouri | 7,721 | 1 |
| 311 Requests by Year | City of Kansas City, Missouri | 16 | 1 |
| 353 | City of Kansas City, Missouri | 80 | 1 |
| 353 | City of Kansas City, Missouri | 80 | 1 |
| AdvanceKC 2.0 | City of Kansas City, Missouri | 854 | 1 |
| AdvanceKC 2.0 Community Survey | City of Kansas City, Missouri | 854 | 1 |
| AED Registrations | City of Kansas City, Missouri | 1,348 | 1 |
| Animal Control Median Response Time | City of Kansas City, Missouri | 66 | 1 |
| Animal Services (Post-June 8, 2025) | City of Kansas City, Missouri | 15,255 | 1 |
| Area Plan Boundaries | City of Kansas City, Missouri | 18 | 1 |
| Area Plan Boundaries | City of Kansas City, Missouri | 18 | 1 |
| BCycle Stats | City of Kansas City, Missouri | 50 | 1 |
| Benchmarking building lookup list | City of Kansas City, Missouri | 1,796 | 1 |
| Budget by Appropriation Unit FY14-15 | City of Kansas City, Missouri | 6 | 1 |
| Building Codes Interpretations | City of Kansas City, Missouri | 360 | 1 |
| Business License Holder Map | City of Kansas City, Missouri | 28,245 | 1 |
| Business License Holders | City of Kansas City, Missouri | 28,245 | 1 |
| Business Satisfaction With Business Assistance Programs | City of Kansas City, Missouri | 6 | 1 |
| Business Satisfaction with Various City Services (FY2021) | City of Kansas City, Missouri | 7 | 1 |
| businesses | City of Kansas City, Missouri | 28,245 | 1 |
| Capital Improvements 1996 to 2019 | City of Kansas City, Missouri | 5,518 | 1 |
| Capital Improvements 1996 to 2020 | City of Kansas City, Missouri | 5,741 | 1 |
| Capital Improvements Sales Tax Expenditures FY 2008-2018 | City of Kansas City, Missouri | 5,328 | 1 |
| Causes Of Death In KCMO 2007-2012 By Year (Transposed) | City of Kansas City, Missouri | 8 | 1 |
| Citizen Communication Preferences | City of Kansas City, Missouri | 7 | 1 |
| Citizen Satisfaction with On-Street Bicycle Infrastructure | City of Kansas City, Missouri | 8 | 1 |
| City Contracts by Focus Area | City of Kansas City, Missouri | 5,848 | 1 |
| City Council Districts Shapefile - Effective 2023 | City of Kansas City, Missouri | 6 | 1 |
| City of KCMO Cultural Asset Inventory Phase 1 Physical Assets | City of Kansas City, Missouri | 230 | 1 |
| City of KCMO Cultural Asset Inventory Phase 1 Programs | City of Kansas City, Missouri | 209 | 1 |
| City of KCMO FY20 Submitted and Adopted Budget- Revenues | City of Kansas City, Missouri | 1,793 | 1 |
| City Owned Parcels | City of Kansas City, Missouri | 2,358 | 1 |
| City Owned Parcels | City of Kansas City, Missouri | 2,358 | 1 |
| City Planning and Development Department Analysis Implementation Status | City of Kansas City, Missouri | 325 | 1 |
| City Wide Water and Sewer Main Replacement | City of Kansas City, Missouri | 6 | 1 |
| City-Level Descriptive Statistics for GHG Inventory | City of Kansas City, Missouri | 80 | 1 |
| Community Greenhouse Gas Inventory Data | City of Kansas City, Missouri | 27 | 1 |
| Community Improvement District | City of Kansas City, Missouri | 73 | 1 |
| Community Improvement District | City of Kansas City, Missouri | 73 | 1 |
| Community Partner Gardens | City of Kansas City, Missouri | 343 | 1 |
| Commuting method | City of Kansas City, Missouri | 10 | 1 |
| Comparative for Illegal Dumping Story | City of Kansas City, Missouri | 2 | 1 |
| Count of LEED Certified Buildings In Kansas City by Certification Level, 2006- | City of Kansas City, Missouri | 5 | 1 |
| County Boundary | City of Kansas City, Missouri | 8 | 1 |
| County Boundary_data | City of Kansas City, Missouri | 8 | 1 |
| Dangerous Buildings Requests (historical) | City of Kansas City, Missouri | 7,703 | 1 |
| Demolished Dangerous Buildings | City of Kansas City, Missouri | 1,912 | 1 |
| Digital Navigator Events | City of Kansas City, Missouri | 181 | 1 |
| Digital Navigator Events - Age | City of Kansas City, Missouri | 181 | 1 |
| Digital Navigator Events - Demographic | City of Kansas City, Missouri | 181 | 1 |
| Digital Navigator Events - Districts | City of Kansas City, Missouri | 181 | 1 |
| Digital Navigator Events - Gender | City of Kansas City, Missouri | 181 | 1 |
| Digital Navigator Events - Laptops | City of Kansas City, Missouri | 181 | 1 |
| Digital Navigator Events - Participants | City of Kansas City, Missouri | 181 | 1 |
| Energy Star Certified Homes | City of Kansas City, Missouri | 271 | 1 |
| Energy Star Homes In Kansas City, Missouri | City of Kansas City, Missouri | 11 | 1 |
| Energy, Air & Climate Impacts of City-Owned Buildings in Kansas City, MO (2015 | City of Kansas City, Missouri | 141 | 1 |
| Energy, Air & Climate Impacts of City-Owned Buildings in Kansas City, MO (2016 | City of Kansas City, Missouri | 156 | 1 |
| Enterprise Zones | City of Kansas City, Missouri | 3 | 1 |
| Enterprise Zones | City of Kansas City, Missouri | 3 | 1 |
| Financial Trends Monitoring System Data | City of Kansas City, Missouri | 15 | 1 |
| Fire Stations | City of Kansas City, Missouri | 34 | 1 |
| Fire Stations | City of Kansas City, Missouri | 34 | 1 |
| Flood Alarm Locations | City of Kansas City, Missouri | 44 | 1 |
| Food Insecurity | City of Kansas City, Missouri | 3 | 1 |
| FY 2015 to 2020 Customer Survey Data | City of Kansas City, Missouri | 12,893 | 1 |
| FY 2017-18 Line Item Budget | City of Kansas City, Missouri | 12,261 | 1 |
| FY 2021-2022 Line Item Budget | City of Kansas City, Missouri | 27,095 | 1 |
| FY 2023-2024 Line Item Budget - Expenditures | City of Kansas City, Missouri | 29,647 | 1 |
| FY 2023-2024 Line Item Budget - Revenue | City of Kansas City, Missouri | 2,401 | 1 |
| GO KC Capital Project | City of Kansas City, Missouri | 27 | 1 |
| Government Operations GHG Inventory Data | City of Kansas City, Missouri | 33 | 1 |
| Government Operations Statistics for GHG Inventory | City of Kansas City, Missouri | 141 | 1 |
| Graffiti Requests to 311 (historical) | City of Kansas City, Missouri | 3,761 | 1 |
| Greenhouse Gas Emissions Communitywide | City of Kansas City, Missouri | 3 | 1 |
| Greenhouse Gas Emissions from Government Operations | City of Kansas City, Missouri | 3 | 1 |
| Homeless Encampment 311 Reports pre-March, 2021. | City of Kansas City, Missouri | 57 | 1 |
| Homeless/Houseless Issues Reported in myKCMO | City of Kansas City, Missouri | 7,395 | 1 |
| Illegal Dumping and Trash in 311 Requests | City of Kansas City, Missouri | 27,914 | 1 |
| Illegal Dumping Statistics | City of Kansas City, Missouri | 100 | 1 |
| Illegal Dumping Story Summary | City of Kansas City, Missouri | 4 | 1 |
| June 2017 Storm Damage to Trees | City of Kansas City, Missouri | 859 | 1 |
| Kansas City Missouri Parks and Boulevards Map | City of Kansas City, Missouri | 468 | 1 |
| Kansas City Monthly Car Auction | City of Kansas City, Missouri | 162 | 1 |
| Kansas City Neighborhood Borders | City of Kansas City, Missouri | 246 | 1 |
| Kansas City Neighborhood Boundaries | City of Kansas City, Missouri | 246 | 1 |
| KC Composting Locations | City of Kansas City, Missouri | 14 | 1 |
| KC Green Sustainable Projects | City of Kansas City, Missouri | 185 | 1 |
| KC Register of Historic Places | City of Kansas City, Missouri | 106 | 1 |
| KC Register of Historic Places | City of Kansas City, Missouri | 106 | 1 |
| KCATA Bus Stops | City of Kansas City, Missouri | 2,467 | 1 |
| KCATA Bus Stops - Deprecated | City of Kansas City, Missouri | 3,566 | 1 |
| KCATA Bus Stops Map | City of Kansas City, Missouri | 2,467 | 1 |
| KCMO Business License Holders | City of Kansas City, Missouri | 28,245 | 1 |
| KCMO Business License Holders | City of Kansas City, Missouri | 15,895 | 1 |
| KCMO Food Permits | City of Kansas City, Missouri | 3,681 | 1 |
| KCMO FY 2012-2020 Submitted, Adopted, and Actual Budget- Revenue | City of Kansas City, Missouri | 11,709 | 1 |
| KCMO FY 2012-2022 Submitted Adopted Actual Line Item Budget Submitted Rev | City of Kansas City, Missouri | 15,543 | 1 |
| KCMO FY 2019-20 Adopted and Submitted Expenditures | City of Kansas City, Missouri | 24,385 | 1 |
| KCMO FY 2019-20 Adopted and Submitted Revenues | City of Kansas City, Missouri | 1,793 | 1 |
| KCMO Warning Siren Addresses | City of Kansas City, Missouri | 126 | 1 |
| Land Bank and Homesteading Authority Data | City of Kansas City, Missouri | 6,587 | 1 |
| Land Bank and Kansas City Missouri Homesteading Authority Data | City of Kansas City, Missouri | 6,356 | 1 |
| Land Bank Owned Properties by Neighborhood | City of Kansas City, Missouri | 6,356 | 1 |
| Land Bank Properties by Class | City of Kansas City, Missouri | 6,587 | 1 |
| Land Bank Properties by Council District | City of Kansas City, Missouri | 6,587 | 1 |
| Land Bank Properties by Neighborhood | City of Kansas City, Missouri | 6,587 | 1 |
| Land Bank Properties by Property Type | City of Kansas City, Missouri | 6,587 | 1 |
| Land Use Codes | City of Kansas City, Missouri | 73 | 1 |
| layer_0 | City of Kansas City, Missouri | 468 | 1 |
| LEED Certified Buildings in Kansas City | City of Kansas City, Missouri | 103 | 1 |
| List of KCMO City Contracts | City of Kansas City, Missouri | 5,848 | 1 |
| Litter Index | City of Kansas City, Missouri | 9 | 1 |
| LLC Affidavits | City of Kansas City, Missouri | 1,733 | 1 |
| Location of Dialysis facilities Registered with Medicare | City of Kansas City, Missouri | 14 | 1 |
| Map of City Council Districts | City of Kansas City, Missouri | 6 | 1 |
| Map of Council Districts (2014-2023) | City of Kansas City, Missouri | 6 | 1 |
| Map of Current Land Bank / Homesteading Authority Properties | City of Kansas City, Missouri | 6,356 | 1 |
| Map of Land Bank Properties | City of Kansas City, Missouri | 6,587 | 1 |
| Map of TIF (Tax Increment Financing) Districts | City of Kansas City, Missouri | 71 | 1 |
| Market Value Analysis (MVA) 2020 | City of Kansas City, Missouri | 440 | 1 |
| Market Value Analysis (MVA) 2020 | City of Kansas City, Missouri | 440 | 1 |
| Monthly Call Volume | City of Kansas City, Missouri | 112 | 1 |
| National Register of Historic Places | City of Kansas City, Missouri | 313 | 1 |
| National Register of Historic Places | City of Kansas City, Missouri | 313 | 1 |
| Neighborhood Cleanups | City of Kansas City, Missouri | 16 | 1 |
| Neighborhood Improvement District | City of Kansas City, Missouri | 7 | 1 |
| Neighborhood Improvement District | City of Kansas City, Missouri | 7 | 1 |
| Neighborhood Tourist Development Fund Applications, 2021 | City of Kansas City, Missouri | 147 | 1 |
| Neighborhoods Census | City of Kansas City, Missouri | 246 | 1 |
| Neighborhoods Census | City of Kansas City, Missouri | 246 | 1 |
| Neighborhoods FOCUS | City of Kansas City, Missouri | 246 | 1 |
| Neighborhoods FOCUS | City of Kansas City, Missouri | 246 | 1 |
| Non-DV Aggravated Assaults Involving Firearms | City of Kansas City, Missouri | 3,444 | 1 |
| Non-Fatal Assault Map (2023) | City of Kansas City, Missouri | 3,444 | 1 |
| Non-Fatal Assault Timeline (2023) | City of Kansas City, Missouri | 3,444 | 1 |
| NPD Boardup Reports | City of Kansas City, Missouri | 5,289 | 1 |
| Number of LEED Certified Buildings In Kansas City by Rating System | City of Kansas City, Missouri | 5 | 1 |
| OCP I& I Goals Versus Actual | City of Kansas City, Missouri | 12 | 1 |
| Off Street Parking | City of Kansas City, Missouri | 148 | 1 |
| Off Street Parking | City of Kansas City, Missouri | 148 | 1 |
| Older Council Districts (2014-2023) | City of Kansas City, Missouri | 6 | 1 |
| Open Data KC Google Analytics Data | City of Kansas City, Missouri | 37 | 1 |
| Open Illegal Dumping and Trash 311 Requests | City of Kansas City, Missouri | 27,914 | 1 |
| Open violations - exterior building issues | City of Kansas City, Missouri | 5,945 | 1 |
| Out of State Business License Holders | City of Kansas City, Missouri | 28,245 | 1 |
| Outdoor Advertising Signs | City of Kansas City, Missouri | 593 | 1 |
| Outdoor Advertising Signs | City of Kansas City, Missouri | 593 | 1 |
| PIEA | City of Kansas City, Missouri | 86 | 1 |
| PIEA | City of Kansas City, Missouri | 86 | 1 |
| Plumbers | City of Kansas City, Missouri | 518 | 1 |
| Police Divisions | City of Kansas City, Missouri | 6 | 1 |
| Police Divisions | City of Kansas City, Missouri | 6 | 1 |
| Population by Neighborhood | City of Kansas City, Missouri | 240 | 1 |
| Public Works Maintenance Districts | City of Kansas City, Missouri | 3 | 1 |
| Rainfall Depth Table Kansas City Area | City of Kansas City, Missouri | 116 | 1 |
| Rebuild KC Grant Applications - Second Round | City of Kansas City, Missouri | 259 | 1 |
| ReBuildKC Applications | City of Kansas City, Missouri | 1,216 | 1 |
| Registered Neighborhood/Homes Associations_data | City of Kansas City, Missouri | 260 | 1 |
| School Districts | City of Kansas City, Missouri | 105 | 1 |
| School Districts | City of Kansas City, Missouri | 105 | 1 |
| Short-Term Rental 311 Complaints | City of Kansas City, Missouri | 1,530 | 1 |
| Snow and Ice Treatment Needed Jan 2024 | City of Kansas City, Missouri | 793 | 1 |
| Snow and Ice Treatment Needed Jan 2025 | City of Kansas City, Missouri | 7,724 | 1 |
| Solar Electricity Supply for Energy Demand in City-Owned Buildings | City of Kansas City, Missouri | 2 | 1 |
| Street Condition Ratings (PCI) | City of Kansas City, Missouri | 1 | 1 |
| Street Resurfacing | City of Kansas City, Missouri | 1,570 | 1 |
| Street Resurfacing_data | City of Kansas City, Missouri | 1,570 | 1 |
| Summary Of Goals And Objectives 2015-2020 | City of Kansas City, Missouri | 62 | 1 |
| Sustainability Dashboard | City of Kansas City, Missouri | 124 | 1 |
| Sustainable Projects Map 2021 | City of Kansas City, Missouri | 185 | 1 |
| TIF (Tax Increment Financing) Districts | City of Kansas City, Missouri | 71 | 1 |
| Total Trash And Recycling Collected | City of Kansas City, Missouri | 13 | 1 |
| Tree Removal via 311 | City of Kansas City, Missouri | 10,209 | 1 |
| Tree Violations in EnerGov | City of Kansas City, Missouri | 213 | 1 |
| Tree Violations in EnerGov | City of Kansas City, Missouri | 213 | 1 |
| Trees Trimmed And Removed Annually | City of Kansas City, Missouri | 16 | 1 |
| Urban Renewal | City of Kansas City, Missouri | 134 | 1 |
| Urban Renewal | City of Kansas City, Missouri | 134 | 1 |
| Volunteers in Kansas City Metrowide | City of Kansas City, Missouri | 33 | 1 |
| Zip Codes | City of Kansas City, Missouri | 50 | 1 |
| Zip Codes | City of Kansas City, Missouri | 50 | 1 |
| Zoning | City of Kansas City, Missouri | 2,619 | 1 |
| Zoning | City of Kansas City, Missouri | 2,619 | 1 |
| Annexation | City of Lenexa, Kansas | 252 | 1 |
| Comprehensive Plan - Future Land Use | City of Lenexa, Kansas | 1,236 | 2 |
| Comprehensive Plan - Neighborhood Nodes | City of Lenexa, Kansas | 21 | 1 |
| Comprehensive Plan - Transportation and Mobility Network | City of Lenexa, Kansas | 292 | 3 |
| Government - Points of Interest | City of Lenexa, Kansas | 77 | 14 |
| GovernmentServices | City of Lenexa, Kansas | 77 | 14 |
| JoCo_Waterbody | City of Lenexa, Kansas | 419 | 1 |
| JoCo_WaterCourse | City of Lenexa, Kansas | 2,000 | 1 |
| Johnson County Basemap | City of Lenexa, Kansas | 129 | 1 |
| Lenexa City Limits | City of Lenexa, Kansas | 1 | 1 |
| Lenexa City Limits - masked | City of Lenexa, Kansas | 24 | 3 |
| LenexaCityLimits | City of Lenexa, Kansas | 1 | 1 |
| MS Streets Concrete Locations webmap | City of Lenexa, Kansas | 17 | 1 |
| Parcels_ | City of Lenexa, Kansas | 2,000 | 1 |
| Park Planning | City of Lenexa, Kansas | 661 | 4 |
| Parks & Recreation - Trail Network | City of Lenexa, Kansas | 56 | 1 |
| Pavement | City of Lenexa, Kansas | 2,922 | 3 |
| PLSS QQ | City of Lenexa, Kansas | 873 | 1 |
| Road Lane Closure | City of Lenexa, Kansas | 6 | 3 |
| Road Lane Closure | City of Lenexa, Kansas | 6 | 3 |
| Road_Closures | City of Lenexa, Kansas | 6 | 3 |
| Roads | City of Lenexa, Kansas | 2,000 | 1 |
| Zoning District - Group Layer | City of Lenexa, Kansas | 1,258 | 2 |
| Zoning Districts - mapserver | City of Lenexa, Kansas | 1,247 | 1 |
| A I R  P L N  Areas | Johnson County AIMS | 48 | 2 |
| Annexation | Johnson County AIMS | 504 | 3 |
| Annexation | Johnson County AIMS | 504 | 3 |
| Base Map  State Plane | Johnson County AIMS | 129 | 1 |
| Base Map I M S | Johnson County AIMS | 129 | 1 |
| Bike Joco | Johnson County AIMS | 47 | 3 |
| Client Centers  P L | Johnson County AIMS | 8 | 1 |
| Client Centers  P L | Johnson County AIMS | 8 | 1 |
| Community Mental Health Centersof K S | Johnson County AIMS | 157 | 3 |
| County Boundary | Johnson County AIMS | 4,376 | 23 |
| Damage Assessment Viewer | Johnson County AIMS | 481 | 3 |
| Districts | Johnson County AIMS | 1,729 | 7 |
| Emergency Management | Johnson County AIMS | 5,363 | 22 |
| Energov | Johnson County AIMS | 8,002 | 4 |
| Free Data2 | Johnson County AIMS | 1,499 | 16 |
| Import Plat | Johnson County AIMS | 1 | 1 |
| Incode | Johnson County AIMS | 953 | 1 |
| J C W  G B A | Johnson County AIMS | 1,448 | 3 |
| J C W  G B A | Johnson County AIMS | 1,448 | 3 |
| J C W  Locates | Johnson County AIMS | 2,000 | 1 |
| J C W  Locates | Johnson County AIMS | 2,000 | 1 |
| K C Metro  Utility Coord | Johnson County AIMS | 127 | 1 |
| K C Metro  Utility Coord | Johnson County AIMS | 127 | 1 |
| Landmarks | Johnson County AIMS | 2,958 | 31 |
| Mission  Permitting | Johnson County AIMS | 6,000 | 3 |
| Mission  Permitting | Johnson County AIMS | 6,000 | 3 |
| Open Gov | Johnson County AIMS | 2,062 | 7 |
| P W Rowdocs | Johnson County AIMS | 1,505 | 2 |
| Parcels | Johnson County AIMS | 2,000 | 1 |
| Poverty | Johnson County AIMS | 1,136 | 9 |
| Test E S Z | Johnson County AIMS | 1 | 1 |
| The J O | Johnson County AIMS | 2,249 | 6 |
| Watershed Master Plans | Johnson County AIMS | 15,088 | 36 |
| 10 feet to 20 feet Structures | Kansas Data Access & Support Cen | 2,938 | 1 |
| 2012 Higher Education Facilities | Kansas Data Access & Support Cen | 138 | 1 |
| 2021 Kansas Census Cities (Incorporated Areas) | Kansas Data Access & Support Cen | 740 | 1 |
| 2024 Tax Units | Kansas Data Access & Support Cen | 4,270 | 1 |
| 2025 Pond Sites | Kansas Data Access & Support Cen | 16 | 1 |
| 2025 Tax Units | Kansas Data Access & Support Cen | 4,194 | 1 |
| 2026 Tax Units | Kansas Data Access & Support Cen | 4,230 | 1 |
| 303d Lake - Approved | Kansas Data Access & Support Cen | 111 | 1 |
| 303d Stream - Approved | Kansas Data Access & Support Cen | 1,050 | 1 |
| AADT Flow Map | Kansas Data Access & Support Cen | 5,064 | 1 |
| AADT NonState | Kansas Data Access & Support Cen | 9,082 | 1 |
| Abandoned Railroad | Kansas Data Access & Support Cen | 297 | 1 |
| Active Railroads | Kansas Data Access & Support Cen | 352 | 1 |
| Active Railroads | Kansas Data Access & Support Cen | 352 | 1 |
| Alluvial Aquifer Extent | Kansas Data Access & Support Cen | 1 | 1 |
| Alluvial Aquifer Extent | Kansas Data Access & Support Cen | 366 | 1 |
| Alternative Fuel Stations | Kansas Data Access & Support Cen | 71 | 1 |
| Billboard Faces - Mobile LiDAR (2023) | Kansas Data Access & Support Cen | 2,458 | 1 |
| Catchments | Kansas Data Access & Support Cen | 1,147 | 1 |
| Catchments (2025) | Kansas Data Access & Support Cen | 1,341 | 1 |
| Catchments for KBS Potential Wetland Areas & Possible Playas - Western Kansas | Kansas Data Access & Support Cen | 48,338 | 1 |
| Catchments for PLJV Probable Playas (v5) - Kansas | Kansas Data Access & Support Cen | 1,457 | 1 |
| Certified Electric Areas | Kansas Data Access & Support Cen | 522 | 1 |
| Certified Gas Areas | Kansas Data Access & Support Cen | 405 | 1 |
| Cheney conservation pool LiDAR 2018 | Kansas Data Access & Support Cen | 1 | 1 |
| Cheney DTM 2ft contours LiDAR 2018 | Kansas Data Access & Support Cen | 36,180 | 1 |
| Cheney flood pool LiDAR 2018 | Kansas Data Access & Support Cen | 1 | 1 |
| Cheney Lake contours LiDAR 2018 | Kansas Data Access & Support Cen | 1,517 | 1 |
| Cheney Lake extent | Kansas Data Access & Support Cen | 1 | 1 |
| City Boundaries | Kansas Data Access & Support Cen | 863 | 1 |
| Class II Wells | Kansas Data Access & Support Cen | 32,124 | 1 |
| Clinton DTM 2ft contours LiDAR 2015 | Kansas Data Access & Support Cen | 30,648 | 1 |
| Clinton flood pool LiDAR 2021 | Kansas Data Access & Support Cen | 1 | 1 |
| Clinton Lake contours LiDAR 2021 | Kansas Data Access & Support Cen | 13,240 | 1 |
| Clinton Lake extent on July 12, 2023 | Kansas Data Access & Support Cen | 1 | 1 |
| Commerce Community Development Regions | Kansas Data Access & Support Cen | 6 | 1 |
| Community Corrections | Kansas Data Access & Support Cen | 31 | 1 |
| Congressional Districts | Kansas Data Access & Support Cen | 4 | 1 |
| Dakota Aquifer Base | Kansas Data Access & Support Cen | 72 | 1 |
| Dakota Aquifer Extent | Kansas Data Access & Support Cen | 1 | 1 |
| Dakota Aquifer Extent | Kansas Data Access & Support Cen | 30 | 1 |
| Dakota Aquifer Top | Kansas Data Access & Support Cen | 151 | 1 |
| Delaware River Watershed Boundary buffered 200m | Kansas Data Access & Support Cen | 1 | 1 |
| Department of Children and Families | Kansas Data Access & Support Cen | 4 | 1 |
| Detention (2025) | Kansas Data Access & Support Cen | 1,340 | 1 |
| Detention (2025; 16 sites) | Kansas Data Access & Support Cen | 16 | 1 |
| Detention (2025; original sites) | Kansas Data Access & Support Cen | 96 | 1 |
| Earthquakes | Kansas Data Access & Support Cen | 5,046 | 1 |
| El Dorado conservation pool LiDAR 2018 | Kansas Data Access & Support Cen | 1 | 1 |
| El Dorado DTM 2ft contours LiDAR 2018 | Kansas Data Access & Support Cen | 1,426 | 1 |
| El Dorado Lake contours LiDAR 2018 | Kansas Data Access & Support Cen | 5,739 | 1 |
| El Dorado Lake extent | Kansas Data Access & Support Cen | 1 | 1 |
| El Dorado Lake extent on August 1, 2023 | Kansas Data Access & Support Cen | 1 | 1 |
| Fire Marshal Prevention Districts | Kansas Data Access & Support Cen | 11 | 1 |
| Flint Hills Aquifer Extent | Kansas Data Access & Support Cen | 1 | 1 |
| Floodplains of Chase County, Kansas | Kansas Data Access & Support Cen | 1 | 1 |
| Gas Production by Section | Kansas Data Access & Support Cen | 12,710 | 1 |
| Glacial Drift Aquifer Base | Kansas Data Access & Support Cen | 9,942 | 1 |
| Glacial Drift Aquifer Extent | Kansas Data Access & Support Cen | 1 | 1 |
| Glacial Drift Aquifer Extent | Kansas Data Access & Support Cen | 272 | 1 |
| Groundwater Management Districts (GMD) | Kansas Data Access & Support Cen | 5 | 1 |
| Guardrails - Mobile LiDAR (2023) | Kansas Data Access & Support Cen | 30,358 | 1 |
| gWCI | Kansas Data Access & Support Cen | 1,341 | 1 |
| high plains aquifer base | Kansas Data Access & Support Cen | 1,902 | 1 |
| high plains aquifer bedrock wells | Kansas Data Access & Support Cen | 37,026 | 1 |
| High Plains Aquifer Extent | Kansas Data Access & Support Cen | 1 | 1 |
| high plains aquifer extent | Kansas Data Access & Support Cen | 88 | 1 |
| High Plains Aquifer Section Properties | Kansas Data Access & Support Cen | 33,190 | 1 |
| Hillsdale conservation pool LiDAR 2018 | Kansas Data Access & Support Cen | 1 | 1 |
| Hillsdale flood pool LiDAR 2018 | Kansas Data Access & Support Cen | 1 | 1 |
| Hillsdale Lake contours LiDAR 2018 | Kansas Data Access & Support Cen | 1,537 | 1 |
| Hillsdale Lake extent | Kansas Data Access & Support Cen | 1 | 1 |
| Hillsdale Lake extent on September 6, 2023 | Kansas Data Access & Support Cen | 1 | 1 |
| Homeland Security Regions | Kansas Data Access & Support Cen | 7 | 1 |
| HUC 10 Boundaries | Kansas Data Access & Support Cen | 367 | 1 |
| HUC 12 Boundaries | Kansas Data Access & Support Cen | 2,055 | 1 |
| HUC 8 Boundaries | Kansas Data Access & Support Cen | 90 | 1 |
| Incorporated Areas | Kansas Data Access & Support Cen | 28 | 1 |
| Inorganic Organic | Kansas Data Access & Support Cen | 2,404 | 1 |
| Intersections - Mobile LiDAR (2023) | Kansas Data Access & Support Cen | 25,724 | 1 |
| Judicial Districts | Kansas Data Access & Support Cen | 31 | 1 |
| K-12 Schools | Kansas Data Access & Support Cen | 1,854 | 1 |
| Kansas Arboretums | Kansas Data Access & Support Cen | 31 | 1 |
| Kansas Black Walnut Hulling Stations | Kansas Data Access & Support Cen | 9 | 1 |
| Kansas Cell Towers | Kansas Data Access & Support Cen | 2,851 | 1 |
| Kansas Deer Management Units | Kansas Data Access & Support Cen | 18 | 1 |
| Kansas Department of Transportation Districts | Kansas Data Access & Support Cen | 6 | 1 |
| Kansas Fire Districts | Kansas Data Access & Support Cen | 659 | 1 |
| Kansas Fire Stations | Kansas Data Access & Support Cen | 1,013 | 1 |
| Kansas Highway Patrol Troop Areas | Kansas Data Access & Support Cen | 7 | 1 |
| Kansas Identified Sites List (ISL) (KDHE) | Kansas Data Access & Support Cen | 3,834 | 1 |
| Kansas Irrigated Cropland c.2007 | Kansas Data Access & Support Cen | 44,063 | 1 |
| Kansas Reservoir Protection Initiative (KRPI) Priority Areas | Kansas Data Access & Support Cen | 10 | 1 |
| Kansas River Centerline | Kansas Data Access & Support Cen | 1 | 1 |
| Kansas River Mile Points | Kansas Data Access & Support Cen | 1,696 | 1 |
| Kansas Sawmills | Kansas Data Access & Support Cen | 56 | 1 |
| Kansas Stream Order 3-9 | Kansas Data Access & Support Cen | 42,972 | 1 |
| Kansas Timber Buyers | Kansas Data Access & Support Cen | 61 | 1 |
| Kansas Tree Campuses | Kansas Data Access & Support Cen | 8 | 1 |
| Kansas Tree Cities | Kansas Data Access & Support Cen | 87 | 1 |
| Kansas Waterfowl Hunting Zones | Kansas Data Access & Support Cen | 4 | 1 |
| Kansas Wildland Fire Perimeters | Kansas Data Access & Support Cen | 250 | 1 |
| KansasLunettes | Kansas Data Access & Support Cen | 175 | 1 |
| KBS LiDAR-based Playa Mapping Study Area | Kansas Data Access & Support Cen | 1 | 1 |
| KBS Potential Wetland Areas & Possible Playas - Western Kansas | Kansas Data Access & Support Cen | 60,496 | 1 |
| KDHE Administrative Boundaries | Kansas Data Access & Support Cen | 6 | 1 |
| KDHE Closed City Dumps | Kansas Data Access & Support Cen | 775 | 1 |
| KDHE Environmental Interest Data | Kansas Data Access & Support Cen | 96,642 | 1 |
| KDHE Environmental Use Control (EUC) Sites | Kansas Data Access & Support Cen | 387 | 1 |
| KDHE Regulated Solid Waste Facilities | Kansas Data Access & Support Cen | 1,057 | 1 |
| KDHE Regulated Solid Waste Facilities Tonnage Table | Kansas Data Access & Support Cen | 56,563 | 1 |
| KDHE Regulated Storage Tank | Kansas Data Access & Support Cen | 17,518 | 1 |
| KDHE Regulated Storage Tank Details | Kansas Data Access & Support Cen | 37,356 | 1 |
| KDHE Regulated Storage Tanks - Leaking Underground (LUST) | Kansas Data Access & Support Cen | 11,943 | 1 |
| KDHE Reported Spills | Kansas Data Access & Support Cen | 32,548 | 1 |
| KDHE Surface Water Register - Lakes | Kansas Data Access & Support Cen | 358 | 1 |
| KDHE Surface Water Register - Streams | Kansas Data Access & Support Cen | 2,049 | 1 |
| KDHE TMDL Lake | Kansas Data Access & Support Cen | 168 | 1 |
| KDHE TMDL Stream | Kansas Data Access & Support Cen | 1,339 | 1 |
| KDOT reference post markers | Kansas Data Access & Support Cen | 11,444 | 1 |
| KSU Extension Office Regions | Kansas Data Access & Support Cen | 5 | 1 |
| Lane Counts - Mobile LiDAR (2023) | Kansas Data Access & Support Cen | 12,409 | 1 |
| Lottery Regions | Kansas Data Access & Support Cen | 6 | 1 |
| Major Floodplains of Eastern Kansas | Kansas Data Access & Support Cen | 54,500 | 1 |
| Marion conservation pool LiDAR 2018 | Kansas Data Access & Support Cen | 1 | 1 |
| Marion DTM 2ft contours LiDAR 2018 | Kansas Data Access & Support Cen | 1,360 | 1 |
| Marion flood pool LiDAR 2018 | Kansas Data Access & Support Cen | 1 | 1 |
| Marion Lake contours LiDAR 2018 | Kansas Data Access & Support Cen | 1,548 | 1 |
| Marion Lake extent | Kansas Data Access & Support Cen | 1 | 1 |
| Marion Reservoir extent on August 28, 2023 | Kansas Data Access & Support Cen | 1 | 1 |
| Medians - Mobile LiDAR (2023) | Kansas Data Access & Support Cen | 5,039 | 1 |
| Melvern conservation pool LiDAR 2018 | Kansas Data Access & Support Cen | 1 | 1 |
| Melvern DTM 2ft contours LiDAR 2018 | Kansas Data Access & Support Cen | 40,566 | 1 |
| Melvern flood pool LiDAR 2018 | Kansas Data Access & Support Cen | 1 | 1 |
| Melvern Lake contours LiDAR 2018 | Kansas Data Access & Support Cen | 1,442 | 1 |
| Melvern Lake extent | Kansas Data Access & Support Cen | 1 | 1 |
| Melvern Lake extent on August 29, 2023 | Kansas Data Access & Support Cen | 1 | 1 |
| Metadata | Kansas Data Access & Support Cen | 1 | 1 |
| Milford conservation pool LiDAR 2017 18 | Kansas Data Access & Support Cen | 1 | 1 |
| Milford flood pool LiDAR 2017 18 | Kansas Data Access & Support Cen | 1 | 1 |
| Milford Lake extent | Kansas Data Access & Support Cen | 1 | 1 |
| Milford Lake extent on August 15, 2023 | Kansas Data Access & Support Cen | 1 | 1 |
| National Inventory of Dams | Kansas Data Access & Support Cen | 6,491 | 1 |
| National Prescribed Burn Associations | Kansas Data Access & Support Cen | 184 | 1 |
| National Wetland Inventory Lines | Kansas Data Access & Support Cen | 49,135 | 1 |
| National Wetland Inventory Polygons | Kansas Data Access & Support Cen | 100,119 | 1 |
| Noise Walls - Mobile LiDAR (2023) | Kansas Data Access & Support Cen | 55 | 1 |
| Non State Bridges | Kansas Data Access & Support Cen | 19,291 | 1 |
| Office of Veterans Service Areas | Kansas Data Access & Support Cen | 16 | 1 |
| Oil and Gas Fields | Kansas Data Access & Support Cen | 2,830 | 1 |
| Oil Production by Section | Kansas Data Access & Support Cen | 19,290 | 1 |
| Osage Aquifer Extent | Kansas Data Access & Support Cen | 1 | 1 |
| Ozark Aquifer Base | Kansas Data Access & Support Cen | 129 | 1 |
| Ozark Aquifer Extent | Kansas Data Access & Support Cen | 2 | 1 |
| Ozark Aquifer Extent | Kansas Data Access & Support Cen | 1 | 1 |
| Ozark Aquifer Top | Kansas Data Access & Support Cen | 135 | 1 |
| Parole Regions | Kansas Data Access & Support Cen | 2 | 1 |
| Partial Statewide Historical Geology Beds | Kansas Data Access & Support Cen | 744 | 1 |
| Partial Statewide Historical Geology Contacts | Kansas Data Access & Support Cen | 37,022 | 1 |
| Partial Statewide Historical Geology Faults | Kansas Data Access & Support Cen | 135 | 1 |
| Partial Statewide Historical Geology Intermittent Ponds | Kansas Data Access & Support Cen | 430 | 1 |
| Partial Statewide Historical Geology Points | Kansas Data Access & Support Cen | 12 | 1 |
| Partial Statewide Historical Geology Polygons | Kansas Data Access & Support Cen | 12,027 | 1 |
| Perry conservation pool LiDAR 2015 18 | Kansas Data Access & Support Cen | 1 | 1 |
| Perry flood pool LiDAR 2015 18 | Kansas Data Access & Support Cen | 1 | 1 |
| Perry Lake contours LiDAR 2015 18 | Kansas Data Access & Support Cen | 1,235 | 1 |
| Perry Lake extent | Kansas Data Access & Support Cen | 1 | 1 |
| Perry Lake extent on August 3, 2023 | Kansas Data Access & Support Cen | 1 | 1 |
| Physiographic Regions | Kansas Data Access & Support Cen | 11 | 1 |
| Pioneer Cemeteries | Kansas Data Access & Support Cen | 927 | 1 |
| Playa Lakes Joint Venture - Probable Playas, v5 (11/5/2019) | Kansas Data Access & Support Cen | 71,848 | 1 |
| playas Ver1-3 | Kansas Data Access & Support Cen | 10,540 | 1 |
| PLSS- Township Range | Kansas Data Access & Support Cen | 2,343 | 1 |
| Ponds | Kansas Data Access & Support Cen | 1,136 | 1 |
| Protected Areas Database | Kansas Data Access & Support Cen | 3,127 | 1 |
| Public Wholesale Water Supply Districts (PWWSD) | Kansas Data Access & Support Cen | 19 | 1 |
| Quarries and Mines | Kansas Data Access & Support Cen | 8,807 | 1 |
| Radiological | Kansas Data Access & Support Cen | 104 | 1 |
| Railroad Crossings - Mobile LiDAR (2023) | Kansas Data Access & Support Cen | 1,251 | 1 |
| Regional Planning Areas | Kansas Data Access & Support Cen | 14 | 1 |
| Reported Wildfires | Kansas Data Access & Support Cen | 230 | 1 |
| Rest Areas | Kansas Data Access & Support Cen | 37 | 1 |
| Retaining Walls - Mobile LiDAR (2023) | Kansas Data Access & Support Cen | 363 | 1 |
| Retention (2025) | Kansas Data Access & Support Cen | 1,125 | 1 |
| Retention (2025; 16 sites) | Kansas Data Access & Support Cen | 16 | 1 |
| Retention (2025; original sites) | Kansas Data Access & Support Cen | 96 | 1 |
| Roads | Kansas Data Access & Support Cen | 5,262 | 1 |
| Rural Opportunity Zones | Kansas Data Access & Support Cen | 105 | 1 |
| Rural Water Districts | Kansas Data Access & Support Cen | 799 | 1 |
| School Districts | Kansas Data Access & Support Cen | 286 | 1 |
| School Sub Districts | Kansas Data Access & Support Cen | 8 | 1 |
| Section Boundaries for KCC Chloride Contamination Sites | Kansas Data Access & Support Cen | 182 | 1 |
| Section Boundaries for KDHE Chloride Contamination Sites | Kansas Data Access & Support Cen | 115 | 1 |
| Section Centroids for KCC Chloride Contamination Sites | Kansas Data Access & Support Cen | 182 | 1 |
| Section Centroids for KDHE Chloride Contamination Sites | Kansas Data Access & Support Cen | 114 | 1 |
| Sidewalks - Mobile LiDAR (2023) | Kansas Data Access & Support Cen | 2,000 | 1 |
| Southern & Central High Plains Aquifer Center Pivot Irrigation | Kansas Data Access & Support Cen | 50,116 | 1 |
| Speed Limits | Kansas Data Access & Support Cen | 1,000 | 1 |
| State Board of Education Districts | Kansas Data Access & Support Cen | 10 | 1 |
| State Bridges | Kansas Data Access & Support Cen | 1,000 | 1 |
| State Geology Contacts (M-118) | Kansas Data Access & Support Cen | 2,000 | 1 |
| State Surficial Geologic Units (M-118) | Kansas Data Access & Support Cen | 946 | 1 |
| State System | Kansas Data Access & Support Cen | 1,000 | 1 |
| Streambank Stabilization Projects | Kansas Data Access & Support Cen | 293 | 1 |
| Surface Management Agency Dataset | Kansas Data Access & Support Cen | 40 | 1 |
| Surface Water Monitoring Sites for Lakes and Streams | Kansas Data Access & Support Cen | 1,026 | 1 |
| Telephone Exchange Boundaries | Kansas Data Access & Support Cen | 618 | 1 |
| Tiger 2020 American Indian Reservations | Kansas Data Access & Support Cen | 7 | 1 |
| Tiger 2020 Block Groups | Kansas Data Access & Support Cen | 1,314 | 1 |
| Tiger 2020 Blocks | Kansas Data Access & Support Cen | 95,139 | 1 |
| Tiger 2020 Census Designated Places | Kansas Data Access & Support Cen | 740 | 1 |
| Tiger 2020 Counties | Kansas Data Access & Support Cen | 105 | 1 |
| Tiger 2020 Counties | Kansas Data Access & Support Cen | 105 | 1 |
| Tiger 2020 Landmark Areas | Kansas Data Access & Support Cen | 2,000 | 1 |
| Tiger 2020 Landmark Points | Kansas Data Access & Support Cen | 2,000 | 1 |
| Tiger 2020 Metro and Urban Areas | Kansas Data Access & Support Cen | 21 | 1 |
| Tiger 2020 Military Boundaries | Kansas Data Access & Support Cen | 7 | 1 |
| Tiger 2020 Political Townships | Kansas Data Access & Support Cen | 918 | 1 |
| Tiger 2020 Railroads | Kansas Data Access & Support Cen | 2,000 | 1 |
| Tiger 2020 Roads | Kansas Data Access & Support Cen | 236,256 | 1 |
| Tiger 2020 State Boundary | Kansas Data Access & Support Cen | 1 | 1 |
| Tiger 2020 Tracts | Kansas Data Access & Support Cen | 819 | 1 |
| Tiger 2020 Zip Code Tabulation Areas | Kansas Data Access & Support Cen | 313 | 1 |
| TMDL 303d Lake - Approved KDHE | Kansas Data Access & Support Cen | 111 | 1 |
| TMDL 303d Stream - Approved KDHE | Kansas Data Access & Support Cen | 1,050 | 1 |
| TMDL Lake | Kansas Data Access & Support Cen | 168 | 1 |
| TMDL Stream | Kansas Data Access & Support Cen | 1,339 | 1 |
| Top10pct BTPD Priority PADUS Intersect | Kansas Data Access & Support Cen | 11 | 1 |
| Trauma Centers (Public) | Kansas Data Access & Support Cen | 37 | 1 |
| Tuttle Creek conservation pool LiDAR 2017 18 | Kansas Data Access & Support Cen | 1 | 1 |
| Tuttle Creek flood pool LiDAR 2017 18 | Kansas Data Access & Support Cen | 1 | 1 |
| Tuttle Creek Lake extent | Kansas Data Access & Support Cen | 1 | 1 |
| Tuttle Creek Lake extent on August 16, 2023 | Kansas Data Access & Support Cen | 1 | 1 |
| Type Wells | Kansas Data Access & Support Cen | 1,750 | 1 |
| Underground Natural Gas Storage | Kansas Data Access & Support Cen | 16 | 1 |
| Unified School Districts | Kansas Data Access & Support Cen | 286 | 1 |
| USACE Reservoirs | Kansas Data Access & Support Cen | 51 | 1 |
| USGS 100K QUAD | Kansas Data Access & Support Cen | 66 | 1 |
| USGS 24K QUAD | Kansas Data Access & Support Cen | 1,521 | 1 |
| USGS 250K QUAD | Kansas Data Access & Support Cen | 22 | 1 |
| USGS Geographic Names Information System | Kansas Data Access & Support Cen | 31,063 | 1 |
| USNG 100000m | Kansas Data Access & Support Cen | 40,935 | 1 |
| USNG 10000m | Kansas Data Access & Support Cen | 111,408 | 1 |
| USNG 6x8 Zones | Kansas Data Access & Support Cen | 328 | 1 |
| Volatiles Organics | Kansas Data Access & Support Cen | 822 | 1 |
| Voting Districts | Kansas Data Access & Support Cen | 1,620 | 1 |
| Wakarusa Breach Inundation Areas | Kansas Data Access & Support Cen | 51 | 1 |
| Wakarusa Watershed Index Map | Kansas Data Access & Support Cen | 8 | 1 |
| Waterflood | Kansas Data Access & Support Cen | 2,000 | 1 |
| Wind Turbines | Kansas Data Access & Support Cen | 2,000 | 1 |
| ACS 2022 Cities Geo | Mid-America Regional Council | 130 | 1 |
| ACS 2022 Counties Geo | Mid-America Regional Council | 11 | 1 |
| ACS 2022 Tracts Geo | Mid-America Regional Council | 585 | 1 |
| ACS Counties HousingHub | Mid-America Regional Council | 9 | 1 |
| ACS Tracts HousingHub | Mid-America Regional Council | 584 | 1 |
| Active Transportation | Mid-America Regional Council | 16 | 1 |
| Active Transportation | Mid-America Regional Council | 56 | 1 |
| Activity Centers Without Bikeways | Mid-America Regional Council | 1,295 | 1 |
| ActivityCenters | Mid-America Regional Council | 1,000 | 1 |
| ActivityCenters | Mid-America Regional Council | 1,969 | 1 |
| AdultsWithDisabilitiesLayer | Mid-America Regional Council | 194 | 1 |
| Advanced Manufacturing | Mid-America Regional Council | 961 | 1 |
| Advanced Manufacturing | Mid-America Regional Council | 961 | 1 |
| Aging Senior Centers | Mid-America Regional Council | 15 | 1 |
| Aging Service Areas | Mid-America Regional Council | 13 | 1 |
| Air Quality Boundary | Mid-America Regional Council | 1 | 1 |
| Air Quality Maintenance Area | Mid-America Regional Council | 1 | 1 |
| Air Quality Monitoring Stations | Mid-America Regional Council | 10 | 1 |
| Airports | Mid-America Regional Council | 17 | 1 |
| Airports | Mid-America Regional Council | 99 | 1 |
| AlernativeFuelStations | Mid-America Regional Council | 379 | 1 |
| AlignmentTruman | Mid-America Regional Council | 1 | 1 |
| AlignmentTrumanHalfMi | Mid-America Regional Council | 1 | 1 |
| AlignmentTrumanQtrMile | Mid-America Regional Council | 1 | 1 |
| AlignmentUS24 | Mid-America Regional Council | 1 | 1 |
| AlignmentUS24HalfMile | Mid-America Regional Council | 1 | 1 |
| AlignmentUS24Mile | Mid-America Regional Council | 1 | 1 |
| AlignmentUS24QtrMile | Mid-America Regional Council | 1 | 1 |
| Alternative Fuel Stations | Mid-America Regional Council | 1,204 | 1 |
| AlternativeFuelStations | Mid-America Regional Council | 2,000 | 1 |
| AlternativeFuelStations | Mid-America Regional Council | 2,000 | 1 |
| Apartments | Mid-America Regional Council | 443 | 1 |
| Apartments | Mid-America Regional Council | 1,000 | 1 |
| Arenas | Mid-America Regional Council | 7 | 1 |
| Belton Signals | Mid-America Regional Council | 3 | 1 |
| Bicycle-involved crashes (2019 - 2023) | Mid-America Regional Council | 141 | 1 |
| Bikeways at Activity Centers | Mid-America Regional Council | 984 | 1 |
| BiStateCorridorApr22 | Mid-America Regional Council | 1 | 1 |
| BiStateSustainableReinvestmentCorridor | Mid-America Regional Council | 1 | 1 |
| Block Groups 2010 | Mid-America Regional Council | 2,000 | 1 |
| Block Groups 2020 | Mid-America Regional Council | 1,218 | 1 |
| Blue Springs Signals | Mid-America Regional Council | 8 | 1 |
| Bonner Springs Signals | Mid-America Regional Council | 3 | 1 |
| Bridge | Mid-America Regional Council | 6 | 1 |
| Bridge | Mid-America Regional Council | 13 | 1 |
| Bridge Condition (All) | Mid-America Regional Council | 3,677 | 1 |
| Bridge Condition (All) | Mid-America Regional Council | 4,927 | 1 |
| Bridge Condition (All) | Mid-America Regional Council | 5,000 | 1 |
| Bridge Condition (NHS) | Mid-America Regional Council | 1,101 | 1 |
| Bridge Condition (NHS) | Mid-America Regional Council | 1,090 | 1 |
| Bridge Condition (NHS) | Mid-America Regional Council | 5,000 | 1 |
| Bridge Condition (NHS) 2023 | Mid-America Regional Council | 1,121 | 1 |
| Bridge Condition All 2023 | Mid-America Regional Council | 2,000 | 1 |
| Bridges | Mid-America Regional Council | 30,740 | 1 |
| Building in Flood Zone Missouri | Mid-America Regional Council | 7,689 | 1 |
| CatchmentAreas988 | Mid-America Regional Council | 5 | 1 |
| Census Tracts | Mid-America Regional Council | 584 | 1 |
| CFPLine | Mid-America Regional Council | 82 | 1 |
| CFPPoint | Mid-America Regional Council | 18 | 1 |
| Child Care Deserts | Mid-America Regional Council | 592 | 1 |
| ChildCareCenters | Mid-America Regional Council | 1,459 | 1 |
| Cities | Mid-America Regional Council | 144 | 1 |
| Cities | Mid-America Regional Council | 87 | 1 |
| Cities | Mid-America Regional Council | 165 | 1 |
| Cities 2010 | Mid-America Regional Council | 1,703 | 1 |
| Cities 2020 | Mid-America Regional Council | 1,216 | 1 |
| Cities By County | Mid-America Regional Council | 165 | 1 |
| Cities2020 wCounty | Mid-America Regional Council | 160 | 1 |
| CKC Projects 2050 | Mid-America Regional Council | 526 | 1 |
| CKC Projects 2050 - Active Transportation Projects | Mid-America Regional Council | 98 | 1 |
| CKC Projects 2050 - Constrained Projects | Mid-America Regional Council | 240 | 1 |
| CKC Projects 2050 - Roadway Projects | Mid-America Regional Council | 372 | 1 |
| CMN 2020 KS HERE AllSegments 2022 AfternoonPTI | Mid-America Regional Council | 5,000 | 1 |
| CMN 2021 | Mid-America Regional Council | 1,000 | 1 |
| CMN 2022 KS HERE AllSegments 2022 | Mid-America Regional Council | 5,000 | 1 |
| CMN 2022 KS HERE AllSegments 2022 MorningPTI | Mid-America Regional Council | 5,000 | 1 |
| CMN 2022 KS HERE Highways 2022 AfternoonTTI | Mid-America Regional Council | 5,000 | 1 |
| CMN 2022 KS HERE Highways 2022 MorningTTI | Mid-America Regional Council | 5,000 | 1 |
| CMN 2022 KS HERE MajorRoadways 2022 AfternoonTTI | Mid-America Regional Council | 5,000 | 1 |
| CMN 2022 KS HERE MajorRoadways 2022 MorningTTI | Mid-America Regional Council | 5,000 | 1 |
| CMN KS Highways TTI Afternoon 2019 | Mid-America Regional Council | 1,000 | 1 |
| CMN KS Highways TTI Afternoon 2020 | Mid-America Regional Council | 1,000 | 1 |
| CMN KS Highways TTI Morning 2020 | Mid-America Regional Council | 1,000 | 1 |
| CMN KS MajorRoadways TTI Afternoon 2019 | Mid-America Regional Council | 1,000 | 1 |
| CMN KS MajorRoadways TTI Morning 2019 | Mid-America Regional Council | 1,000 | 1 |
| CMN KS MajorRoadways TTI Morning 2020 | Mid-America Regional Council | 1,000 | 1 |
| CMN KS PTI Afternoon 2019 | Mid-America Regional Council | 1,000 | 1 |
| CMN KS PTI Afternoon 2020 | Mid-America Regional Council | 1,000 | 1 |
| CMN KS PTI Morning 2019 | Mid-America Regional Council | 1,000 | 1 |
| CMN KS PTI Morning 2020 | Mid-America Regional Council | 1,000 | 1 |
| CMN KSMajorRoadwaysTTI Afternoon 2020 | Mid-America Regional Council | 1,000 | 1 |
| CMN MO Highways TTI Afternoon 2019 | Mid-America Regional Council | 912 | 1 |
| CMN MO Highways TTI Afternoon 2020 | Mid-America Regional Council | 924 | 1 |
| CMN MO Highways TTI Afternoon 2022 | Mid-America Regional Council | 924 | 1 |
| CMN MO Highways TTI Morning 2019 | Mid-America Regional Council | 912 | 1 |
| CMN MO Highways TTI Morning 2020 | Mid-America Regional Council | 924 | 1 |
| CMN MO Highways TTI Morning 2022 | Mid-America Regional Council | 924 | 1 |
| CMN MO MajorRoadways TTI Afternoon 2019 | Mid-America Regional Council | 616 | 1 |
| CMN MO MajorRoadways TTI Afternoon 2020 | Mid-America Regional Council | 612 | 1 |

---

© 2026 Dany Theriault. EVE "digital stem cell" glyph and glyph-based design principles — all rights reserved. Stewardship of rights of use and assignment for large public and institutional usage rests with the Pacific Utilities Design Council. Published as a time-stamped record of authorship and intent.

*Pour le bien-être du peuple.*
