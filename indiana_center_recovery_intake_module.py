# Indiana Center for Recovery – Member Intake Module
# Publicly listable information (no permission required)

ICR_INFO = {
    "name": "Indiana Center for Recovery – Terre Haute",
    "address": "135 E Hospital Ln, Terre Haute, IN 47802",
    "phone": "(812) 613-4914",
    "email": None,  # No public email listed
    "services": [
        "Medical Detox",
        "Inpatient Treatment",
        "Outpatient Treatment",
        "Dual-Diagnosis Care",
        "Clinical Therapy"
    ],
    "eligibility_rules": {
        "requires_id": True,
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
def evaluate_member_for_icr(member):
    rules = ICR_INFO["eligibility_rules"]
    reasons = []

    # Age requirement
    if member["age"] < rules["age_min"]:
        reasons.append("Must be 18 or older")

    # ID requirement
    if rules["requires_id"] and not member["has_id"]:
        reasons.append("Valid ID required")

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
        full_name="Michael Johnson",
        age=41,
        has_id=True,
        insurance_type="private",
        assessment_complete=True,
        substance_type="methamphetamine",
        homelessness_status=True,
        veteran_status=False
    )

    result = evaluate_member_for_icr(member)
    print(result)

if __name__ == "__main__":
    demo()
