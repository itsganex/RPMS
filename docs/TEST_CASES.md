# Test Cases

| ID | Scenario | Expected result |
|---|---|---|
| TC01 | Register candidate with valid unique email/mobile | Candidate saved |
| TC02 | Duplicate candidate email | Database rejects duplicate |
| TC03 | Duplicate candidate mobile | Database rejects duplicate |
| TC04 | Percentage below 0 or above 100 | Validation rejects |
| TC05 | Negative backlog count | Validation rejects |
| TC06 | Create company with required details | Company saved |
| TC07 | Create job with openings 0 | Validation rejects |
| TC08 | Minimum package exceeds maximum | Validation rejects |
| TC09 | Deadline earlier than posted date | Validation rejects |
| TC10 | Eligible active candidate applies to open job | Application created |
| TC11 | Candidate applies to same job twice | Duplicate blocked |
| TC12 | Candidate fails percentage/qualification/technology rule | NOT_ELIGIBLE with reason |
| TC13 | APPLIED transitions directly to JOINED | Invalid transition rejected |
| TC14 | Schedule same application round twice | Unique constraint rejects |
| TC15 | Add feedback twice to same interview | Unique constraint rejects |
| TC16 | Create offer for non-selected application | Service rejects |
| TC17 | Create offer for selected application | Offer and history committed together |
| TC18 | Confirm joining for accepted offer | Placement and status updates committed |
| TC19 | Confirm joining for unaccepted offer | Service rejects |
| TC20 | Run reports | Results are calculated from MySQL |

Run `pytest -q` from the project root. The test suite contains isolated unit tests for workflow and validation logic; database integration cases require a configured MySQL instance and seeded database.
