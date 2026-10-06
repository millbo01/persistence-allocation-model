# **1\. ACCESS AND TERMS**

**a. How the data are obtained** According to the VitalDB open dataset page and the PhysioNet repository documentation (Data Description section), the dataset files can be obtained via direct web download in .csv, compressed .csv.gz, and binary .vital file formats1. Additionally, the data can be accessed programmatically using an Application Programming Interface (API) and an open-source Python library named vitaldb, which is available on the Python Package Index (PyPI). The Python library features a VitalFile class capable of converting .vital structures directly into pandas DataFrames, numpy arrays, .csv files, or waveform-database (.wfdb) formats1. Regarding registration, accessing the dataset via the web download portal requires users to create an account and sign a data usage agreement, although no specific institutional credentials are required; conversely, the API and Python library can retrieve data tracks from the open dataset without explicit authentication3.  
**b. The licence and data-use terms** The VitalDB open dataset is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International Public License (CC BY-NC-SA 4.0), though the Amazon Web Services (AWS) registry documentation additionally references the standard Creative Commons Attribution 4.0 International Public License (CC BY 4.0)1. As outlined in the Provider website's "Registration Agreement and Data Use Agreement" (Terms and Conditions section), the permitted use is strictly for research and development purposes1.  
The required citation for any use of the dataset is explicitly defined on the dataset homepage as: "Lee HC, Park Y, Yoon SB, Yang SM, Park D, Jung CW. VitalDB, a high-fidelity multi-parameter vital signs database in surgical patients. Sci Data. 2022 Jun 8;9(1):279."1.  
The restrictions on redistribution prohibit users from transferring, assigning, or mortgaging any right or duty in relation to the use of the services. Furthermore, data cannot be disclosed to non-contracted third parties or employees unless equivalent agreement restrictions are enforced. The agreement stipulates that users must implement appropriate security measures to prevent unauthorized disclosure, and any such unauthorized disclosure must be reported to the Provider within 24 hours1. To gain access, users must explicitly accept the "Registration agreement and data use agreement"5.  
**c. The current version or release date and the number of cases** The current version of the open dataset on PhysioNet is Version 1.0.0, which was officially released on September 21, 20222. The open dataset contains exactly 6,388 cases1.

# **2\. CASE-LEVEL (CLINICAL) INFORMATION**

**a. The full list of case-level fields** The case-level clinical fields are documented in the clinical\_data.csv file and defined in the clinical\_parameters.csv data dictionary, as well as in Table 3 of the *Scientific Data* 2022 paper (Data Records section). The exact names, definitions, and units of the demographic, body size, surgery type, emergency status, physical status, anaesthesia type, timing, preoperative laboratory, and outcome variables are detailed in the table below1.

| Exact Name | Definition | Unit |
| :---- | :---- | :---- |
| caseid | Case ID; Random number between 00001 and 06388 | unit not stated |
| subjectid | Subject ID; Deidentified hospital ID of patient | unit not stated |
| age | Patient age | years |
| sex | Gender / Sex | M/F |
| height | Height | cm |
| weight | Weight | kg |
| bmi | Body mass index | kg/m2 |
| department | Surgical department | unit not stated |
| optype | Surgery type | unit not stated |
| dx | Diagnosis | unit not stated |
| opname | Operation name | unit not stated |
| approach | Surgical approach | unit not stated |
| position | Surgical position | unit not stated |
| emop | Emergency operation | unit not stated |
| asa | ASA Physical status classification | unit not stated |
| ane\_type | Type of anesthesia | unit not stated |
| casestart | Time of case recording start; Set to 0 for anonymization | sec |
| caseend | Time of case recording end; relative to casestart | sec |
| anestart | Time of anesthesia start; relative to casestart | sec |
| aneend | Time of anesthesia end; relative to casestart | sec |
| opstart | Time of operation (surgery) start; relative to casestart | sec |
| opend | Time of operation (surgery) end; relative to casestart | sec |
| preop\_htn | Preoperative hypertension | unit not stated |
| preop\_dm | Preoperative diabetes | unit not stated |
| preop\_ecg | Preoperative ecg | unit not stated |
| preop\_pft | Preoperative pulmonary function | unit not stated |
| preop\_hb | Preoperative hemoglobin | g/dL |
| preop\_plt | Preoperative platelet count | x1000/mcL |
| preop\_pt | Preoperative PT | % |
| preop\_aptt | Preoperative APTT | sec |
| preop\_na | Preoperative sodium | mmol/L |
| preop\_k | Preoperative potassium | mmol/L |
| preop\_gluc | Preoperative glucose | mg/dL |
| preop\_alb | Preoperative albumin | g/dL |
| preop\_ast | Preoperative asparate transferase | IU/L |
| preop\_alt | Preoperative alanine transferase | IU/L |
| preop\_bun | Preoperative blood urea nitrogen | mg/dL |
| preop\_cr | Preoperative creatinine | mg/dL |
| preop\_ph | Preoperative pH | unit not stated |
| preop\_hco3 | Preoperative bicarbonate | mmol/L |
| preop\_be | Preoperative base excess | mmol/L |
| preop\_pao2 | Preoperative partial pressure of oxygen | mmHg |
| preop\_paco2 | Preoperative partial pressure of carbon dioxide | mmHg |
| preop\_sao2 | Preoperative arterial oxygen saturation | % |
| adm | Admission time from casestart | sec |
| dis | Discharge time from casestart | sec |
| los\_postop | Postoperative length of hospital stay | days |
| los\_icu / icu\_days | Postoperative length of ICU stay | days |
| death\_inhosp | In-hospital Mortality | unit not stated |

