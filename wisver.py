DOCTYPE :html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SkillGap Analyzer</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>SkillGap Analyzer</h1>
        <form id="resumeForm">
            <label for="resume">Upload your resume (PDF or DOCX):</label>
            <input type="file" id="resume" accept=".pdf,.docx" required>
            <button type="submit">Analyze</button>
        </form>
        <div id="result" class="hidden">
            <h2>Your Skill Gap Analysis</h2>
            <div id="recommendations"></div>
        </div>
    </div>
    <script src="script.js"></script>
</body>
</html>
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    margin: 0;
    padding:20 px;
}

.container {
    max-width: 600 px;
    margin: auto;
    background: white;
    padding: 20 px;
    border-radius: 5 px;
    box-shadow: 0 0 10 px rgba(0, 0, 0, 0.1);
}

h1 {
    text-align: center;
}

.hidden {
    display: none;
}

button {
    display: block;
    width: 100%;
    padding: 10 px;
    background-color: #007BFF;
    color: white;
    border: none;
    border-radius: 5 px;
    cursor: pointer;
}

button:hover {
    background-color: #0056b3;
}document.getElementById('resumeForm').addEventListener('submit', async function(event) {
    event.preventDefault();
    
    const resumeFile = document.getElementById('resume').files[0];
    const formData = new FormData();
    formData.append('resume', resumeFile);

    const response = await fetch('/analyze', {
        method: 'POST',
        body: formData
    });

    const data = await response.json();
    displayResults(data);
});

function displayResults(data) {
    const resultDiv = document.getElementById('result');
    const recommendationsDiv = document.getElementById('recommendations');
    
    recommendationsDiv.innerHTML = '';
    data.recommendations.forEach(rec => {
        const p = document.createElement('p');
        p.textContent = rec;
        recommendationsDiv.appendChild(p);
    });

    resultDiv.classList.remove('hidden');
}
const express = require('express');
const multer = require('multer');
const bodyParser = require('body-parser');
const { analyzeResume } = require('./resumeAnalyzer'); // Assume this is a module you create for analyzing resumes

const app = express();
const PORT = process.env.PORT || 3000;

const upload = multer({ dest: 'uploads/' });

app.use(express.static('public'));
app.use(bodyParser.json());

app.post('/analyze', upload.single('resume'), async (req, res) => {
    try {
        const resumePath = req.file.path;
        const recommendations = await analyzeResume(resumePath);
        res.json({ recommendations });
    } catch (error) {
        res.status(500).json({ error: 'An error occurred while analyzing the resume.' });
    }
});

app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
const fs = require('fs');

async function analyzeResume(resumePath) {
    // Placeholder for actual resume analysis logic
    // You would implement logic to read the resume file, extract skills,
    // compare them against a database of required skills, and generate recommendations.

    // For demonstration, returning static recommendations
    return [
    
        <!-- Add to container div -->
<div class="input-group">
    <label for="targetRole">Target Job Role:</label>
    <input type="text" id="targetRole" required>
</div>

<div class="input-group">
    <label for="experience">Years of Experience:</label>
    <input type="number" id="experience" min="0" required>
</div>

<!-- Update results section -->
<div id="result" class="hidden">
    <h2>Your Personalized Learning Roadmap</h2>
    <div class="skill-gap-chart"></div>
    <h3>Recommended Resources</h3>
    <div id="resources"></div>
    <h3>Project Suggestions</h3>
    <div id="projects"></div>
</div>
.skill-gap-chart {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200 px, 1 fr));
    gap: 10 px;
    margin: 20 px 0;
}

.skill-card {
    background: #fff;
    border: 1 px solid #ddd;
    padding: 15 px;
    border-radius: 8 px;
    box-shadow: 0 2 px 4 px rgba(0,0,0,0.1);
}

.resource-item {
    margin: 10 px 0;
    padding: 10 px;
    border-left: 4 px solid #007BFF;
}

.project-card {
    background: #f8f9fa;
    padding: 15 px;
    margin: 10 px 0;
    border-radius: 5 px;
}
// Update form submission handler
const formData = new FormData();
formData.append('resume', resumeFile);
formData.append('targetRole', document.getElementById('targetRole').value);
formData.append('experience', document.getElementById('experience').value);

// Enhanced display function
function displayResults(data) {
    // Clear previous results
    resultDiv.classList.remove('hidden');
    
    // Display skill gaps
    const chartDiv = document.querySelector('.skill-gap-chart');
    data.skillGaps.forEach(skill => {
        chartDiv.innerHTML += `
            <div class="skill-card">
                <h4>${skill.name}</h4>
                <p>Priority: ${skill.priority}/5</p>
                <p>${skill.description}</p>
            </div>
        `;
    });

    // Display resources
    data.resources.forEach(resource => {
        resourcesDiv.innerHTML += `
            <div class="resource-item">
                <a href="${resource.link}" target="_blank">${resource.title}</a>
                <p>${resource.platform} (${resource.type})</p>
            </div>
        `;
    });

    // Display projects
    data.projects.forEach(project => {
        projectsDiv.innerHTML += `
            <div class="project-card">
                <h4>${project.title}</h4>
                <p>${project.description}</p>
                <p>Skills: ${project.skills.join(', ')}</p>
            </div>
        `;
    });
}
// Add database connection
const mongoose = require('mongoose');
mongoose.connect('mongodb://localhost/skillgap', { 
    useNewUrlParser: true, 
    useUnifiedTopology: true 
});

// Add authentication middleware
const authMiddleware = (req, res, next) => {
    // Implement JWT validation here
    next();
};

// Add user endpoints
app.post('/register', async (req, res) => {
    // User registration logic
});

app.post('/login', async (req, res) => {
    // User login logic
});