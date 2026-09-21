# Beast System 3.0 – Substance Abuse Program Registry
# Registers all Terre Haute recovery programs for system-wide access.

from anabranch_member_intake_module import ANABRANCH_INFO, evaluate_member_for_anabranch
from hickory_member_intake_module import HICKORY_INFO, evaluate_member_for_hickory
from indiana_center_recovery_intake_module import ICR_INFO, evaluate_member_for_icr
from next_step_foundation_intake_module import NEXT_STEP_INFO, evaluate_member_for_next_step
from wabash_valley_teen_challenge_intake_module import TEEN_CHALLENGE_INFO, evaluate_member_for_teen_challenge
from wabash_valley_recovery_center_intake_module import WV_RECOVERY_INFO, evaluate_member_for_wv_recovery
from groups_recover_together_intake_module import GROUPS_INFO, evaluate_member_for_groups
from brightwing_recovery_intake_module import BRIGHTWING_INFO, evaluate_member_for_brightwing

PROGRAM_REGISTRY = {
    "anabranch": {
        "info": ANABRANCH_INFO,
        "eligibility_engine": evaluate_member_for_anabranch
    },
    "hickory": {
        "info": HICKORY_INFO,
        "eligibility_engine": evaluate_member_for_hickory
    },
    "indiana_center_recovery": {
        "info": ICR_INFO,
        "eligibility_engine": evaluate_member_for_icr
    },
    "next_step_foundation": {
        "info": NEXT_STEP_INFO,
        "eligibility_engine": evaluate_member_for_next_step
    },
    "teen_challenge": {
        "info": TEEN_CHALLENGE_INFO,
        "eligibility_engine": evaluate_member_for_teen_challenge
    },
    "wabash_valley_recovery_center": {
        "info": WV_RECOVERY_INFO,
        "eligibility_engine": evaluate_member_for_wv_recovery
    },
    "groups_recover_together": {
        "info": GROUPS_INFO,
        "eligibility_engine": evaluate_member_for_groups
    },
    "brightwing_recovery": {
        "info": BRIGHTWING_INFO,
        "eligibility_engine": evaluate_member_for_brightwing
    }
}

def get_program_list():
    return list(PROGRAM_REGISTRY.keys())

def get_program_info(program_name):
    return PROGRAM_REGISTRY.get(program_name, None)

def evaluate_member(program_name, member_record):
    program = PROGRAM_REGISTRY.get(program_name)
    if not program:
        return {"eligible": False, "reason": "Program not found"}
    return program["eligibility_engine"](member_record)

# Example usage
def demo():
    print("Registered Programs:")
    print(get_program_list())

if __name__ == "__main__":
    demo()
