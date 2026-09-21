# Wabash Valley Recovery Center – Member Intake Module
# Publicly listable information (no permission required)

WV_RECOVERY_INFO = {
    "name": "Wabash Valley Recovery Center – Terre Haute",
    "address": "1096 Ohio St, Terre Haute, IN 47807",
    "phone": "(812) 917-0068",
    "email": None,  # No public email listed
    "services": [
        "Peer Recovery Support",
        "Harm Reduction Services",
        "Community Recovery Resources",
        "Recovery Coaching",
        "Support Groups"
    ],
    "eligibility_rules": {
        "requires_id": False,
        "requires_recovery_engagement": True,
        "requires_peer_support_readiness": True,
        "requires_assessment": False,
        "accepts_medicaid": False,
        "accepts_private_insurance": False,
        "accepts_self_pay": False,  # Free community program
        "age_min": 18
    }
}

# Pre-filled member structure
def create_member_record(
    full_name,
    age,
    has_id,
    recovery_engagement,
    peer_support_readiness,
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
        "recovery_engagement": recovery_engagement,
        "peer_support_readiness": peer_support_readiness,
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
def evaluate_member_for_wv_recovery(member):
    rules = WV_RECOVERY_INFO["eligibility_rules"]
    reasons = []

    # Age requirement
    if member["age"] < rules["age_min"]:
        reasons.append("Must be 18 or older")

    # Recovery engagement requirement
    if rules["requires_recovery_engagement"] and not member["recovery_engagement"]:
        reasons.append("Must be actively engaged in recovery")

    # Peer support readiness requirement
    if rules["requires_peer_support_readiness"] and not member["peer_support_readiness"]:
        reasons.append("Must be ready for peer support participation")

    # Insurance irrelevant (program is free)
    if member["insurance_type"] not in [None, "none"]:
        reasons.append("Insurance not applicable for free community program")

    # Finalize
    member["intake_timestamp"] = "AUTO"
    member["eligible"] = len(reasons) == 0
    member["reasons"] = reasons

    return member

# Example usage
def demo():
    member = create_member_record(
        full_name="Alex Ramirez",
        age=30,
        has_id=False,
        recovery_engagement=True,
        peer_support_readiness=True,
        insurance_type=None,
        assessment_complete=False,
        substance_type="alcohol",
        homelessness_status=False,
        veteran_status=False
    )

    result = evaluate_member_for_wv_recovery(member)
    print(result)

if __name__ == "__main__":
    demo()