**b. Intraoperative totals for blood loss, fluids, and urine** As documented in Table 3 of the *Scientific Data* 2022 paper and the VitalDB Clinical Information list, the dataset includes intraoperative totals for estimated blood loss, crystalloid, colloid, blood product volumes, and urine output. These are provided exclusively as single total values per case in the clinical file, rather than as time-stamped arrays. The exact field names and units are intraop\_ebl for estimated blood loss (mL), intraop\_crystalloid for infused crystalloid volume (mL), intraop\_colloid for infused colloid volume (mL), intraop\_rbc for red blood cell transfusion volume (unit), intraop\_ffp for fresh frozen plasma transfusion volume (unit), and intraop\_uo for urine output (mL)1.

# **3\. TIME-SERIES TRACKS**

**a. The full list of recording devices and their track names** The track\_names.csv parameter list and Table 2 of the *Scientific Data* 2022 paper itemize the recording devices, track names, data types (waveform or numeric), and sampling rates. Numeric data (N) is recorded at intervals ranging from 1 to 7 seconds, depending on the specific device, whereas waveform data (W) is sampled at frequencies between 62.5 Hz and 500 Hz9. The comprehensive structure is tabulated below.

| Device Prefix & Exact Track Name | Type | Sampling Rate / Interval | Unit |
| :---- | :---- | :---- | :---- |
| **SNUADC** (TramRac-4A Patient Monitor) |  |  |  |
| SNUADC/ART (Arterial pressure wave) | Waveform | 500 Hz | mmHg |
| SNUADC/CVP (Central venous pressure wave) | Waveform | 500 Hz | mmHg |
| SNUADC/ECG\_II (ECG lead II wave) | Waveform | 500 Hz | mV |
| SNUADC/ECG\_V5 (ECG lead V5 wave) | Waveform | 500 Hz | mV |
| SNUADC/FEM (Femoral arterial pressure wave) | Waveform | 500 Hz | mmHg |
| SNUADC/PLETH (Plethysmography wave) | Waveform | 500 Hz | unit not stated |
| **Solar8000** (Solar 8000 M Patient Monitor) |  |  |  |
| Solar8000/ART\_DBP, ART\_MBP, ART\_SBP | Numeric | 2 sec | mmHg |
| Solar8000/CVP | Numeric | 2 sec | mmHg |
| Solar8000/FEM\_DBP, FEM\_MBP, FEM\_SBP | Numeric | 2 sec | mmHg |
| Solar8000/NIBP\_DBP, NIBP\_MBP, NIBP\_SBP | Numeric | 2 sec | mmHg |
| Solar8000/PA\_DBP, PA\_MBP, PA\_SBP | Numeric | 2 sec | mmHg |
| Solar8000/INCO2, ETCO2 | Numeric | 2 sec | mmHg |
| Solar8000/BT (Body temperature) | Numeric | 2 sec | ℃ |
| Solar8000/FEO2, FIO2 | Numeric | 2 sec | % |
| Solar8000/GAS2\_EXPIRED, GAS2\_INSPIRED | Numeric | 2 sec | % |
| Solar8000/PLETH\_SPO2, VENT\_SET\_FIO2 | Numeric | 2 sec | % |
| Solar8000/HR, PLETH\_HR, RR, RR\_CO2, VENT\_RR | Numeric | 2 sec | /min |
| Solar8000/ST\_AVF, ST\_AVL, ST\_AVR, ST\_I, ST\_II, ST\_III, ST\_V5 | Numeric | 2 sec | mm |
| Solar8000/VENT\_COMPL | Numeric | 2 sec | mL/mbar |
| Solar8000/VENT\_INSP\_TM | Numeric | 2 sec | sec |
| Solar8000/VENT\_MAWP, VENT\_MEAS\_PEEP, VENT\_PIP, VENT\_PPLAT | Numeric | 2 sec | mbar |
| Solar8000/VENT\_MV | Numeric | 2 sec | L/min |
| Solar8000/VENT\_SET\_PCP | Numeric | 2 sec | cmH2O |
| Solar8000/VENT\_SET\_TV, VENT\_TV | Numeric | 2 sec | mL |
| **Primus** (Anesthesia Machine) |  |  |  |
| Primus/AWP (Airway pressure wave) | Waveform | 62.5 Hz | hPa |
| Primus/CO2 (Capnography wave) | Waveform | 62.5 Hz | mmHg |
| Primus/COMPLIANCE | Numeric | 7 sec | mL/mbar |
| Primus/ETCO2, INCO2 | Numeric | 7 sec | mmHg |
| Primus/EXP\_DES, EXP\_SEVO, INSP\_DES, INSP\_SEVO | Numeric | 7 sec | kPa |
| Primus/FEN2O, FEO2, FIN2O, FIO2, SET\_FIO2, SET\_INSP\_PAUSE | Numeric | 7 sec | % |
| Primus/FLOW\_AIR, FLOW\_O2, SET\_FLOW\_TRIG, SET\_FRESH\_FLOW, VENT\_LEAK | Numeric | 7 sec | mL/min |
| Primus/FLOW\_N2O, MAWP\_MBAR, PAMB\_MBAR, PEEP\_MBAR, PIP\_MBAR, PPLAT\_MBAR, SET\_INSP\_PRES, SET\_INTER\_PEEP, SET\_PIP, SET\_RR\_IPPV | Numeric | 7 sec | mbar |
| Primus/MAC | Numeric | 7 sec | unit not stated |
| Primus/MV, SET\_TV\_L | Numeric | 7 sec | L |
| Primus/RR\_CO2 | Numeric | 7 sec | /min |
| Primus/SET\_AGE | Numeric | 7 sec | years |
| Primus/SET\_INSP\_TM | Numeric | 7 sec | sec |
| Primus/TV | Numeric | 7 sec | mL |
| **Orchestra** (Target-Controlled Infusion Pump) |  |  |  |
| Orchestra/\*\_RATE (AMD, DEX2, DEX4, DOBU, DOPA, DTZ, EPI, FUT, MRN, NEPI, NPS, NTG, OXY, PGE1, PHEN, PPF20, RFTN20, RFTN50, ROC, VASO, VEC) | Numeric | 1 sec | mL/hr |
| Orchestra/\*\_VOL (same drug prefixes as above) | Numeric | 1 sec | mL |
| Orchestra/PPF20\_CE, PPF20\_CP, PPF20\_CT | Numeric | 1 sec | mcg/mL |
| Orchestra/\*\_CE, \*\_CP, \*\_CT (RFTN20, RFTN50) | Numeric | 1 sec | ng/mL |
| **BIS** (BIS Vista EEG Monitor) |  |  |  |
| BIS/EEG1\_WAV, EEG2\_WAV | Waveform | 128 Hz | uV |
| BIS/BIS | Numeric | 1 sec | unit not stated |
| BIS/EMG, TOTPOW | Numeric | 1 sec | dB |
| BIS/SEF | Numeric | 1 sec | Hz |
| BIS/SQI, SR | Numeric | 1 sec | % |
| **Invos** (Cerebral/Somatic Oximeter) |  |  |  |
| Invos/SCO2\_L, SCO2\_R | Numeric | 5 sec | % |
| **Vigileo** (Cardiac Output Monitor) |  |  |  |
| Vigileo/CI | Numeric | 2 sec | L/min/m2 |
| Vigileo/CO | Numeric | 2 sec | L/min |
| Vigileo/SV | Numeric | 2 sec | mL/beat |
| Vigileo/SVI | Numeric | 2 sec | mL/beat/m2 |
| Vigileo/SVV | Numeric | 2 sec | % |
| **EV1000** (Cardiac Output Monitor) |  |  |  |
| EV1000/ART\_MBP | Numeric | 2 sec | mmHg |
| EV1000/CI | Numeric | 2 sec | L/min/m2 |
| EV1000/CO | Numeric | 2 sec | L/min |
| EV1000/CVP | Numeric | 2 sec | cmH2O |
| EV1000/SV | Numeric | 2 sec | mL/beat |
| EV1000/SVI | Numeric | 2 sec | mL/beat/m2 |
| EV1000/SVR | Numeric | 2 sec | dn-s/cm5 |
| EV1000/SVRI | Numeric | 2 sec | dn-s-m2/cm5 |
| EV1000/SVV | Numeric | 2 sec | % |
| **Vigilance** (Vigilance II Cardiac Output Monitor) |  |  |  |
| Vigilance/BT\_PA | Numeric | 2 sec | ℃ |
| Vigilance/CI | Numeric | 2 sec | L/min/m2 |
| Vigilance/CO | Numeric | 2 sec | L/min |
| Vigilance/EDV, ESV | Numeric | 2 sec | mL |
| Vigilance/EDVI, ESVI | Numeric | 2 sec | mL/m2 |
| Vigilance/HR\_AVG | Numeric | 2 sec | /min |
| Vigilance/RVEF, SQI, SVO2 | Numeric | 2 sec | % |
| Vigilance/SNR | Numeric | 2 sec | dB |
| Vigilance/SV | Numeric | 2 sec | mL/beat |
| Vigilance/SVI | Numeric | 2 sec | mL/beat/m2 |
| **CardioQ** (CardioQ-ODM+ Cardiac Output Monitor) |  |  |  |
| CardioQ/ABP | Waveform | 180 Hz | mmHg |
| CardioQ/FLOW | Waveform | 180 Hz | cm/sec |
| CardioQ/CI | Numeric | 1 sec | L/min/m2 |
| CardioQ/CO | Numeric | 1 sec | L/min |
| CardioQ/FTc, FTp | Numeric | 1 sec | ms |
| CardioQ/HR | Numeric | 1 sec | /min |
| CardioQ/MA | Numeric | 1 sec | cm/sec2 |
| CardioQ/MD, SD | Numeric | 1 sec | cm |
| CardioQ/PV | Numeric | 1 sec | cm/sec |
| CardioQ/SV | Numeric | 1 sec | mL/beat |
| CardioQ/SVI | Numeric | 1 sec | mL/beat/m2 |
| **FMS** (FMS2000 Rapid Infusion System) |  |  |  |
| FMS/FLOW\_RATE, TOTAL\_VOL | Numeric | per 2.875 mL | mL |
| FMS/INPUT\_AMB\_TEMP, INPUT\_TEMP, OUTPUT\_AMB\_TEMP, OUTPUT\_TEMP | Numeric | per 2.875 mL | ℃ |
| FMS/PRESSURE | Numeric | per 2.875 mL | mmHg |

