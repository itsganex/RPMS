USE rpms_db;

INSERT INTO roles(role_id,role_code,role_name) VALUES (1,'ADMIN','Administrator'),(2,'RECRUITER','Recruiter'),(3,'PLACEMENT_OFFICER','Placement Officer'),(4,'STUDENT','Student') ON DUPLICATE KEY UPDATE role_name=VALUES(role_name);

INSERT INTO users(username,password_hash,full_name,email,role_id) VALUES
('admin','pbkdf2:sha256:600000$rpms-demo-salt$46eb93361ad2ed120deffa362ab0e4f45b71e3fee1572327b6bc8f8b43d8bbe7','System Admin','admin@rpms.local',1),
('recruiter1','pbkdf2:sha256:600000$rpms-demo-salt$46eb93361ad2ed120deffa362ab0e4f45b71e3fee1572327b6bc8f8b43d8bbe7','Aarav Sharma','aarav@rpms.local',2),
('recruiter2','pbkdf2:sha256:600000$rpms-demo-salt$46eb93361ad2ed120deffa362ab0e4f45b71e3fee1572327b6bc8f8b43d8bbe7','Meera Joshi','meera@rpms.local',2),
('placement','pbkdf2:sha256:600000$rpms-demo-salt$46eb93361ad2ed120deffa362ab0e4f45b71e3fee1572327b6bc8f8b43d8bbe7','Placement Officer','placement@rpms.local',3),
('recruiter3','pbkdf2:sha256:600000$rpms-demo-salt$46eb93361ad2ed120deffa362ab0e4f45b71e3fee1572327b6bc8f8b43d8bbe7','Rohan Patil','rohan@rpms.local',2);

INSERT INTO skills(skill_name,category) VALUES ('Python','Programming'),('Java','Programming'),('SQL','Database'),('HTML','Web'),('CSS','Web'),('JavaScript','Web'),('React','Web'),('Flask','Framework'),('MySQL','Database'),('Git','Tools');

INSERT INTO qualifications(qualification_name) VALUES ('B.Tech'),('BE'),('MCA'),('BCA'),('M.Sc Computer Science');

INSERT INTO locations(location_name,state_name) VALUES ('Pune','Maharashtra'),('Mumbai','Maharashtra'),('Nashik','Maharashtra'),('Nagpur','Maharashtra'),('Bengaluru','Karnataka'),('Hyderabad','Telangana');

INSERT INTO companies(company_name,industry,website,location,company_type,hr_name,hr_email,hr_mobile) VALUES ('TCS','IT Services','https://www.tcs.com','Pune','MNC','HR Team','hr1@company.local','9000000001'),('Infosys','IT Services','https://www.infosys.com','Pune','MNC','HR Team','hr2@company.local','9000000002'),('Persistent Systems','Software','https://www.persistent.com','Pune','MID_SIZE','HR Team','hr3@company.local','9000000003'),('Tech Mahindra','IT Services','https://www.techmahindra.com','Pune','MNC','HR Team','hr4@company.local','9000000004'),('Zensar Technologies','IT Services','https://www.zensar.com','Pune','MID_SIZE','HR Team','hr5@company.local','9000000005'),('QuickHeal','Cybersecurity','https://www.quickheal.com','Pune','MID_SIZE','HR Team','hr6@company.local','9000000006'),('Freshworks','SaaS','https://www.freshworks.com','Bengaluru','MNC','HR Team','hr7@company.local','9000000007'),('CloudThat','Cloud Services','https://www.cloudthat.com','Mumbai','STARTUP','HR Team','hr8@company.local','9000000008');

