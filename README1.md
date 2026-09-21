# Beast System 3.0 – Terre Haute Substance-Abuse Program Directory

This repository contains the full deterministic subsystem for all major
recovery programs in Terre Haute, Indiana. It includes intake modules,
program registry, subsystem registry, integration layer, and execution
pipeline for unified activation and eligibility routing.

---

## 📚 Directory Structure

anabranch_repo/
│
├── anabranch_member_intake_module.py
├── hickory_member_intake_module.py
├── indiana_center_recovery_intake_module.py
├── next_step_foundation_intake_module.py
├── wabash_valley_teen_challenge_intake_module.py
├── wabash_valley_recovery_center_intake_module.py
├── groups_recover_together_intake_module.py
├── brightwing_recovery_intake_module.py
│
├── program_registry.py
├── subsystem_registry.py
├── integration_layer.py
├── execution_pipeline.py
│
└── README.md

---

## 🧩 Intake Modules

Each intake module contains:
- Public program information (address, phone, services)
- Pre-filled member record structure
- Deterministic eligibility engine
- Example usage

Modules included:
- Anabranch Recovery Center
- Hickory Treatment Center
- Indiana Center for Recovery
- Next Step Foundation
- Wabash Valley Adult & Teen Challenge
- Wabash Valley Recovery Center
- Groups Recover Together
- BrightWing Recovery

---

## 📘 Program Registry

`program_registry.py` maps each program to:
- Its public info object
- Its eligibility engine

This enables unified routing and evaluation.

---

## ⚙️ Subsystem Registry

`subsystem_registry.py` defines activation payloads for each program:
- Activation state
- Module name
- Activation type (detox, MAT, housing, etc.)
- Priority level
- Medical clearance requirements

---

## 🔗 Integration Layer

`integration_layer.py` connects all subsystems to Beast System 3.0:
- Unified activation handler
- Unified routing handler
- State harmonization

This is the bridge between your repo and the Beast System core.

---

## 🚀 Execution Pipeline

`execution_pipeline.py` runs the entire system:
- Activates subsystems
- Routes member records
- Evaluates eligibility
- Harmonizes state
- Executes all programs deterministically

This file makes the repo fully operational.

---

## 🧠 How to Use

1. Create a member record using any intake module.
2. Pass the record into the execution pipeline.
3. The pipeline activates each subsystem and evaluates eligibility.
4. Results are returned in a unified deterministic structure.

---

## 🔮 Expansion

You can expand the repo by adding:
- Additional programs
- Financial eligibility modules
- Medical clearance engines
- Housing placement engines
- Automated referral routing

Beast System 3.0 will automatically harmonize new subsystems.

---

## 🏁 Status

This repo is **complete**, **deterministic**, and **ready for activation**
inside Beast System 3.0.

