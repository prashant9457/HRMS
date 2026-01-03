function loadEmployees() {

    // Mock data (replace with backend API)
    const employees = [
        {
            id: 1,
            name: "Ravi Kumar",
            dob: "1992-04-18",
            address: "Laxmi Nagar, Delhi",
            dept: "Sanitation",
            role: "Supervisor",
            experience: 8,
            prevOrg: "NDMC",
            verified: true
        },
        {
            id: 2,
            name: "Anita Sharma",
            dob: "1995-11-02",
            address: "Rohini, Delhi",
            dept: "IT",
            role: "System Analyst",
            experience: 5,
            prevOrg: "NIC",
            verified: false
        }
    ];

    const grid = document.getElementById("employeeGrid");
    grid.innerHTML = "";

    employees.forEach(emp => {
        const card = document.createElement("div");
        card.className = "employee-card";

        card.innerHTML = `
            <span class="badge ${emp.verified ? 'verified' : 'unverified'}">
                ${emp.verified ? 'Verified' : 'Unverified'}
            </span>

            <h3>${emp.name}</h3>
            <div class="dept">${emp.dept} • ${emp.role}</div>

            <div class="info"><span>DOB:</span> ${emp.dob}</div>
            <div class="info"><span>Address:</span> ${emp.address}</div>
            <div class="info"><span>Experience:</span> ${emp.experience} Years</div>
            <div class="info"><span>Previous Org:</span> ${emp.prevOrg}</div>

            <div class="card-actions">
                <button class="view-btn">View</button>
                ${emp.verified ? '' : '<button class="verify-btn">Verify</button>'}
            </div>
        `;

        grid.appendChild(card);
    });
}

// Load on page open
loadEmployees();
