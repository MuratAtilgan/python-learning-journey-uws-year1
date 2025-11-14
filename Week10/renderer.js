document.addEventListener('DOMContentLoaded', () => {
    // Navigation
    const menuBtns = document.querySelectorAll('.menu-btn');
    const views = document.querySelectorAll('.view');

    menuBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const viewId = btn.dataset.view + '-view';
            
            // Update active button
            menuBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            
            // Show selected view
            views.forEach(view => {
                view.classList.add('hidden');
                if (view.id === viewId) {
                    view.classList.remove('hidden');
                    loadViewData(btn.dataset.view);
                }
            });
        });
    });

    // Set main menu as active initially
    document.querySelector('[data-view="main"]').classList.add('active');

    // Add Student Form
    document.getElementById('add-form').addEventListener('submit', async (e) => {
        e.preventDefault();
        const resultDiv = document.getElementById('add-result');
        
        const student = {
            name: document.getElementById('add-name').value.trim(),
            surname: document.getElementById('add-surname').value.trim(),
            age: parseInt(document.getElementById('add-age').value),
            mark: parseFloat(document.getElementById('add-mark').value),
            banner: document.getElementById('add-banner').value.trim()
        };

        try {
            const response = await window.electronAPI.addStudent(student);
            resultDiv.innerHTML = `<p class="${response.success ? 'success' : 'error'}">${response.message}</p>`;
            if (response.success) {
                document.getElementById('add-form').reset();
            }
        } catch (error) {
            resultDiv.innerHTML = `<p class="error">Error adding student: ${error.message}</p>`;
        }
    });

    // Search functionality
    let currentSearchType = 'surname';
    document.getElementById('search-surname-btn').addEventListener('click', () => {
        currentSearchType = 'surname';
        document.getElementById('search-label').textContent = 'Enter Surname:';
        document.getElementById('search-value').value = '';
    });

    document.getElementById('search-banner-btn').addEventListener('click', () => {
        currentSearchType = 'banner';
        document.getElementById('search-label').textContent = 'Enter Student ID:';
        document.getElementById('search-value').value = '';
    });

    document.getElementById('search-form').addEventListener('submit', async (e) => {
        e.preventDefault();
        const searchValue = document.getElementById('search-value').value.trim();
        const resultsDiv = document.getElementById('search-results');

        try {
            const results = await window.electronAPI.searchStudent(currentSearchType, searchValue);
            if (results.length > 0) {
                let html = '<div class="student-list">';
                results.forEach(result => {
                    html += `
                        <div class="student-item">
                            <p><strong>Name:</strong> ${result.name} ${result.surname}</p>
                            <p><strong>Age:</strong> ${result.age} years old</p>
                            <p><strong>Mark:</strong> ${result.mark}</p>
                            <p><strong>Grade:</strong> ${result.grade}</p>
                            <p><strong>Student ID:</strong> ${result.banner}</p>
                        </div>
                    `;
                });
                html += '</div>';
                resultsDiv.innerHTML = html;
            } else {
                resultsDiv.innerHTML = '<p class="error">No student found with this ' + (currentSearchType === 'surname' ? 'surname' : 'ID') + '!</p>';
            }
        } catch (error) {
            resultsDiv.innerHTML = `<p class="error">Error searching student: ${error.message}</p>`;
        }
    });

    // Update Student Form
    document.getElementById('update-form').addEventListener('submit', async (e) => {
        e.preventDefault();
        const resultDiv = document.getElementById('update-result');
        
        const banner = document.getElementById('update-banner').value.trim();
        const newMark = parseFloat(document.getElementById('update-mark').value);

        try {
            const response = await window.electronAPI.updateStudent(banner, newMark);
            resultDiv.innerHTML = `<p class="${response.success ? 'success' : 'error'}">${response.message}</p>`;
            if (response.success) {
                document.getElementById('update-form').reset();
            }
        } catch (error) {
            resultDiv.innerHTML = `<p class="error">Error updating student: ${error.message}</p>`;
        }
    });

    // Delete Student
    document.getElementById('delete-btn').addEventListener('click', async () => {
        const index = parseInt(document.getElementById('delete-index').value) - 1;
        const resultDiv = document.getElementById('delete-result');

        try {
            const response = await window.electronAPI.deleteStudent(index);
            resultDiv.innerHTML = `<p class="${response.success ? 'success' : 'error'}">${response.message}</p>`;
            if (response.success) {
                document.getElementById('delete-index').value = '';
                loadDeleteView(); // Reload the student list
            }
        } catch (error) {
            resultDiv.innerHTML = `<p class="error">Error deleting student: ${error.message}</p>`;
        }
    });
});

