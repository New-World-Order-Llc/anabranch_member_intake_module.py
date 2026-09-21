# Wabash Valley Adult & Teen Challenge – Member Intake Module
# Publicly listable information (no permission required)

TEEN_CHALLENGE_INFO = {
    "name": "Wabash Valley Adult & Teen Challenge – Terre Haute",
    "address": "1324 Eagle St, Terre Haute, IN 47807",
    "phone": "(812) 624-5679",
    "email": None,  # No public email listed
    "services": [
        "Long-Term Residential Recovery",
        "Faith-Based Recovery Program",
        "Life Skills Training",
        "Peer Accountability",
        "Structured Recovery Environment"
    ],
    "eligibility_rules": {
        "requires_id": True,
        "requires_sobriety_commitment": True,
        "requires_faith_participation": True,
        "requires_assessment": False,
        "accepts_medicaid": False,
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
    faith_participation,
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
        "faith_participation": faith_participation,
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
def evaluate_member_for_teen_challenge(member):
    rules = TEEN_CHALLENGE_INFO["eligibility_rules"]
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

    # Faith participation requirement
    if rules["requires_faith_participation"] and not member["faith_participation"]:
        reasons.append("Faith participation required for program")

    # Insurance irrelevant for faith-based residential programs
    if member["insurance_type"] not in ["self_pay", None]:
        reasons.append("Insurance not applicable for this program")

    # Finalize
    member["intake_timestamp"] = "AUTO"
    member["eligible"] = len(reasons) == 0
    member["reasons"] = reasons

    return member

# Example usage
def demo():
    member = create_member_record(
        full_name="David Carter",
        age=34,
        has_id=True,
        sobriety_commitment=True,
        faith_participation=True,
        insurance_type="self_pay",
        assessment_complete=False,
        substance_type="opioids",
        homelessness_status=True,
        veteran_status=False
    )

    result = evaluate_member_for_teen_challenge(member)
    print(result)

if __name__ == "__main__":
    demo()
