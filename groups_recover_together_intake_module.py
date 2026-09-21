# Groups Recover Together – Member Intake Module
# Publicly listable information (no permission required)

GROUPS_INFO = {
    "name": "Groups Recover Together – Terre Haute",
    "address": "1359 E Margaret Ave, Terre Haute, IN 47802",
    "phone": "(812) 200-2789",
    "email": None,  # No public email listed
    "services": [
        "Medication-Assisted Treatment (Suboxone)",
        "Weekly Recovery Groups",
        "Counseling",
        "Case Management",
        "Peer Support"
    ],
    "eligibility_rules": {
        "requires_id": True,
        "requires_mat_readiness": True,
        "requires_appointment_commitment": True,
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
    mat_readiness,
    appointment_commitment,
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
        "mat_readiness": mat_readiness,
        "appointment_commitment": appointment_commitment,
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
def evaluate_member_for_groups(member):
    rules = GROUPS_INFO["eligibility_rules"]
    reasons = []

    # Age requirement
    if member["age"] < rules["age_min"]:
        reasons.append("Must be 18 or older")

    # ID requirement
    if rules["requires_id"] and not member["has_id"]:
        reasons.append("Valid ID required")

    # MAT readiness requirement
    if rules["requires_mat_readiness"] and not member["mat_readiness"]:
        reasons.append("Must be ready for MAT (Suboxone)")

    # Appointment commitment requirement
    if rules["requires_appointment_commitment"] and not member["appointment_commitment"]:
        reasons.append("Must commit to weekly appointments")

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
        full_name="Rebecca Allen",
        age=36,
        has_id=True,
        mat_readiness=True,
        appointment_commitment=True,
        insurance_type="medicaid",
        assessment_complete=True,
        substance_type="opioids",
        homelessness_status=False,
        veteran_status=False
    )

    result = evaluate_member_for_groups(member)
    print(result)

if __name__ == "__main__":
    demo()