async function loadViewData(view) {
    switch(view) {
        case 'view':
            loadViewAllStudents();
            break;
        case 'delete':
            loadDeleteView();
            break;
        case 'stats':
            loadStats();
            break;
        case 'distribution':
            loadGradeDistribution();
            break;
    }
}

async function loadViewAllStudents() {
    try {
        const data = await window.electronAPI.getStudents();
        const container = document.getElementById('students-list');
        
        if (data.names.length === 0) {
            container.innerHTML = '<p>No students in database!</p>';
            return;
        }

        let html = '<div class="student-list">';
        for (let i = 0; i < data.names.length; i++) {
            html += `
                <div class="student-item">
                    <p>${i + 1}. ${data.names[i]} ${data.surnames[i]} | Age: ${data.ages[i]} | Mark: ${data.marks[i]} | Grade: ${data.grades[i]} | ID: ${data.banners[i]}</p>
                </div>
            `;
        }
        html += '</div>';
        container.innerHTML = html;
    } catch (error) {
        document.getElementById('students-list').innerHTML = `<p class="error">Error loading students: ${error.message}</p>`;
    }
}

async function loadDeleteView() {
    try {
        const data = await window.electronAPI.getStudents();
        const container = document.getElementById('delete-students-list');
        
        if (data.names.length === 0) {
            container.innerHTML = '<p>No students to delete!</p>';
            return;
        }

        let html = '<div class="student-list">';
        for (let i = 0; i < data.names.length; i++) {
            html += `
                <div class="student-item">
                    <p>${i + 1}. ${data.names[i]} ${data.surnames[i]} | Age: ${data.ages[i]} | Mark: ${data.marks[i]} | Grade: ${data.grades[i]} | ID: ${data.banners[i]}</p>
                </div>
            `;
        }
        html += '</div>';
        container.innerHTML = html;
    } catch (error) {
        document.getElementById('delete-students-list').innerHTML = `<p class="error">Error loading students: ${error.message}</p>`;
    }
}

async function loadStats() {
    try {
        const stats = await window.electronAPI.getStats();
        const container = document.getElementById('stats-content');
        
        if (!stats) {
            container.innerHTML = '<p>No students for statistics!</p>';
            return;
        }

        let html = `
            <div class="stats-item">
                <p><strong>HIGHEST:</strong> ${stats.highest.name} | ${stats.highest.mark} marks | Grade ${stats.highest.grade}</p>
            </div>
            <div class="stats-item">
                <p><strong>LOWEST:</strong> ${stats.lowest.name} | ${stats.lowest.mark} marks | Grade ${stats.lowest.grade}</p>
            </div>
            <div class="stats-item">
                <p><strong>YOUNGEST:</strong> ${stats.youngest.name} | ${stats.youngest.age} years old</p>
            </div>
            <div class="stats-item">
                <p><strong>ELDEST:</strong> ${stats.eldest.name} | ${stats.eldest.age} years old</p>
            </div>
            <div class="stats-item">
                <p><strong>AVERAGE:</strong> ${stats.average.mark} marks | Grade ${stats.average.grade}</p>
            </div>
            <div class="stats-item">
                <p><strong>PASS (>=40):</strong> ${stats.passFail.passCount} students (${stats.passFail.passPercent}%)</p>
                <p><strong>FAIL (<40):</strong> ${stats.passFail.failCount} students (${stats.passFail.failPercent}%)</p>
            </div>
        `;
        container.innerHTML = html;
    } catch (error) {
        document.getElementById('stats-content').innerHTML = `<p class="error">Error loading statistics: ${error.message}</p>`;
    }
}

async function loadGradeDistribution() {
    try {
        const distribution = await window.electronAPI.getGradeDistribution();
        const container = document.getElementById('distribution-content');
        
        if (Object.keys(distribution).length === 0) {
            container.innerHTML = '<p>No students for distribution!</p>';
            return;
        }

        let html = '<div class="distribution-list">';
        const gradeOrder = ["A1", "A2", "A3", "B1", "B2", "C", "D", "E"];
        
        for (const grade of gradeOrder) {
            if (distribution[grade]) {
                const count = distribution[grade].count;
                const percent = distribution[grade].percent;
                const barWidth = (count / 10) * 100; // Adjust bar width based on count
                html += `
                    <div class="distribution-item">
                        <p>${grade}: ${count} students (${percent}%)</p>
                        <div class="bar" style="width: ${Math.min(barWidth, 100)}%"></div>
                    </div>
                `;
            }
        }
        html += '</div>';
        container.innerHTML = html;
    } catch (error) {
        document.getElementById('distribution-content').innerHTML = `<p class="error">Error loading grade distribution: ${error.message}</p>`;
    }
}