INSERT INTO candidates(candidate_code,full_name,email,mobile,date_of_birth,gender,qualification,college,university,passing_year,percentage,cgpa,backlog_count,primary_technology,current_location,preferred_location,profile_status,placement_status) VALUES
('CAN-2026-0001','Aarav Patil','candidate1@mail.local','919000000000', '2004-05-15','Other','B.Tech','Ahinsa Institute of Technology','DBATU',2024,68.50,6.20,0,'Python','Dhule','Pune','ACTIVE','NOT_PLACED'),
('CAN-2026-0002','Vivaan Sharma','candidate2@mail.local','919000000001', '2004-05-15','Other','B.Tech','Ahinsa Institute of Technology','DBATU',2025,69.50,7.20,1,'Java','Dhule','Pune','ACTIVE','NOT_PLACED'),
('CAN-2026-0003','Aditya Joshi','candidate3@mail.local','919000000002', '2004-05-15','Other','B.Tech','Ahinsa Institute of Technology','DBATU',2026,70.50,8.20,2,'JavaScript','Dhule','Pune','ACTIVE','NOT_PLACED'),
('CAN-2026-0004','Vihaan Kulkarni','candidate4@mail.local','919000000003', '2004-05-15','Other','B.Tech','Ahinsa Institute of Technology','DBATU',2024,71.50,6.20,0,'Python','Dhule','Pune','ACTIVE','NOT_PLACED'),
('CAN-2026-0005','Arjun Deshmukh','candidate5@mail.local','919000000004', '2004-05-15','Other','B.Tech','Ahinsa Institute of Technology','DBATU',2025,72.50,7.20,1,'Java','Dhule','Pune','ACTIVE','NOT_PLACED'),
('CAN-2026-0006','Sai More','candidate6@mail.local','919000000005', '2004-05-15','Other','B.Tech','Ahinsa Institute of Technology','DBATU',2026,73.50,8.20,2,'Python','Dhule','Pune','ACTIVE','NOT_PLACED'),
('CAN-2026-0007','Reyansh Pawar','candidate7@mail.local','919000000006', '2004-05-15','Other','B.Tech','Ahinsa Institute of Technology','DBATU',2024,74.50,6.20,0,'Java','Dhule','Pune','ACTIVE','NOT_PLACED'),
('CAN-2026-0008','Ayaan Jadhav','candidate8@mail.local','919000000007', '2004-05-15','Other','B.Tech','Ahinsa Institute of Technology','DBATU',2025,75.50,7.20,1,'JavaScript','Dhule','Pune','ACTIVE','NOT_PLACED'),
('CAN-2026-0009','Krishna Shinde','candidate9@mail.local','919000000008', '2004-05-15','Other','B.Tech','Ahinsa Institute of Technology','DBATU',2026,76.50,8.20,2,'Python','Dhule','Pune','ACTIVE','NOT_PLACED'),
('CAN-2026-0010','Ishaan Chavan','candidate10@mail.local','919000000009', '2004-05-15','Other','B.Tech','Ahinsa Institute of Technology','DBATU',2024,77.50,6.20,0,'Java','Dhule','Pune','ACTIVE','NOT_PLACED'),
('CAN-2026-0011','Ananya Patil','candidate11@mail.local','919000000010', '2004-05-15','Other','B.Tech','Ahinsa Institute of Technology','DBATU',2025,78.50,7.20,1,'Python','Dhule','Pune','ACTIVE','NOT_PLACED'),
('CAN-2026-0012','Diya Sharma','candidate12@mail.local','919000000011', '2004-05-15','Other','B.Tech','Ahinsa Institute of Technology','DBATU',2026,79.50,8.20,2,'Java','Dhule','Pune','ACTIVE','NOT_PLACED'),
('CAN-2026-0013','Saanvi Joshi','candidate13@mail.local','919000000012', '2004-05-15','Other','B.Tech','Ahinsa Institute of Technology','DBATU',2024,80.50,6.20,0,'JavaScript','Dhule','Pune','ACTIVE','NOT_PLACED'),
('CAN-2026-0014','Aadhya Kulkarni','candidate14@mail.local','919000000013', '2004-05-15','Other','B.Tech','Ahinsa Institute of Technology','DBATU',2025,81.50,7.20,1,'Python','Dhule','Pune','ACTIVE','NOT_PLACED'),
('CAN-2026-0015','Pari Deshmukh','candidate15@mail.local','919000000014', '2004-05-15','Other','B.Tech','Ahinsa Institute of Technology','DBATU',2026,82.50,8.20,2,'Java','Dhule','Pune','ACTIVE','NOT_PLACED'),
('CAN-2026-0016','Meera More','candidate16@mail.local','919000000015', '2004-05-15','Other','B.Tech','Ahinsa Institute of Technology','DBATU',2024,83.50,6.20,0,'Python','Dhule','Pune','ACTIVE','NOT_PLACED'),
('CAN-2026-0017','Ira Pawar','candidate17@mail.local','919000000016', '2004-05-15','Other','B.Tech','Ahinsa Institute of Technology','DBATU',2025,84.50,7.20,1,'Java','Dhule','Pune','ACTIVE','NOT_PLACED'),
('CAN-2026-0018','Riya Jadhav','candidate18@mail.local','919000000017', '2004-05-15','Other','B.Tech','Ahinsa Institute of Technology','DBATU',2026,85.50,8.20,2,'JavaScript','Dhule','Pune','ACTIVE','NOT_PLACED'),
('CAN-2026-0019','Anika Shinde','candidate19@mail.local','919000000018', '2004-05-15','Other','B.Tech','Ahinsa Institute of Technology','DBATU',2024,86.50,6.20,0,'Python','Dhule','Pune','ACTIVE','NOT_PLACED'),
('CAN-2026-0020','Kavya Chavan','candidate20@mail.local','919000000019', '2004-05-15','Other','B.Tech','Ahinsa Institute of Technology','DBATU',2025,87.50,7.20,1,'Java','Dhule','Pune','ACTIVE','NOT_PLACED'),
('CAN-2026-0021','Om Patil','candidate21@mail.local','919000000020', '2004-05-15','Other','B.Tech','Ahinsa Institute of Technology','DBATU',2026,88.50,8.20,2,'Python','Dhule','Pune','ACTIVE','NOT_PLACED'),
('CAN-2026-0022','Atharva Sharma','candidate22@mail.local','919000000021', '2004-05-15','Other','B.Tech','Ahinsa Institute of Technology','DBATU',2024,89.50,6.20,0,'Java','Dhule','Pune','ACTIVE','NOT_PLACED'),
('CAN-2026-0023','Vedant Joshi','candidate23@mail.local','919000000022', '2004-05-15','Other','B.Tech','Ahinsa Institute of Technology','DBATU',2025,90.50,7.20,1,'JavaScript','Dhule','Pune','ACTIVE','NOT_PLACED'),
('CAN-2026-0024','Rudra Kulkarni','candidate24@mail.local','919000000023', '2004-05-15','Other','B.Tech','Ahinsa Institute of Technology','DBATU',2026,91.50,8.20,2,'Python','Dhule','Pune','ACTIVE','NOT_PLACED'),
('CAN-2026-0025','Tanmay Deshmukh','candidate25@mail.local','919000000024', '2004-05-15','Other','B.Tech','Ahinsa Institute of Technology','DBATU',2024,92.50,6.20,0,'Java','Dhule','Pune','ACTIVE','NOT_PLACED'),
('CAN-2026-0026','Pranav More','candidate26@mail.local','919000000025', '2004-05-15','Other','B.Tech','Ahinsa Institute of Technology','DBATU',2025,68.50,7.20,1,'Python','Dhule','Pune','ACTIVE','NOT_PLACED'),
('CAN-2026-0027','Siddhi Pawar','candidate27@mail.local','919000000026', '2004-05-15','Other','B.Tech','Ahinsa Institute of Technology','DBATU',2026,69.50,8.20,2,'Java','Dhule','Pune','ACTIVE','NOT_PLACED'),
('CAN-2026-0028','Neha Jadhav','candidate28@mail.local','919000000027', '2004-05-15','Other','B.Tech','Ahinsa Institute of Technology','DBATU',2024,70.50,6.20,0,'JavaScript','Dhule','Pune','INACTIVE','NOT_PLACED'),
('CAN-2026-0029','Pooja Shinde','candidate29@mail.local','919000000028', '2004-05-15','Other','B.Tech','Ahinsa Institute of Technology','DBATU',2025,71.50,7.20,1,'Python','Dhule','Pune','ACTIVE','NOT_PLACED'),
('CAN-2026-0030','Rohan Chavan','candidate30@mail.local','919000000029', '2004-05-15','Other','B.Tech','Ahinsa Institute of Technology','DBATU',2026,72.50,8.20,2,'Java','Dhule','Pune','ACTIVE','NOT_PLACED');