**b. Specific time-series tracks requested** The track\_names.csv and the VitalDB Dataset Summary table define the exact track names, units, recording intervals, and the overall volume of device usage across the database1.

* **Invasive arterial pressure:** Waveforms include SNUADC/ART (500 Hz, mmHg), SNUADC/FEM (500 Hz, mmHg), and CardioQ/ABP (180 Hz, mmHg). Numeric systolic, diastolic, and mean values are recorded under Solar8000/ART\_SBP, Solar8000/ART\_DBP, Solar8000/ART\_MBP, Solar8000/FEM\_SBP, Solar8000/FEM\_DBP, Solar8000/FEM\_MBP, Solar8000/PA\_SBP, Solar8000/PA\_DBP, Solar8000/PA\_MBP, and EV1000/ART\_MBP (all sampled at 2-second intervals, mmHg). The SNUADC/ART waveform track is contained in exactly 3,645 cases11. The SNUADC device family is present in 6,355 cases, the Solar 8000M device is present in 6,388 cases, and CardioQ tracks appear in 29 cases1. Individual case counts for the remaining discrete numeric tracks are not stated.  
* **Non-invasive blood pressure:** Numeric tracks are Solar8000/NIBP\_SBP, Solar8000/NIBP\_DBP, and Solar8000/NIBP\_MBP (2-second interval, mmHg). The parent Solar 8000M device is present in 6,388 cases, but the exact case count for these specific tracks is not stated1.  
* **Heart rate and electrocardiogram:** Heart rate numerics include Solar8000/HR, Solar8000/PLETH\_HR, Vigilance/HR\_AVG (all 2-second interval, /min), and CardioQ/HR (1-second interval, /min). Electrocardiogram waveforms include SNUADC/ECG\_II and SNUADC/ECG\_V5 (both 500 Hz, mV). Case counts for these specific individual tracks are not stated, though the SNUADC device appears in 6,355 cases and the Solar 8000M in 6,388 cases1.  
* **Stroke volume, cardiac output, SVV, and PPV:** Stroke volume (SV) tracks include Vigileo/SV, EV1000/SV, Vigilance/SV (2-second interval, mL/beat), and CardioQ/SV (1-second interval, mL/beat). Cardiac output (CO) tracks include Vigileo/CO, EV1000/CO, Vigilance/CO (2-second interval, L/min), and CardioQ/CO (1-second interval, L/min). Stroke volume variation (SVV) tracks include Vigileo/SVV and EV1000/SVV (2-second interval, %). Pulse pressure variation (PPV) is not recorded directly by any primary device, but rather can be calculated as a secondary variable via external analysis libraries. Case counts corresponding to the hardware are 348 cases for Vigileo, 599 cases for EV1000, 63 cases for Vigilance II, and 29 cases for CardioQ1.  
* **Peripheral oxygen saturation and plethysmography:** Numerics include Solar8000/PLETH\_SPO2 (2-second interval, %). Waveforms include SNUADC/PLETH (500 Hz, unitless). Exact case counts for the tracks are not stated10.  
* **Cerebral or tissue oximetry:** Tracks include Invos/SCO2\_L and Invos/SCO2\_R (5-second interval, %). The INVOS device was utilized in 33 cases1.  
* **Depth-of-anaesthesia indices:** Derived indices include BIS/BIS (1-second interval, unitless), BIS/SEF (1-second interval, Hz), BIS/SQI (1-second interval, %), BIS/SR (1-second interval, %), BIS/TOTPOW (1-second interval, dB), BIS/EMG (1-second interval, dB), and Primus/MAC (7-second interval, unitless). The BIS Vista device is present in 5,566 cases, and the Primus machine in 6,362 cases1.  
* **Body temperature:** Tracks include Solar8000/BT (2-second interval, ℃), Vigilance/BT\_PA (2-second interval, ℃), FMS/INPUT\_TEMP, and FMS/OUTPUT\_TEMP (both recorded per 2.875 mL infused, ℃). The FMS2000 device is recorded in 15 cases1.  
* **End-tidal gases and ventilator settings:** End-tidal CO2 is recorded via Solar8000/ETCO2 (2-second interval, mmHg) and Primus/ETCO2 (7-second interval, mmHg). Expired oxygen includes Solar8000/FEO2 (2-second interval, %) and Primus/FEO2 (7-second interval, %). Volatile gases are monitored via Solar8000/GAS2\_EXPIRED (2-second interval, %), Primus/EXP\_DES (7-second interval, kPa), and Primus/EXP\_SEVO (7-second interval, kPa). Ventilator settings include Solar8000/VENT\_SET\_FIO2 (2-second interval, %), Solar8000/VENT\_SET\_PCP (2-second interval, cmH2O), Solar8000/VENT\_SET\_TV (2-second interval, mL), Primus/SET\_FIO2 (7-second interval, %), Primus/SET\_INSP\_PRES (7-second interval, mbar), Primus/SET\_TV\_L (7-second interval, L), Primus/SET\_INTER\_PEEP (7-second interval, mbar), Primus/SET\_PIP (7-second interval, mbar), and Primus/SET\_RR\_IPPV (7-second interval, mbar). Case counts for these individual tracks are not stated10.

