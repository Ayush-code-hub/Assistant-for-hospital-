# data.py

RAW_KNOWLEDGE_BASE = [
    {
        "id": "KB001",
        "title": "Post-TKR Pain Management",
        "department": "Orthopaedics",
        "access_level": "STAFF",
        "content": "Supra Ortho uses Paracetamol 650mg QDS as first-line post-TKR. Escalate to Tramadol 50mg if VAS > 6. AVOID NSAIDs at all steps due to surgical bleeding risk. Decision by Dr. Vikram, January 2025."
    },
    {
        "id": "KB002",
        "title": "Patient Rajan Drug Alert",
        "department": "Cardiology",
        "access_level": "STAFF",
        "content": "ABSOLUTE: No ibuprofen, no aspirin, no diclofenac for patient Rajan. Cardiac stent 2022, dual antiplatelet therapy. Previous 8 NSAID refusals documented. Family also requests — refuse firmly."
    },
    {
        "id": "KB003",
        "title": "Sepsis Protocol v3",
        "department": "ICU",
        "access_level": "STAFF",
        "content": "Supra Sepsis Bundle v3 2026: blood cultures before antibiotics, lactate within 1 HOUR (tightened from v2 which was 3 hours), 30mL/kg crystalloid for hypotension, vasopressors if MAP <65 after fluids."
    },
    {
        "id": "KB004",
        "title": "DVT Prophylaxis",
        "department": "Surgery",
        "access_level": "STAFF",
        "content": "ALL ortho surgical patients receive DVT prophylaxis: Enoxaparin 40mg SC daily starting 12 hours post-op. Duration: 14 days for TKR, 28 days for THR."
    },
    {
        "id": "KB005",
        "title": "Diabetic Fasting Protocol",
        "department": "General Medicine",
        "access_level": "STAFF",
        "content": "For fasting patients with Type 2 DM: adjust insulin timing not dose. Skip Glimepiride on fast days, continue Metformin with evening meal."
    },
    {
        "id": "KB006",
        "title": "TKR Discharge Rule",
        "department": "Orthopaedics",
        "access_level": "STAFF",
        "content": "Do NOT discharge TKR patients before 48 hours post-op. Past incident: patient discharged at 36 hours developed DVT at home, emergency readmission."
    },
    {
        "id": "KB007",
        "title": "Zimmer Biomet Preference",
        "department": "Orthopaedics",
        "access_level": "STAFF",
        "content": "Supra Ortho uses Zimmer Biomet as preferred TKR implant vendor. Smith & Nephew for revision cases only."
    },
    {
        "id": "KB008",
        "title": "Ortho Budget FY2026",
        "department": "Administration",
        "access_level": "CONFIDENTIAL",
        "content": "FY2026 Ortho budget: 4.2 Cr. Implants 45%, Staffing 30%, Equipment 15%, Training 10%. CONFIDENTIAL — HOD and Admin only."
    },
    {
        "id": "KB009",
        "title": "Night Shift Handover",
        "department": "General Medicine",
        "access_level": "STAFF",
        "content": "15-minute structured handover using SBAR format. Include: pending labs, new admissions past 4 hours, patients for morning surgery."
    },
    {
        "id": "KB010",
        "title": "Warfarin-NSAID Interaction",
        "department": "Pharmacy",
        "access_level": "STAFF",
        "content": "CRITICAL: Never prescribe NSAIDs to patients on Warfarin. Risk of life-threatening GI bleed. Use Paracetamol for pain."
    },
    {
        "id": "KB011",
        "title": "Verbal Orders Policy",
        "department": "Administration",
        "access_level": "STAFF",
        "content": "NEVER accept verbal orders for medication changes without written confirmation within 1 hour. Exception: cardiac arrest only. Incident 2023: wrong dose from mishearing."
    },
    {
        "id": "KB012",
        "title": "Formulary Brands",
        "department": "Pharmacy",
        "access_level": "STAFF",
        "content": "Supra preferred brands: Paracetamol (Calpol/Dolo), Omeprazole (Omez), Amoxicillin (Mox), Metformin (Glycomet)."
    },
    {
        "id": "KB013",
        "title": "Padma Fasting DM",
        "department": "General Medicine",
        "access_level": "STAFF",
        "content": "Mrs. Padma, 62F, Type 2 DM. Observes Ekadashi fasting twice monthly. 3 hypoglycemia episodes in 2025 before protocol adjustment."
    },
    {
        "id": "KB014",
        "title": "Hospital Expansion Plan",
        "department": "Administration",
        "access_level": "CONFIDENTIAL",
        "content": "Board-approved: 80 beds by Q4 2027. 85 Cr investment. STRICTLY CONFIDENTIAL — Admin only."
    },
    {
        "id": "KB015",
        "title": "Emergency Codes",
        "department": "Administration",
        "access_level": "STAFF",
        "content": "Code Blue: cardiac arrest. Code Red: fire. Code Pink: infant abduction. Code Grey: combative patient."
    }
]

USERS = {
    "Dr. Vikram": {"role": "HOD", "dept": "Orthopaedics", "level": "CONFIDENTIAL"},
    "Nurse Priya": {"role": "Staff Nurse", "dept": "Orthopaedics", "level": "STAFF"},
    "Dr. Meera": {"role": "HOD", "dept": "General Medicine", "level": "CONFIDENTIAL"},
    "Dr. Ananya": {"role": "Junior Doctor", "dept": "General Medicine", "level": "STAFF"},
    "Admin Suresh": {"role": "Hospital Admin", "dept": "Administration", "level": "CONFIDENTIAL"}
}