INSERT INTO candidate_skills(candidate_id,skill_id,skill_level,is_primary) SELECT c.candidate_id,s.skill_id,'INTERMEDIATE',1 FROM candidates c JOIN skills s ON s.skill_name=c.primary_technology;

INSERT INTO jobs(company_id,job_code,job_title,openings,employment_type,location,min_package,max_package,qualification,min_percentage,min_passing_year,max_passing_year,max_backlogs,experience_required,required_technology,posted_date,application_deadline,job_status,created_by) VALUES
(1,'JOB-2026-001','Python Developer', 2,'FULL_TIME','Pune',3.00,6.00,'B.Tech',60.00,2024,2027,2,'FRESHER','Python','2026-10-01','2026-12-31','OPEN',2),
(2,'JOB-2026-002','Java Developer', 3,'FULL_TIME','Pune',4.00,7.00,'B.Tech',60.00,2024,2027,2,'FRESHER','Java','2026-10-01','2026-12-31','OPEN',2),
(3,'JOB-2026-003','JavaScript Developer', 4,'FULL_TIME','Pune',5.00,8.00,'B.Tech',60.00,2024,2027,2,'FRESHER','JavaScript','2026-10-01','2026-12-31','OPEN',2),
(4,'JOB-2026-004','Python Developer', 5,'FULL_TIME','Pune',3.00,9.00,'B.Tech',60.00,2024,2027,2,'FRESHER','Python','2026-10-01','2026-12-31','OPEN',2),
(5,'JOB-2026-005','Java Developer', 6,'FULL_TIME','Pune',4.00,6.00,'B.Tech',60.00,2024,2027,2,'FRESHER','Java','2026-10-01','2026-12-31','OPEN',2),
(6,'JOB-2026-006','JavaScript Developer', 2,'FULL_TIME','Pune',5.00,7.00,'B.Tech',60.00,2024,2027,2,'FRESHER','JavaScript','2026-10-01','2026-12-31','OPEN',2),
(7,'JOB-2026-007','Python Developer', 3,'FULL_TIME','Pune',3.00,8.00,'B.Tech',60.00,2024,2027,2,'FRESHER','Python','2026-10-01','2026-12-31','OPEN',2),
(8,'JOB-2026-008','Java Developer', 4,'FULL_TIME','Pune',4.00,9.00,'B.Tech',60.00,2024,2027,2,'FRESHER','Java','2026-10-01','2026-12-31','OPEN',2),
(1,'JOB-2026-009','JavaScript Developer', 5,'FULL_TIME','Pune',5.00,6.00,'B.Tech',60.00,2024,2027,2,'FRESHER','JavaScript','2026-10-01','2026-12-31','OPEN',2),
(2,'JOB-2026-010','Python Developer', 6,'FULL_TIME','Pune',3.00,7.00,'B.Tech',60.00,2024,2027,2,'FRESHER','Python','2026-10-01','2026-12-31','CLOSED',2),
(3,'JOB-2026-011','Java Developer', 2,'FULL_TIME','Pune',4.00,8.00,'B.Tech',60.00,2024,2027,2,'FRESHER','Java','2026-10-01','2026-12-31','CLOSED',2),
(4,'JOB-2026-012','JavaScript Developer', 3,'FULL_TIME','Pune',5.00,9.00,'B.Tech',60.00,2024,2027,2,'FRESHER','JavaScript','2026-10-01','2026-12-31','CLOSED',2);