**c. How tracks are time-aligned within a case** According to the *Scientific Data* 2022 paper (Data Records section), all time-series data tracks within a specific vital file are strictly aligned and anonymized relative to a unified zero-point8.

* **Time origin:** The origin point is uniformly defined by the casestart parameter, which signifies the initiation of case file recording. The value of casestart is perpetually set to "0" seconds across all files8.  
* **Time resolution:** The time arrays are expressed continuously in seconds relative to the casestart origin. Numeric data possesses an update resolution spanning 1 to 7 seconds based on device polling rates, whereas waveform data inherently possesses sub-second resolution constrained by sampling frequencies between 62.5 Hz and 500 Hz8.  
* **Gaps or device disconnections:** When accessing the data by extracting structural columns, the dataset handles discontinuity differently depending on the data type. Within numeric data tracks, missing value rows generated by device disconnection or signal loss are entirely removed from the record structure. Conversely, within waveform data tracks, rows reflecting missing values are not removed, but are instead retained as blank fields (represented programmatically as nan values) to ensure the fixed dimensional grid of the high-frequency timeline is preserved4.

# **4\. INTERVENTIONS AND EVENTS**

**a. Drug infusions** The track\_names.csv parameter list and *Scientific Data* 2022 documentation (Table 2\) outline the drug infusion parameters acquired from Orchestra target-controlled infusion pumps9. Recorded at rigid 1-second intervals, the exact drug prefixes are: Amiodarone (AMD), Dexmedetomidine (DEX2, DEX4), Dobutamine (DOBU), Dopamine (DOPA), Diltiazem (DTZ), Epinephrine (EPI), Futhan (FUT), Milrinone (MRN), Norepinephrine (NEPI), Nitroprusside (NPS), Nitroglycerine (NTG), Oxytocin (OXY), Prostaglandin-E1 (PGE1), Phenylephrine (PHEN), Propofol (PPF20), Remifentanil (RFTN20, RFTN50), Rocuronium (ROC), Vasopressin (VASO), and Vecuronium (VEC). Each drug's delivery is logged via parallel tracks capturing the infusion rate (\_RATE measured in mL/hr) and the cumulative infused volume (\_VOL measured in mL). For specific target-controlled anesthetics such as Propofol and Remifentanil, the pumps concurrently record calculated concentrations, specifically the target (\_CT), plasma (\_CP), and effect-site (\_CE) concentrations (measured in mcg/mL for Propofol and ng/mL for Remifentanil)9.  
**b. Bolus drugs** Based on the clinical parameters dictionary, bolus administrations of vasopressors, inotropes, and anesthetics are fundamentally not recorded as time-stamped series or discrete tracks. Instead, they are aggregated into singular total cumulative doses reflecting the entire surgical case. The exact clinical fields recording these totals are intraop\_ppf (Propofol bolus dose, mg), intraop\_mdz (Midazolam bolus dose, mg), intraop\_ftn (Fentanyl bolus dose, mcg), intraop\_rocu (Rocuronium dose, mg), intraop\_vecu (Vecuronium dose, mg), intraop\_eph (Ephedrine dose, mg), intraop\_phe (Phenylephrine dose, mcg), intraop\_epi (Epinephrine dose, mcg), and intraop\_ca (Calcium chloride dose, mg). Exact times for boluses are not stated1.  
**c. Fluids and blood products given during surgery** Routine intraoperative fluids and blood products are similarly archived solely as case-level totals (e.g., intraop\_crystalloid, intraop\_colloid, intraop\_rbc, intraop\_ffp) rather than continuous streams1. However, if the FMS2000 Rapid Infusion system is actively deployed during a severe intervention, high-resolution volumetric administration is recorded natively in the time-series files. Under this specific hardware configuration, the exact tracks FMS/TOTAL\_VOL and FMS/FLOW\_RATE generate discrete structural records at a precise recording interval of every 2.875 mL infused9.  
**d. Bleeding** Intraoperative bleeding is recorded formally as an aggregate variable representing estimated blood loss for the entire procedure, mapped to the exact name intraop\_ebl in the clinical file1. Time-stamped volumetric blood loss, such as discrete suction, swab measurements, or cell-saver inputs at varying time points, are not stated in the database documentation.  
**e. Any event or annotation records** The .vital file architecture integrates a distinct event track. Within this track, specific chronological milestones sourced retrospectively from the electronic medical record (EMR) are embedded. The exact named milestones included are the times of case recording start (casestart), case recording end (caseend), anesthesia start (anestart), anesthesia end (aneend), surgery start (opstart), and surgery end (opend)8. While the Vital Recorder software generally permits the programmatic inclusion of arbitrary textual strings to annotate ad-hoc events relative to the zeroed timeline12, specific standardized surgical annotations (e.g., surgical incision, start of bypass, position changes, or clamping) are not stated in the parameter dictionaries.

