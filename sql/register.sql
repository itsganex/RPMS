USE rpms_db;

-- Add the student login fields.
ALTER TABLE users
    ADD COLUMN mobile VARCHAR(20) NULL UNIQUE,
    ADD COLUMN candidate_id INT NULL UNIQUE;

-- Add the remaining student profile fields.
ALTER TABLE candidates
    ADD COLUMN parent_guardian_name VARCHAR(150) NULL,
    ADD COLUMN course VARCHAR(80) NULL,
    ADD COLUMN branch VARCHAR(100) NULL,
    ADD COLUMN class_grade VARCHAR(100) NULL,
    ADD COLUMN semester TINYINT NULL,
    ADD COLUMN tenth_percentage DECIMAL(5,2) NULL,
    ADD COLUMN twelfth_percentage DECIMAL(5,2) NULL,
    ADD COLUMN secondary_skills VARCHAR(500) NULL,
    ADD COLUMN programming_languages VARCHAR(255) NULL,
    ADD COLUMN frameworks VARCHAR(255) NULL,
    ADD COLUMN database_skills VARCHAR(255) NULL,
    ADD COLUMN skill_level VARCHAR(30) NULL,
    ADD COLUMN preferred_job_role VARCHAR(120) NULL,
    ADD COLUMN expected_salary DECIMAL(10,2) NULL,
    ADD COLUMN willing_to_relocate VARCHAR(5) NULL,
    ADD COLUMN internship_experience VARCHAR(5) NULL,
    ADD COLUMN work_experience VARCHAR(255) NULL;

-- Link each student login to its candidate profile.
ALTER TABLE users
    ADD CONSTRAINT fk_users_candidate
    FOREIGN KEY (candidate_id) REFERENCES candidates(candidate_id);

-- Make sure the student role is available.
INSERT INTO roles (role_code, role_name, is_active)
VALUES ('STUDENT', 'Student', 1)
ON DUPLICATE KEY UPDATE role_name = VALUES(role_name), is_active = 1;