INSERT INTO job_skills(job_id,skill_id,mandatory_flag) SELECT j.job_id,s.skill_id,1 FROM jobs j JOIN skills s ON s.skill_name=j.required_technology;

INSERT INTO applications(application_code,candidate_id,job_id,eligibility_status,eligibility_reason,application_status,applied_at,assigned_recruiter_id) VALUES
('APP-2026-001',1,1,'ELIGIBLE','Meets configured sample criteria','APPLIED',DATE_SUB(NOW(),INTERVAL 0 DAY),3),
('APP-2026-002',2,2,'ELIGIBLE','Meets configured sample criteria','ELIGIBILITY_VERIFIED',DATE_SUB(NOW(),INTERVAL 1 DAY),2),
('APP-2026-003',3,3,'ELIGIBLE','Meets configured sample criteria','SHORTLISTED',DATE_SUB(NOW(),INTERVAL 2 DAY),2),
('APP-2026-004',4,4,'ELIGIBLE','Meets configured sample criteria','INTERVIEW_SCHEDULED',DATE_SUB(NOW(),INTERVAL 3 DAY),3),
('APP-2026-005',5,5,'ELIGIBLE','Meets configured sample criteria','INTERVIEWED',DATE_SUB(NOW(),INTERVAL 4 DAY),2),
('APP-2026-006',6,6,'ELIGIBLE','Meets configured sample criteria','SELECTED',DATE_SUB(NOW(),INTERVAL 5 DAY),2),
('APP-2026-007',7,7,'ELIGIBLE','Meets configured sample criteria','REJECTED',DATE_SUB(NOW(),INTERVAL 6 DAY),3),
('APP-2026-008',8,8,'ELIGIBLE','Meets configured sample criteria','OFFERED',DATE_SUB(NOW(),INTERVAL 7 DAY),2),
('APP-2026-009',9,9,'ELIGIBLE','Meets configured sample criteria','JOINED',DATE_SUB(NOW(),INTERVAL 8 DAY),2),
('APP-2026-010',10,1,'ELIGIBLE','Meets configured sample criteria','WITHDRAWN',DATE_SUB(NOW(),INTERVAL 9 DAY),3),
('APP-2026-011',11,2,'ELIGIBLE','Meets configured sample criteria','APPLIED',DATE_SUB(NOW(),INTERVAL 10 DAY),2),
('APP-2026-012',12,3,'ELIGIBLE','Meets configured sample criteria','ELIGIBILITY_VERIFIED',DATE_SUB(NOW(),INTERVAL 11 DAY),2),
('APP-2026-013',13,4,'ELIGIBLE','Meets configured sample criteria','SHORTLISTED',DATE_SUB(NOW(),INTERVAL 12 DAY),3),
('APP-2026-014',14,5,'ELIGIBLE','Meets configured sample criteria','INTERVIEW_SCHEDULED',DATE_SUB(NOW(),INTERVAL 13 DAY),2),
('APP-2026-015',15,6,'ELIGIBLE','Meets configured sample criteria','INTERVIEWED',DATE_SUB(NOW(),INTERVAL 14 DAY),2),
('APP-2026-016',16,7,'ELIGIBLE','Meets configured sample criteria','SELECTED',DATE_SUB(NOW(),INTERVAL 15 DAY),3),
('APP-2026-017',17,8,'ELIGIBLE','Meets configured sample criteria','REJECTED',DATE_SUB(NOW(),INTERVAL 16 DAY),2),
('APP-2026-018',18,9,'ELIGIBLE','Meets configured sample criteria','OFFERED',DATE_SUB(NOW(),INTERVAL 17 DAY),2),
('APP-2026-019',19,1,'ELIGIBLE','Meets configured sample criteria','JOINED',DATE_SUB(NOW(),INTERVAL 18 DAY),3),
('APP-2026-020',20,2,'ELIGIBLE','Meets configured sample criteria','WITHDRAWN',DATE_SUB(NOW(),INTERVAL 19 DAY),2),
('APP-2026-021',21,3,'ELIGIBLE','Meets configured sample criteria','APPLIED',DATE_SUB(NOW(),INTERVAL 20 DAY),2),
('APP-2026-022',22,4,'ELIGIBLE','Meets configured sample criteria','ELIGIBILITY_VERIFIED',DATE_SUB(NOW(),INTERVAL 21 DAY),3),
('APP-2026-023',23,5,'ELIGIBLE','Meets configured sample criteria','SHORTLISTED',DATE_SUB(NOW(),INTERVAL 22 DAY),2),
('APP-2026-024',24,6,'ELIGIBLE','Meets configured sample criteria','INTERVIEW_SCHEDULED',DATE_SUB(NOW(),INTERVAL 23 DAY),2),
('APP-2026-025',25,7,'ELIGIBLE','Meets configured sample criteria','INTERVIEWED',DATE_SUB(NOW(),INTERVAL 24 DAY),3),
('APP-2026-026',26,8,'ELIGIBLE','Meets configured sample criteria','SELECTED',DATE_SUB(NOW(),INTERVAL 25 DAY),2),
('APP-2026-027',27,9,'ELIGIBLE','Meets configured sample criteria','REJECTED',DATE_SUB(NOW(),INTERVAL 26 DAY),2),
('APP-2026-028',28,1,'ELIGIBLE','Meets configured sample criteria','OFFERED',DATE_SUB(NOW(),INTERVAL 27 DAY),3),
('APP-2026-029',29,2,'ELIGIBLE','Meets configured sample criteria','JOINED',DATE_SUB(NOW(),INTERVAL 28 DAY),2),
('APP-2026-030',30,3,'ELIGIBLE','Meets configured sample criteria','WITHDRAWN',DATE_SUB(NOW(),INTERVAL 29 DAY),2),
('APP-2026-031',1,4,'ELIGIBLE','Meets configured sample criteria','APPLIED',DATE_SUB(NOW(),INTERVAL 30 DAY),3),
('APP-2026-032',2,5,'ELIGIBLE','Meets configured sample criteria','ELIGIBILITY_VERIFIED',DATE_SUB(NOW(),INTERVAL 31 DAY),2),
('APP-2026-033',3,6,'ELIGIBLE','Meets configured sample criteria','SHORTLISTED',DATE_SUB(NOW(),INTERVAL 32 DAY),2),
('APP-2026-034',4,7,'ELIGIBLE','Meets configured sample criteria','INTERVIEW_SCHEDULED',DATE_SUB(NOW(),INTERVAL 33 DAY),3),
('APP-2026-035',5,8,'ELIGIBLE','Meets configured sample criteria','INTERVIEWED',DATE_SUB(NOW(),INTERVAL 34 DAY),2),
('APP-2026-036',6,9,'ELIGIBLE','Meets configured sample criteria','SELECTED',DATE_SUB(NOW(),INTERVAL 35 DAY),2),
('APP-2026-037',7,1,'ELIGIBLE','Meets configured sample criteria','REJECTED',DATE_SUB(NOW(),INTERVAL 36 DAY),3),
('APP-2026-038',8,2,'ELIGIBLE','Meets configured sample criteria','OFFERED',DATE_SUB(NOW(),INTERVAL 37 DAY),2),
('APP-2026-039',9,3,'ELIGIBLE','Meets configured sample criteria','JOINED',DATE_SUB(NOW(),INTERVAL 38 DAY),2),
('APP-2026-040',10,4,'ELIGIBLE','Meets configured sample criteria','WITHDRAWN',DATE_SUB(NOW(),INTERVAL 39 DAY),3),
('APP-2026-041',11,5,'ELIGIBLE','Meets configured sample criteria','APPLIED',DATE_SUB(NOW(),INTERVAL 40 DAY),2),
('APP-2026-042',12,6,'ELIGIBLE','Meets configured sample criteria','ELIGIBILITY_VERIFIED',DATE_SUB(NOW(),INTERVAL 41 DAY),2),
('APP-2026-043',13,7,'ELIGIBLE','Meets configured sample criteria','SHORTLISTED',DATE_SUB(NOW(),INTERVAL 42 DAY),3),
('APP-2026-044',14,8,'ELIGIBLE','Meets configured sample criteria','INTERVIEW_SCHEDULED',DATE_SUB(NOW(),INTERVAL 43 DAY),2),
('APP-2026-045',15,9,'ELIGIBLE','Meets configured sample criteria','INTERVIEWED',DATE_SUB(NOW(),INTERVAL 44 DAY),2);