# **5\. INTRAOPERATIVE LABORATORY RESULTS**

All intraoperative and perioperative laboratory test results (ranging from 3 months prior to 3 months following surgery) are housed in the secondary lab\_data.csv file2. As outlined in the lab\_parameters.csv documentation and the *Scientific Data* 2022 methods section, these laboratory events are intrinsically time-stamped using a relative time marker designated exactly as dt. The dt metric operates in continuous seconds anchored to the case reference point (where casestart equals 0), resulting in negative integer values for tests conducted preoperatively and positive integer values for intraoperative or postoperative assays2.  
The exhaustive list of recorded blood parameters, with their exact test names (name) and corresponding units, comprises13:

* **Complete Blood Count (CBC):** wbc (White blood cell count, ×1000/mcL), hb (Hemoglobin, g/dL), hct (Hematocrit, %), plt (Platelet count, ×1000/mcL), esr (Erythrocyte sedimentation rate, mm/hr).  
* **Chemistry:** gluc (Glucose, mg/dL), tprot (Total protein, g/dL), alb (Albumin, g/dL), tbil (Total bilirubin, mg/dL), ast (Asparate transferase, IU/L), alt (Alanine transferase, IU/L), bun (Blood urea nitrogen, mg/dL), cr (Creatinine, mg/dL), gfr (Glomerular filtration rate, mL/min/1.73 m2), ccr (Creatinine clearance, mL/min), na (Sodium, mmol/L), k (Potassium, mmol/L), ica (ionized Calcium, mmol/L), cl (Chloride, mmol/L), ammo (Ammonia, mcg/dL), crp (C-reactive protein, mg/dL), lac (Lactate, mmol/L).  
* **Coagulation:** ptinr (Prothrombin time, INR), pt% (Prothrombin time, %), ptsec (Prothrombin time, sec), aptt (Activated partial thromboplastin time, sec), fib (Fibrinogen, mg/dL).  
* **Arterial Blood Gas Analysis (ABGA):** ph (pH, unit not stated), pco2 (partial pressure of CO2, mmHg), po2 (partial pressure of O2, mmHg), hco3 (Bicarbonate, mmol/L), be (Base excess, mmol/L), sao2 (Arterial oxygen saturation, %).

