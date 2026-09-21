# Next Step Foundation – Member Intake Module
# Publicly listable information (no permission required)

NEXT_STEP_INFO = {
    "name": "Next Step Foundation – Terre Haute",
    "address": "619 Washington Ave, Terre Haute, IN 47802",
    "phone": "(812) 917-5006",
    "email": None,  # No public email listed
    "services": [
        "Transitional Housing",
        "Sober Living",
        "Recovery Support",
        "Peer Accountability",
        "Community-Based Recovery"
    ],
    "eligibility_rules": {
        "requires_id": True,
        "requires_sobriety_commitment": True,
        "requires_assessment": False,
        "accepts_medicaid": False,  # Housing programs typically do not bill insurance
        "accepts_private_insurance": False,
        "accepts_self_pay": True,
        "age_min": 18
    }
}

# Pre-filled member structure
def create_member_record(
    full_name,
    age,
    has_id,
    sobriety_commitment,
    insurance_type,
    assessment_complete,
    substance_type,
    homelessness_status,
    veteran_status
):
    return {
        "full_name": full_name,
        "age": age,
        "has_id": has_id,
        "sobriety_commitment": sobriety_commitment,
        "insurance_type": insurance_type,
        "assessment_complete": assessment_complete,
        "substance_type": substance_type,
        "homelessness_status": homelessness_status,
        "veteran_status": veteran_status,
        "intake_timestamp": None,
        "eligible": None,
        "reasons": []
    }

# Eligibility engine
def evaluate_member_for_next_step(member):
    rules = NEXT_STEP_INFO["eligibility_rules"]
    reasons = []

    # Age requirement
    if member["age"] < rules["age_min"]:
        reasons.append("Must be 18 or older")

    # ID requirement
    if rules["requires_id"] and not member["has_id"]:
        reasons.append("Valid ID required")

    # Sobriety commitment requirement
    if rules["requires_sobriety_commitment"] and not member["sobriety_commitment"]:
        reasons.append("Sobriety commitment required")

    # Insurance is irrelevant for housing programs
    if member["
