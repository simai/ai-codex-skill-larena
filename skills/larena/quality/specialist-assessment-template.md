# Specialist Assessment Template

```json
{
  "specialist": "qa-validation",
  "status": "approved_with_conditions",
  "summary": "Primary conclusion in 1-2 sentences.",
  "findings": [
    {
      "severity": "medium",
      "issue": "What is wrong or risky.",
      "recommendation": "What should be changed or verified."
    }
  ],
  "acceptance": {
    "passed": true,
    "missing": []
  }
}
```

Allowed statuses: `approved`, `approved_with_conditions`, `needs_revision`, `rejected`.

Severity values: `critical`, `high`, `medium`, `low`.