# **6\. KNOWN LIMITATIONS**

The formal dataset description located in the *Scientific Data* 2022 paper highlights several known data-quality limitations and structural nuances intrinsic to the database formulation8.

* **Artefacts:** The raw physiological signals forming the primary tracks are intentionally not pre-processed. The authors emphasize that real-world noise generated within the operating room is deliberately preserved to test the robustness of analytical algorithms. Specifically noted are extensive electrocardiography and electroencephalography noises directly induced by electrocautery and parallel electrophysiologic monitoring8.  
* **Missing devices:** The structural integrity of specific waveforms frequently exhibits missing blocks due to environmental workflow realities. Documented gaps explicitly include data loss affecting the bispectral index, cerebral oximeter, electrocardiography, and plethysmography, which are attributed to the temporary detachment of external sensors9.  
* **Known errors in any field:** The text expressly documents that abnormal physiological values are structurally embedded within the arterial pressure tracks. These anomalies inherently correspond to physical interventions by clinicians, specifically during arterial blood sampling protocols. The presence of known errors in any other field is not stated9.  
* **Changes of device or software over the collection period:** Whether devices or software parameters experienced undocumented shifts or upgrades across the data collection period is not stated.  
* **Cases excluded from the open set:** The structural footprint of the final repository does not encompass all initially recorded cases. From a primary cohort of 7,051 eligible surgeries, a total of 663 cases were intentionally excluded from the open access set during internal technical validation. The explicit causes for these exclusions were procedures restricted solely to local anesthesia (239 cases), files containing incomplete electronic recordings (279 cases), and instances where essential core data tracks suffered complete structural loss (145 cases). The resulting balance establishes the current open-set ceiling of 6,388 surgical cases2.  
* **Temporal Logging Discrepancies:** A known structural discrepancy exists regarding the precision of case-level event boundaries. Because the exact moments for anesthesia start (anestart) and anesthesia end (aneend) were imported retrospectively from the hospital EMR—which inherently rounds inputs to rigid 5-minute intervals—there remains a documented timing misalignment of several minutes between these logged EMR markers and the precise digital start (casestart) and end (caseend) recorded by the automated hardware8.

