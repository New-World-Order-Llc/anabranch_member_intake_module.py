# BrightWing Recovery – Member Intake Module
# Publicly listable information (no permission required)

BRIGHTWING_INFO = {
    "name": "BrightWing Recovery – Terre Haute",
    "address": "335 Kent Ave, Terre Haute, IN 47807",
    "phone": "(812) 297-3322",
    "email": None,  # No public email listed
    "services": [
        "Medical Detox",
        "Residential Treatment",
        "Clinical Therapy",
        "24/7 Recovery Support",
        "Dual-Diagnosis Care"
    ],
    "eligibility_rules": {
        "requires_id": True,
        "requires_detox_readiness": True,
        "requires_residential_stability": True,
        "requires_assessment": True,
        "accepts_medicaid": True,
        "accepts_private_insurance": True,
        "accepts_self_pay": True,
        "age_min": 18
    }
}

# Pre-filled member structure
def create_member_record(
    full_name,
    age,
    has_id,
    detox_readiness,
    residential_stability,
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
        "detox_readiness": detox_readiness,
        "residential_stability": residential_stability,
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
def evaluate_member_for_brightwing(member):
    rules = BRIGHTWING_INFO["eligibility_rules"]
    reasons = []

    # Age requirement
    if member["age"] < rules["age_min"]:
        reasons.append("Must be 18 or older")

    # ID requirement
    if rules["requires_id"] and not member["has_id"]:
        reasons.append("Valid ID required")

    # Detox readiness requirement
    if rules["requires_detox_readiness"] and not member["detox_readiness"]:
        reasons.append("Must be medically ready for detox")

    # Residential stability requirement
    if rules["requires_residential_stability"] and not member["residential_stability"]:
        reasons.append("Residential stability required for treatment")

    # Assessment requirement
    if rules["requires_assessment"] and not member["assessment_complete"]:
        reasons.append("Clinical assessment required")

    # Insurance check
    if member["insurance_type"] not in ["medicaid", "private", "self_pay"]:
        reasons.append("Insurance type not accepted")

    # Finalize
    member["intake_timestamp"] = "AUTO"
    member["eligible"] = len(reasons) == 0
    member["reasons"] = reasons

    return member

# Example usage
def demo():
    member = create_member_record(
        full_name="Christopher Lane",
        age=45,
        has_id=True,
        detox_readiness=True,
        residential_stability=True,
        insurance_type="private",
        assessment_complete=True,
        substance_type="alcohol",
        homelessness_status=False,
        veteran_status=True
    )

    result = evaluate_member_for_brightwing(member)
    print(result)

if __name__ == "__main__":
    demo()
