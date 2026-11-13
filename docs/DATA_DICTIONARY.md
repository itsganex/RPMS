# Data Dictionary

The complete field-level definitions and constraints are authoritative in `sql/database_schema.sql`.

| Table | Purpose | Primary key |
|---|---|---|
| roles | Role master | role_id |
| users | Authorized users and password hashes | user_id |
| candidates | Candidate profile and academics | candidate_id |
| skills | Skill/technology master | skill_id |
| candidate_skills | Candidate-skill mapping | candidate_skill_id |
| companies | Hiring company master | company_id |
| jobs | Job openings and criteria | job_id |
| job_skills | Job-skill mapping | job_skill_id |
| applications | Candidate applications | application_id |
| application_history | Status audit trail | history_id |
| interview_rounds | Interview rounds | interview_id |
| interview_feedback | Interview evaluation | feedback_id |
| offers | Offer lifecycle | offer_id |
| placements | Joining and placement | placement_id |
| activity_logs | System activity audit | activity_id |
| qualifications | Qualification master | qualification_id |
| locations | Location master | location_id |
