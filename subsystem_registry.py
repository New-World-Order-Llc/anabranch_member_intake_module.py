# Beast System 3.0 – Subsystem Registry
# Defines activation payloads for all Terre Haute recovery programs.

SUBSYSTEM_REGISTRY = {
    "anabranch": {
        "activation_state": "READY",
        "module": "anabranch_member_intake_module",
        "activation_payload": {
            "type": "detox_residential",
            "priority": 1,
            "requires_medical_clearance": True
        }
    },
    "hickory": {
        "activation_state": "READY",
        "module": "hickory_member_intake_module",
        "activation_payload": {
            "type": "residential_mat",
            "priority": 1,
            "requires_medical_clearance": True
        }
    },
    "indiana_center_recovery": {
        "activation_state": "READY",
        "module": "indiana_center_recovery_intake_module",
        "activation_payload": {
            "type": "detox_inpatient_outpatient",
            "priority": 1,
            "requires_medical_clearance": True
        }
    },
    "next_step_foundation": {
        "activation_state": "READY",
        "module": "next_step_foundation_intake_module",
        "activation_payload": {
            "type": "housing_sober_living",
            "priority": 2,
            "requires_medical_clearance": False
        }
    },
    "teen_challenge": {
        "activation_state": "READY",
        "module": "wabash_valley_teen_challenge_intake_module",
        "activation_payload": {
            "type": "faith_based_residential",
            "priority": 2,
            "requires_medical_clearance": False
        }
    },
    "wabash_valley_recovery_center": {
        "activation_state": "READY",
        "module": "wabash_valley_recovery_center_intake_module",
        "activation_payload": {
            "type": "peer_support_harm_reduction",
            "priority": 3,
            "requires_medical_clearance": False
        }
    },
    "groups_recover_together": {
        "activation_state": "READY",
        "module": "groups_recover_together_intake_module",
        "activation_payload": {
            "type": "mat_suboxone",
            "priority": 1,
            "requires_medical_clearance": True
        }
    },
    "brightwing_recovery": {
        "activation_state": "READY",
        "module": "brightwing_recovery_intake_module",
        "activation_payload": {
            "type": "detox_residential_clinical",
            "priority": 1,
            "requires_medical_clearance": True
        }
    }
}

def get_subsystem_list():
    return list(SUBSYSTEM_REGISTRY.keys())

def get_activation_payload(subsystem_name):
    return SUBSYSTEM_REGISTRY.get(subsystem_name, None)

# Example usage
def demo():
    print("Registered Subsystems:")
    print(get_subsystem_list())

if __name__ == "__main__":
    demo()
