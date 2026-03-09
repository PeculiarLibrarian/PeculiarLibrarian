# 🚨 PADI Embassy: System Recovery Protocol

This document provides the instructions for a **Full Global Fleet Resynchronization**. Use these procedures if the GitHub UI is unresponsive, if agents appear out of sync, or if a platform-wide update requires a hard reset of the Alpha-9 units.

## 1. Global Fleet Re-sync (The 60-Second Recovery)
This command forces all 6 geographic units (AU, DE, NL, UK, CH, MENA) to redeploy their logic simultaneously.

### Command:
```bash
gh workflow run triage.yml -f reason="Full Global Fleet Resynchronization"
