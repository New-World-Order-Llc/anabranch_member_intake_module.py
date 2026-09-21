# Beast System 3.0 – Integration Layer
# Connects all recovery program subsystems to the Beast System core.

from program_registry import PROGRAM_REGISTRY
from subsystem_registry import SUBSYSTEM_REGISTRY

class IntegrationLayer:

    def __init__(self):
        self.programs = PROGRAM_REGISTRY
        self.subsystems = SUBSYSTEM_REGISTRY

    # Unified activation handler
    def activate_subsystem(self, subsystem_name):
        subsystem = self.subsystems.get(subsystem_name)
        if not subsystem:
            return {"status": "ERROR", "reason": "Subsystem not found"}

        if subsystem["activation_state"] != "READY":
            return {"status": "ERROR", "reason": "Subsystem not ready"}

        payload = subsystem["activation_payload"]

        return {
            "status": "ACTIVATED",
            "subsystem": subsystem_name,
            "payload": payload
        }

    # Unified routing handler
    def route_member(self, subsystem_name, member_record):
        program = self.programs.get(subsystem_name)
        if not program:
            return {"eligible": False, "reason": "Program not found"}

        engine = program["eligibility_engine"]
        return engine(member_record)

    # Unified state harmonization
    def harmonize_state(self):
        return {
            "status": "HARMONIZED",
            "program_count": len(self.programs),
            "subsystem_count": len(self.subsystems)
        }

# Example usage
def demo():
    layer = IntegrationLayer()

    print("Harmonizing System State...")
    print(layer.harmonize_state())

    print("\nActivating Anabranch...")
    print(layer.activate_subsystem("anabranch"))

    print("\nListing Registered Subsystems...")
    print(list(SUBSYSTEM_REGISTRY.keys()))

if __name__ == "__main__":
    demo()