INSERT INTO application_history(application_id,old_status,new_status,remarks,changed_by)
SELECT application_id,NULL,application_status,'Sample imported status',2 FROM applications;

INSERT INTO interview_rounds(application_id,round_number,round_type,interview_date,interview_time,mode,interviewer_name,interview_status) VALUES
(1,1,'APTITUDE',DATE_ADD(CURDATE(),INTERVAL -5 DAY),'10:30:00','ONLINE','Interview Panel','COMPLETED'),
(2,2,'TECHNICAL',DATE_ADD(CURDATE(),INTERVAL -4 DAY),'10:30:00','ONLINE','Interview Panel','COMPLETED'),
(3,3,'MANAGERIAL',DATE_ADD(CURDATE(),INTERVAL -3 DAY),'10:30:00','ONLINE','Interview Panel','COMPLETED'),
(4,4,'HR',DATE_ADD(CURDATE(),INTERVAL -2 DAY),'10:30:00','ONLINE','Interview Panel','COMPLETED'),
(5,1,'APTITUDE',DATE_ADD(CURDATE(),INTERVAL -1 DAY),'10:30:00','ONLINE','Interview Panel','COMPLETED'),
(6,2,'TECHNICAL',DATE_ADD(CURDATE(),INTERVAL 0 DAY),'10:30:00','ONLINE','Interview Panel','COMPLETED'),
(7,3,'MANAGERIAL',DATE_ADD(CURDATE(),INTERVAL 1 DAY),'10:30:00','ONLINE','Interview Panel','COMPLETED'),
(8,4,'HR',DATE_ADD(CURDATE(),INTERVAL 2 DAY),'10:30:00','ONLINE','Interview Panel','COMPLETED'),
(9,1,'APTITUDE',DATE_ADD(CURDATE(),INTERVAL 3 DAY),'10:30:00','ONLINE','Interview Panel','COMPLETED'),
(10,2,'TECHNICAL',DATE_ADD(CURDATE(),INTERVAL 4 DAY),'10:30:00','ONLINE','Interview Panel','COMPLETED'),
(11,3,'MANAGERIAL',DATE_ADD(CURDATE(),INTERVAL 5 DAY),'10:30:00','ONLINE','Interview Panel','COMPLETED'),
(12,4,'HR',DATE_ADD(CURDATE(),INTERVAL 6 DAY),'10:30:00','ONLINE','Interview Panel','COMPLETED'),
(13,1,'APTITUDE',DATE_ADD(CURDATE(),INTERVAL 7 DAY),'10:30:00','ONLINE','Interview Panel','COMPLETED'),
(14,2,'TECHNICAL',DATE_ADD(CURDATE(),INTERVAL 8 DAY),'10:30:00','ONLINE','Interview Panel','COMPLETED'),
(15,3,'MANAGERIAL',DATE_ADD(CURDATE(),INTERVAL -5 DAY),'10:30:00','ONLINE','Interview Panel','COMPLETED'),
(16,4,'HR',DATE_ADD(CURDATE(),INTERVAL -4 DAY),'10:30:00','ONLINE','Interview Panel','SCHEDULED'),
(17,1,'APTITUDE',DATE_ADD(CURDATE(),INTERVAL -3 DAY),'10:30:00','ONLINE','Interview Panel','SCHEDULED'),
(18,2,'TECHNICAL',DATE_ADD(CURDATE(),INTERVAL -2 DAY),'10:30:00','ONLINE','Interview Panel','SCHEDULED'),
(19,3,'MANAGERIAL',DATE_ADD(CURDATE(),INTERVAL -1 DAY),'10:30:00','ONLINE','Interview Panel','SCHEDULED'),
(20,4,'HR',DATE_ADD(CURDATE(),INTERVAL 0 DAY),'10:30:00','ONLINE','Interview Panel','SCHEDULED'),
(21,1,'APTITUDE',DATE_ADD(CURDATE(),INTERVAL 1 DAY),'10:30:00','ONLINE','Interview Panel','SCHEDULED'),
(22,2,'TECHNICAL',DATE_ADD(CURDATE(),INTERVAL 2 DAY),'10:30:00','ONLINE','Interview Panel','SCHEDULED'),
(23,3,'MANAGERIAL',DATE_ADD(CURDATE(),INTERVAL 3 DAY),'10:30:00','ONLINE','Interview Panel','SCHEDULED'),
(24,4,'HR',DATE_ADD(CURDATE(),INTERVAL 4 DAY),'10:30:00','ONLINE','Interview Panel','SCHEDULED');

