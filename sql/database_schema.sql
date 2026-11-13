CREATE DATABASE IF NOT EXISTS rpms_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE rpms_db;

CREATE TABLE roles (
 role_id INT AUTO_INCREMENT PRIMARY KEY, role_code VARCHAR(30) NOT NULL UNIQUE,
 role_name VARCHAR(80) NOT NULL, is_active TINYINT(1) DEFAULT 1,
 created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE users (
 user_id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(80) NOT NULL UNIQUE,
 password_hash VARCHAR(255) NOT NULL, full_name VARCHAR(120) NOT NULL,
 email VARCHAR(150) UNIQUE, role_id INT NOT NULL, status VARCHAR(20) DEFAULT 'ACTIVE',
 last_login_at DATETIME NULL, created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
 CONSTRAINT fk_users_role FOREIGN KEY(role_id) REFERENCES roles(role_id),
 INDEX idx_users_role(role_id)
);
CREATE TABLE qualifications (
 qualification_id INT AUTO_INCREMENT PRIMARY KEY, qualification_name VARCHAR(80) NOT NULL UNIQUE,
 is_active TINYINT(1) DEFAULT 1
);
CREATE TABLE locations (
 location_id INT AUTO_INCREMENT PRIMARY KEY, location_name VARCHAR(100) NOT NULL UNIQUE,
 state_name VARCHAR(100), country_name VARCHAR(100) DEFAULT 'India'
);
CREATE TABLE candidates (
 candidate_id INT AUTO_INCREMENT PRIMARY KEY, candidate_code VARCHAR(30) NOT NULL UNIQUE,
 full_name VARCHAR(150) NOT NULL, parent_guardian_name VARCHAR(150), email VARCHAR(150) NOT NULL UNIQUE, mobile VARCHAR(20) NOT NULL UNIQUE,
 date_of_birth DATE NULL, gender VARCHAR(20) NULL, qualification VARCHAR(80) NOT NULL,
 course VARCHAR(80), branch VARCHAR(100), class_grade VARCHAR(100), semester TINYINT,
 college VARCHAR(180), university VARCHAR(180), passing_year SMALLINT NOT NULL,
 tenth_percentage DECIMAL(5,2), twelfth_percentage DECIMAL(5,2),
 percentage DECIMAL(5,2), cgpa DECIMAL(4,2), backlog_count INT DEFAULT 0,
 primary_technology VARCHAR(80), secondary_skills VARCHAR(500), programming_languages VARCHAR(255),
 frameworks VARCHAR(255), database_skills VARCHAR(255), skill_level VARCHAR(30),
 current_location VARCHAR(100), preferred_location VARCHAR(100),
 preferred_job_role VARCHAR(120), expected_salary DECIMAL(10,2),
 willing_to_relocate VARCHAR(5), internship_experience VARCHAR(5), work_experience VARCHAR(255),
 profile_status VARCHAR(20) DEFAULT 'ACTIVE', placement_status VARCHAR(20) DEFAULT 'NOT_PLACED',
 created_at DATETIME DEFAULT CURRENT_TIMESTAMP, updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
 CONSTRAINT chk_candidate_percentage CHECK (percentage IS NULL OR percentage BETWEEN 0 AND 100),
 CONSTRAINT chk_candidate_backlogs CHECK (backlog_count >= 0),
 INDEX idx_candidate_technology(primary_technology), INDEX idx_candidate_year(passing_year),
 INDEX idx_candidate_status(profile_status,placement_status)
);

-- Add student login fields after the candidate table is available.
ALTER TABLE users
 ADD COLUMN mobile VARCHAR(20) NULL UNIQUE,
 ADD COLUMN candidate_id INT NULL UNIQUE,
 ADD CONSTRAINT fk_users_candidate
 FOREIGN KEY(candidate_id) REFERENCES candidates(candidate_id);

CREATE TABLE skills (
 skill_id INT AUTO_INCREMENT PRIMARY KEY, skill_name VARCHAR(100) NOT NULL UNIQUE,
 category VARCHAR(60), is_active TINYINT(1) DEFAULT 1
);
CREATE TABLE candidate_skills (
 candidate_skill_id INT AUTO_INCREMENT PRIMARY KEY, candidate_id INT NOT NULL, skill_id INT NOT NULL,
 skill_level VARCHAR(30), is_primary TINYINT(1) DEFAULT 0,
 UNIQUE KEY uq_candidate_skill(candidate_id,skill_id),
 FOREIGN KEY(candidate_id) REFERENCES candidates(candidate_id),
 FOREIGN KEY(skill_id) REFERENCES skills(skill_id)
);
CREATE TABLE companies (
 company_id INT AUTO_INCREMENT PRIMARY KEY, company_name VARCHAR(160) NOT NULL UNIQUE,
 industry VARCHAR(100), website VARCHAR(200), location VARCHAR(100), company_type VARCHAR(30),
 hr_name VARCHAR(120), hr_email VARCHAR(150), hr_mobile VARCHAR(20),
 status VARCHAR(20) DEFAULT 'ACTIVE', created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
 INDEX idx_company_status(status)
);
CREATE TABLE jobs (
 job_id INT AUTO_INCREMENT PRIMARY KEY, company_id INT NOT NULL, job_code VARCHAR(40) NOT NULL UNIQUE,
 job_title VARCHAR(150) NOT NULL, openings INT NOT NULL, employment_type VARCHAR(40),
 location VARCHAR(100), min_package DECIMAL(10,2), max_package DECIMAL(10,2),
 qualification VARCHAR(80), min_percentage DECIMAL(5,2), min_passing_year SMALLINT,
 max_passing_year SMALLINT, max_backlogs INT DEFAULT 0, experience_required VARCHAR(80),
 required_technology VARCHAR(80), posted_date DATE NOT NULL, application_deadline DATE NOT NULL,
 job_status VARCHAR(20) DEFAULT 'DRAFT', created_by INT NULL, created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
 FOREIGN KEY(company_id) REFERENCES companies(company_id),
 FOREIGN KEY(created_by) REFERENCES users(user_id),
 CONSTRAINT chk_job_openings CHECK(openings > 0),
 CONSTRAINT chk_job_package CHECK(max_package IS NULL OR min_package IS NULL OR min_package <= max_package),
 CONSTRAINT chk_job_percentage CHECK(min_percentage IS NULL OR min_percentage BETWEEN 0 AND 100),
 CONSTRAINT chk_job_backlogs CHECK(max_backlogs >= 0),
 CONSTRAINT chk_job_dates CHECK(application_deadline >= posted_date),
 INDEX idx_job_status(job_status), INDEX idx_job_company(company_id), INDEX idx_job_deadline(application_deadline)
);
CREATE TABLE job_skills (
 job_skill_id INT AUTO_INCREMENT PRIMARY KEY, job_id INT NOT NULL, skill_id INT NOT NULL,
 mandatory_flag TINYINT(1) DEFAULT 1, UNIQUE KEY uq_job_skill(job_id,skill_id),
 FOREIGN KEY(job_id) REFERENCES jobs(job_id), FOREIGN KEY(skill_id) REFERENCES skills(skill_id)
);
CREATE TABLE applications (
 application_id INT AUTO_INCREMENT PRIMARY KEY, application_code VARCHAR(40) NOT NULL UNIQUE,
 candidate_id INT NOT NULL, job_id INT NOT NULL, eligibility_status VARCHAR(20) DEFAULT 'PENDING',
 eligibility_reason VARCHAR(500), application_status VARCHAR(30) NOT NULL DEFAULT 'APPLIED',
 applied_at DATETIME DEFAULT CURRENT_TIMESTAMP, assigned_recruiter_id INT NULL,
 UNIQUE KEY uq_candidate_job(candidate_id,job_id),
 FOREIGN KEY(candidate_id) REFERENCES candidates(candidate_id),
 FOREIGN KEY(job_id) REFERENCES jobs(job_id),
 FOREIGN KEY(assigned_recruiter_id) REFERENCES users(user_id),
 INDEX idx_application_status(application_status), INDEX idx_application_applied(applied_at),
 INDEX idx_application_recruiter(assigned_recruiter_id)
);
CREATE TABLE application_history (
 history_id BIGINT AUTO_INCREMENT PRIMARY KEY, application_id INT NOT NULL,
 old_status VARCHAR(30), new_status VARCHAR(30) NOT NULL, remarks VARCHAR(500),
 changed_by INT NULL, changed_at DATETIME DEFAULT CURRENT_TIMESTAMP,
 FOREIGN KEY(application_id) REFERENCES applications(application_id),
 FOREIGN KEY(changed_by) REFERENCES users(user_id), INDEX idx_history_app(application_id), INDEX idx_history_changed(changed_at)
);
CREATE TABLE interview_rounds (
 interview_id INT AUTO_INCREMENT PRIMARY KEY, application_id INT NOT NULL, round_number INT NOT NULL,
 round_type VARCHAR(30) NOT NULL, interview_date DATE NOT NULL, interview_time TIME,
 mode VARCHAR(20), interviewer_name VARCHAR(120), interview_status VARCHAR(20) DEFAULT 'SCHEDULED',
 created_at DATETIME DEFAULT CURRENT_TIMESTAMP, UNIQUE KEY uq_application_round(application_id,round_number),
 FOREIGN KEY(application_id) REFERENCES applications(application_id), INDEX idx_interview_date_status(interview_date,interview_status)
);
CREATE TABLE interview_feedback (
 feedback_id INT AUTO_INCREMENT PRIMARY KEY, interview_id INT NOT NULL UNIQUE,
 technical_rating DECIMAL(3,1), communication_rating DECIMAL(3,1), problem_solving_rating DECIMAL(3,1),
 overall_rating DECIMAL(3,1), feedback_remarks TEXT, recommendation VARCHAR(30),
 created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
 FOREIGN KEY(interview_id) REFERENCES interview_rounds(interview_id),
 INDEX idx_feedback_recommendation(recommendation)
);
CREATE TABLE offers (
 offer_id INT AUTO_INCREMENT PRIMARY KEY, offer_code VARCHAR(40) NOT NULL UNIQUE,
 application_id INT NOT NULL UNIQUE, designation VARCHAR(120) NOT NULL,
 offered_package DECIMAL(10,2) NOT NULL, offer_date DATE NOT NULL, expected_joining_date DATE,
 offer_status VARCHAR(20) DEFAULT 'OFFERED', created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
 FOREIGN KEY(application_id) REFERENCES applications(application_id), INDEX idx_offer_status(offer_status)
);
CREATE TABLE placements (
 placement_id INT AUTO_INCREMENT PRIMARY KEY, offer_id INT NOT NULL UNIQUE, candidate_id INT NOT NULL,
 company_id INT NOT NULL, actual_joining_date DATE, joining_status VARCHAR(20) DEFAULT 'PENDING',
 final_package DECIMAL(10,2), designation VARCHAR(120), created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
 FOREIGN KEY(offer_id) REFERENCES offers(offer_id), FOREIGN KEY(candidate_id) REFERENCES candidates(candidate_id),
 FOREIGN KEY(company_id) REFERENCES companies(company_id),
 INDEX idx_placement_candidate(candidate_id), INDEX idx_placement_company(company_id), INDEX idx_placement_status(joining_status)
);
CREATE TABLE activity_logs (
 activity_id BIGINT AUTO_INCREMENT PRIMARY KEY, user_id INT NULL, module_name VARCHAR(80),
 action_text VARCHAR(500) NOT NULL, logged_at DATETIME DEFAULT CURRENT_TIMESTAMP,
 FOREIGN KEY(user_id) REFERENCES users(user_id), INDEX idx_activity_user(user_id),
 INDEX idx_activity_module(module_name), INDEX idx_activity_logged(logged_at)
);
