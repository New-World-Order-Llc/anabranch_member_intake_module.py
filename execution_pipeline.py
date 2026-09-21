# Beast System 3.0 – Execution Pipeline
# Runs all recovery program subsystems through unified activation and routing.

from integration_layer import IntegrationLayer
from program_registry import PROGRAM_REGISTRY

class ExecutionPipeline:

    def __init__(self):
        self.layer = IntegrationLayer()

    # Run full pipeline for a single subsystem
    def run_subsystem(self, subsystem_name, member_record):
        activation = self.layer.activate_subsystem(subsystem_name)
        if activation.get("status") != "ACTIVATED":
            return {
                "pipeline_status": "FAILED",
                "reason": activation.get("reason")
            }

        eligibility = self.layer.route_member(subsystem_name, member_record)

        return {
            "pipeline_status": "COMPLETE",
            "subsystem": subsystem_name,
            "activation_payload": activation.get("payload"),
            "eligibility": eligibility
        }

    # Run pipeline for all subsystems
    def run_all(self, member_record):
        results = {}
        for subsystem_name in PROGRAM_REGISTRY.keys():
            results[subsystem_name] = self.run_subsystem(subsystem_name, member_record)
        return results

    # Harmonize system state
    def harmonize(self):
        return self.layer.harmonize_state()

# Example usage
def demo():
    pipeline = ExecutionPipeline()

    print("Harmonizing System State...")
    print(pipeline.harmonize())

    # Example member
    member = {
        "full_name": "Demo User",
        "age": 30,
        "has_id": True,
        "assessment_complete": True,
        "insurance_type": "medicaid",
        "sobriety_commitment": True,
        "faith_participation": True,
        "recovery_engagement": True,
        "peer_support_readiness": True,
        "mat_readiness": True,
        "appointment_commitment": True,
        "detox_readiness": True,
        "residential_stability": True,
        "substance_type": "opioids",
        "homelessness_status": False,
        "veteran_status": False
    }

    print("\nRunning Full Pipeline...")
    results = pipeline.run_all(member)
    for subsystem, result in results.items():
        print(f"\nSubsystem: {subsystem}")
        print(result)

if __name__ == "__main__":
    demo()