INSERT INTO interview_feedback(interview_id,technical_rating,communication_rating,problem_solving_rating,overall_rating,feedback_remarks,recommendation)
SELECT interview_id,7.5,8.0,7.0,7.5,'Good fundamentals and communication',CASE WHEN interview_id%4=0 THEN 'SELECTED' WHEN interview_id%4=1 THEN 'NEXT_ROUND' WHEN interview_id%4=2 THEN 'ON_HOLD' ELSE 'REJECTED' END
FROM interview_rounds WHERE interview_status='COMPLETED' LIMIT 16;

INSERT INTO offers(offer_code,application_id,designation,offered_package,offer_date,expected_joining_date,offer_status) VALUES
('OFF-2026-001',6,'Associate Software Engineer',5.50,'2026-10-20','2026-12-01','ACCEPTED'),
('OFF-2026-002',8,'Associate Software Engineer',5.50,'2026-10-20','2026-12-01','ACCEPTED'),
('OFF-2026-003',16,'Associate Software Engineer',5.50,'2026-10-20','2026-12-01','ACCEPTED'),
('OFF-2026-004',18,'Associate Software Engineer',5.50,'2026-10-20','2026-12-01','ACCEPTED'),
('OFF-2026-005',26,'Associate Software Engineer',5.50,'2026-10-20','2026-12-01','ACCEPTED'),
('OFF-2026-006',28,'Associate Software Engineer',5.50,'2026-10-20','2026-12-01','OFFERED'),
('OFF-2026-007',36,'Associate Software Engineer',5.50,'2026-10-20','2026-12-01','OFFERED'),
('OFF-2026-008',38,'Associate Software Engineer',5.50,'2026-10-20','2026-12-01','OFFERED');

