const api = async (url, options = {}) => {
    const response = await fetch(url, {
        credentials: "same-origin",
        headers: { "Content-Type": "application/json", ...(options.headers || {}) },
        ...options
    });
    const result = await response.json().catch(() => ({}));
    if (!response.ok) throw new Error(result.error || result.message || "Request failed.");
    return result;
};

const escapeHTML = value => String(value ?? "").replace(/[&<>"']/g, char => ({
    "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"
}[char]));

const showMessage = (element, message, type = "success") => {
    element.textContent = message;
    element.className = `message ${type}`;
};

async function loadProfile() {
    const profile = await api("/api/student/profile");
    document.getElementById("studentName").textContent = profile.full_name;
    document.getElementById("profile").innerHTML = `
        <p><strong>Name</strong><br>${escapeHTML(profile.full_name)}</p>
        <p><strong>Candidate ID</strong><br>${escapeHTML(profile.candidate_code)}</p>
        <p><strong>Email</strong><br>${escapeHTML(profile.email)}</p>
        <p><strong>Mobile</strong><br>${escapeHTML(profile.mobile)}</p>
        <p><strong>Course / Branch</strong><br>${escapeHTML(profile.course || profile.qualification)} / ${escapeHTML(profile.branch)}</p>
        <p><strong>College</strong><br>${escapeHTML(profile.college)}</p>
        <p><strong>Passing year</strong><br>${escapeHTML(profile.passing_year)}</p>
        <p><strong>CGPA</strong><br>${escapeHTML(profile.cgpa)}</p>`;
}

async function loadJobs() {
    const jobs = await api("/api/student/jobs");
    const body = document.getElementById("jobRows");
    body.innerHTML = jobs.map(job => `
        <tr>
            <td>${escapeHTML(job.company_name)}</td>
            <td>${escapeHTML(job.job_title)}</td>
            <td>${escapeHTML(job.location)}</td>
            <td>${escapeHTML(job.min_package)} - ${escapeHTML(job.max_package)}</td>
            <td>${escapeHTML(job.application_deadline)}</td>
            <td><button class="btn primary small apply-job" data-job-id="${Number(job.job_id)}">Apply</button></td>
        </tr>`).join("") || '<tr><td colspan="6">There are no open jobs at the moment.</td></tr>';

    body.querySelectorAll(".apply-job").forEach(button => {
        button.addEventListener("click", async () => {
            button.disabled = true;
            try {
                const result = await api("/api/student/apply", {
                    method: "POST",
                    body: JSON.stringify({ job_id: Number(button.dataset.jobId) })
                });
                showMessage(document.getElementById("jobMessage"), result.message);
                await loadApplications();
            } catch (error) {
                showMessage(document.getElementById("jobMessage"), error.message, "error");
            } finally {
                button.disabled = false;
            }
        });
    });
}

async function loadApplications() {
    const rows = await api("/api/student/applications");
    document.getElementById("applicationRows").innerHTML = rows.map(row => `
        <tr>
            <td>${escapeHTML(row.application_code)}</td>
            <td>${escapeHTML(row.company_name)}</td>
            <td>${escapeHTML(row.job_title)}</td>
            <td>${escapeHTML(row.application_status)}</td>
            <td>${escapeHTML(row.applied_at)}</td>
        </tr>`).join("") || '<tr><td colspan="5">You have not applied for any jobs yet.</td></tr>';
}

document.getElementById("logoutBtn").addEventListener("click", async () => {
    try {
        await api("/api/logout", { method: "POST" });
        window.location.href = "/login.html";
    } catch (error) {
        alert(error.message);
    }
});

Promise.all([loadProfile(), loadJobs(), loadApplications()]).catch(error => {
    alert(error.message);
    if (error.message.toLowerCase().includes("sign in")) {
        window.location.href = "/login.html";
    }
});
