# AI-Driven SRE Automation: Self-Improvement Lifecycle

This repository demonstrates a fully autonomous, AI-driven software development and infrastructure lifecycle. It serves as a technical showcase for automating code maintenance, documentation, and real-world validation using ephemeral infrastructure.

---

## 📖 Project Context
As part of an advanced SRE technical demonstration initiated in **May 2026**, this project explores the boundaries of "Self-Healing" and "Self-Improving" systems. The goal is to minimize manual intervention in the standard SDLC (Software Development Life Cycle) by offloading refactoring and documentation tasks to a managed AI agent.

## 🏗 System Architecture

The solution implements a **5-stage pipeline** orchestrated via GitHub Actions, designed for high resilience and cost-efficiency.

1.  **AI Enhancement Stage**: A custom Python agent (Anthropic Claude API) scans the codebase, optimizes logic, and enforces English-only standards.
2.  **Git-based Communication**: Uses a temporary branch `ai-improved-code` as a data transport to bypass platform-level artifact storage instabilities.
3.  **Dynamic Provisioning**: A Bash-based script utilizes the `hcloud` CLI to spin up an ephemeral VPS in the **nbg1** region.
4.  **Ephemeral Validation**: Executes the `pytest` suite on the freshly provisioned Hetzner VPS, handling PEP 668 restrictions for Ubuntu 24.04.
5.  **Deployment & Cleanup**: Merges verified code into `main` and destroys the VPS to ensure zero infrastructure persistence and minimal costs.

---

## 📂 Project Structure

| Directory / File | Description | Role in the Lifecycle |
| :--- | :--- | :--- |
| **`app/`** | Core application source code. | Target for AI refactoring and optimization. |
| **`agent/`** | AI Agent logic (Anthropic Claude). | Scans code, generates improvements, and creates docs. |
| **`infra/`** | Infrastructure-as-Code (Bash, Hetzner CLI). | Provisions ephemeral VPS and registers runners. |
| **`tests/`** | Python test suite (`pytest`). | Validates AI-modified code on real infrastructure. |
| **`.github/workflows/`** | GitHub Actions YAML definitions. | Orchestrates the entire 5-stage SRE pipeline. |
| **`CHANGELOG.md`** | Automated record of system changes. | Provides observability and audit trail for AI actions. |
| **`requirements.txt`** | Project dependencies. | Environment setup for both Agent and Runner. |
| **`.commit_msg`** | Temporary metadata storage. | Stores AI-generated detailed Git commit logs. |

---

## 🛠 Technical Stack
*   **Cloud**: Hetzner Cloud (Infrastructure as Code via CLI).
*   **CI/CD**: GitHub Actions.
*   **AI Engine**: Anthropic Claude.
*   **Programming**: Python 3.11+ (FastAPI, SQLModel focus).
*   **Automation**: Bash & GitOps workflows.

## 📈 Key Engineering Achievements
*   **Resiliency**: Successfully pivoted from Artifacts to a Git-based transport layer during major GitHub service disruptions.
*   **Observability as Code**: Automated maintenance of `CHANGELOG.md` and project documentation.
*   **Cost Management**: Implemented a "Zero-Waste" infrastructure policy, ensuring temporary resources are destroyed after validation.

---
**Author**: Vasyl Poliakov, DevOps & Site Reliability Engineer.