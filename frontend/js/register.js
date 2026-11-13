
document.addEventListener("DOMContentLoaded", function () {

    const registerForm = document.getElementById("registerForm");
    const registerButton = document.getElementById("registerButton");
    const messageBox = document.getElementById("message");

    const passwordInput = document.getElementById("password");
    const confirmPasswordInput = document.getElementById("confirm_password");
    const dobInput = document.getElementById("dob");

    // Display messages
    function showMessage(message, type = "error") {
        messageBox.textContent = message;
        messageBox.className = "message " + type;
        messageBox.style.display = "block";
    }

    function clearMessage() {
        messageBox.textContent = "";
        messageBox.style.display = "none";
    }

    // Validate mobile number
    function isValidMobile(mobile) {
        return /^[0-9]{10}$/.test(mobile);
    }

    // Validate email
    function isValidEmail(email) {
        return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
    }

    // Validate date of birth
    function isValidDOB(dob) {
        if (!dob) return false;

        const birthDate = new Date(dob + "T00:00:00");
        const today = new Date();

        return !isNaN(birthDate.getTime()) && birthDate <= today;
    }

    // Validate passwords
    function validatePassword(password) {
        return password.length >= 8;
    }

    // Convert empty numeric fields to null
    function convertNumber(value) {
        if (value === "" || value === null || value === undefined) {
            return null;
        }

        return Number(value);
    }

    // Registration form submission
    registerForm.addEventListener("submit", async function (event) {

        event.preventDefault();
        clearMessage();

        // Collect form data
        const formData = new FormData(registerForm);
        const data = Object.fromEntries(formData.entries());

        // Trim text fields
        Object.keys(data).forEach(function (key) {
            if (typeof data[key] === "string") {
                data[key] = data[key].trim();
            }
        });

        // Password validation
        if (!validatePassword(data.password)) {
            showMessage("Password must contain at least 8 characters.");
            passwordInput.focus();
            return;
        }

        if (data.password !== data.confirm_password) {
            showMessage("Password and Confirm Password do not match.");
            confirmPasswordInput.focus();
            return;
        }

        // Email validation
        if (!isValidEmail(data.email)) {
            showMessage("Please enter a valid email address.");
            return;
        }

        // Mobile validation
        if (!isValidMobile(data.mobile)) {
            showMessage("Please enter a valid 10-digit mobile number.");
            return;
        }

        // DOB validation
        if (!isValidDOB(data.date_of_birth)) {
            showMessage("Please select a valid date of birth.");
            dobInput.focus();
            return;
        }

        // Academic validation
        const percentageFields = [
            "tenth_percentage",
            "twelfth_percentage",
            "percentage"
        ];

        for (const field of percentageFields) {
            const value = data[field];

            if (value !== "" && (Number(value) < 0 || Number(value) > 100)) {
                showMessage(field.replaceAll("_", " ") +
                    " must be between 0 and 100.");
                return;
            }
        }

        if (data.cgpa !== "" &&
            (Number(data.cgpa) < 0 || Number(data.cgpa) > 10)) {
            showMessage("CGPA must be between 0 and 10.");
            return;
        }

        if (data.backlog_count !== "" &&
            Number(data.backlog_count) < 0) {
            showMessage("Backlog count cannot be negative.");
            return;
        }

        // Convert numeric fields
        const numericFields = [
            "passing_year",
            "semester",
            "tenth_percentage",
            "twelfth_percentage",
            "percentage",
            "cgpa",
            "backlog_count",
            "expected_salary"
        ];

        numericFields.forEach(function (field) {
            if (field in data) {
                data[field] = convertNumber(data[field]);
            }
        });

        // Age is calculated from DOB in HTML.
        // It is not sent because it has no name attribute.

        // Confirm password is not stored in the database.
        delete data.confirm_password;

        // Prevent duplicate submissions
        registerButton.disabled = true;
        registerButton.textContent = "Registering...";

        try {

            const response = await fetch("/api/register", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(data)
            });

            let result;

            try {
                result = await response.json();
            } catch {
                throw new Error("Invalid server response. Please check your Flask API.");
            }

            if (!response.ok) {
                throw new Error(
                    result.message || result.error ||
                    "Registration failed. Please try again."
                );
            }

            showMessage(
                result.message || "Registration successful! You can now log in.",
                "success"
            );

            registerForm.reset();

            const ageInput = document.getElementById("age");
            if (ageInput) {
                ageInput.value = "";
            }

            // Redirect to login after successful registration
            setTimeout(function () {
                window.location.href = "/login.html";
            }, 2000);

        } catch (error) {

            console.error("Registration Error:", error);

            showMessage(
                error.message || "Unable to connect to the server."
            );

        } finally {

            registerButton.disabled = false;
            registerButton.textContent = "Register Now";

        }

    });

});