INSERT INTO application_history(application_id,old_status,new_status,remarks,changed_by)
SELECT application_id,application_status,'OFFERED','Sample offer created',2
FROM applications WHERE application_id IN (SELECT application_id FROM offers);
UPDATE applications a JOIN offers o ON o.application_id=a.application_id SET a.application_status='OFFERED';

INSERT INTO placements(offer_id,candidate_id,company_id,actual_joining_date,joining_status,final_package,designation)
SELECT o.offer_id,a.candidate_id,j.company_id,'2026-10-30','JOINED',o.offered_package,o.designation
FROM offers o JOIN applications a ON a.application_id=o.application_id JOIN jobs j ON j.job_id=a.job_id
WHERE o.offer_status='ACCEPTED' LIMIT 5;
INSERT INTO application_history(application_id,old_status,new_status,remarks,changed_by)
SELECT a.application_id,'OFFERED','JOINED','Sample joining confirmed',4
FROM applications a JOIN placements p ON p.candidate_id=a.candidate_id AND p.offer_id IN (SELECT offer_id FROM offers);
UPDATE applications a JOIN offers o ON o.application_id=a.application_id JOIN placements p ON p.offer_id=o.offer_id SET a.application_status='JOINED';
UPDATE candidates c JOIN placements p ON p.candidate_id=c.candidate_id SET c.placement_status='PLACED';

INSERT INTO activity_logs(user_id,module_name,action_text) VALUES
(1,'SYSTEM','Sample data loaded'),(2,'CANDIDATES','Candidate sample records inserted'),
(3,'JOBS','Job sample records inserted'),(4,'PLACEMENTS','Placement sample records inserted');