**SOURCE LIST:**  
**SELF-CHECK:**

* No introduction or background written: CHECKED.  
* No data values, distributions, thresholds, or findings reported anywhere (excluding permissible case counts): CHECKED.  
* No study using VitalDB listed: CHECKED.  
* Every answer sourced or marked "not stated": CHECKED.

#### **Works cited**

> 1. Dataset : VitalDB, [https\://vitaldb.net/dataset/](https://vitaldb.net/dataset/)  
> 2. VitalDB, a high-fidelity multi-parameter vital signs database in, [https\://physionet.org/content/vitaldb/1.0.0/](https://physionet.org/content/vitaldb/1.0.0/)  
> 3. Open datasets in perioperative medicine: a narrative review, [https\://www\.anesth-pain-med.org/journal/view.php?number=1212\&viewtype=pubreader](https://www.anesth-pain-med.org/journal/view.php?number=1212&viewtype=pubreader)  
> 4. Dataset \- VitalDB Python Library, [https\://vitaldb.net/dataset/?query=lib](https://vitaldb.net/dataset/?query=lib)  
> 5. Registration Agreement \- VitalDB, [https\://vitaldb.net/registration-agreement/](https://vitaldb.net/registration-agreement/)  
> 6. VitalDB \- Registry of Open Data on AWS, [https\://registry.opendata.aws/vitaldb/](https://registry.opendata.aws/vitaldb/)  
> 7. VitalDB, a high-fidelity multi-parameter vital signs database in, [https\://physionet.org/content/vitaldb/1.0.0/LICENSE.txt](https://physionet.org/content/vitaldb/1.0.0/LICENSE.txt)  
> 8. (PDF) VitalDB, a high-fidelity multi-parameter vital signs database in, [https\://www\.researchgate.net/publication/361167330\_VitalDB\_a\_high-fidelity\_multi-parameter\_vital\_signs\_database\_in\_surgical\_patients](https://www.researchgate.net/publication/361167330_VitalDB_a_high-fidelity_multi-parameter_vital_signs_database_in_surgical_patients)  
> 9. VitalDB, a high-fidelity multi-parameter vital signs database in ... \- PMC, [https\://pmc.ncbi.nlm.nih.gov/articles/PMC9178032/](https://pmc.ncbi.nlm.nih.gov/articles/PMC9178032/)  
> 10. [https\://physionet.org/content/vitaldb/1.0.0/track\_names.csv](https://physionet.org/content/vitaldb/1.0.0/track_names.csv)  
> 11. A Latent-Class Analysis of the VitalDB Registry \- MDPI, [https\://www\.mdpi.com/2077-0383/15/17/6871](https://www.mdpi.com/2077-0383/15/17/6871)  
> 12. Vitabel: A Python Framework for Visualizing and Labelling High, [https\://pmc.ncbi.nlm.nih.gov/articles/PMC13249750](https://pmc.ncbi.nlm.nih.gov/articles/PMC13249750)  
> 13. [https\://physionet.org/content/vitaldb/1.0.0/lab\_parameters.csv](https://physionet.org/content/vitaldb/1.0.0/lab_parameters.csv)