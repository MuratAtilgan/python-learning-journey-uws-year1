const { app, BrowserWindow, ipcMain } = require('electron');
const path = require('path');
const fs = require('fs');

// Student data arrays
let names = [];
let surnames = [];
let ages = [];
let marks = [];
let grades = [];
let banners = [];

// Load existing data
function loadStudents() {
  try {
    if (fs.existsSync('students.pck')) {
      const data = JSON.parse(fs.readFileSync('students.pck', 'utf8'));
      names = data.names || [];
      surnames = data.surnames || [];
      ages = data.ages || [];
      marks = data.marks || [];
      grades = data.grades || [];
      banners = data.banners || [];
      console.log(`Loaded ${names.length} students`);
    }
  } catch (error) {
    console.log('Starting fresh!');
  }
}

// Calculate grade based on mark
function calculationGrade(mark) {
  if (mark < 30) return "E";
  else if (mark < 40) return "D";
  else if (mark < 50) return "C";
  else if (mark < 60) return "B2";
  else if (mark < 70) return "B1";
  else if (mark < 80) return "A3";
  else if (mark < 90) return "A2";
  else return "A1";
}

// Check if student exists
function studentExists(bannerId) {
  return banners.some(banner => banner.toLowerCase() === bannerId.toLowerCase());
}

// Save data
function saveStudents() {
  const studentData = {
    names,
    surnames,
    ages,
    marks,
    grades,
    banners
  };
  fs.writeFileSync('students.pck', JSON.stringify(studentData, null, 2));
  console.log('All student data saved to students.pck');
}

// Create main window
function createWindow() {
  const mainWindow = new BrowserWindow({
    width: 1000,
    height: 700,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
      nodeIntegration: false,
      contextIsolation: true
    }
  });

  mainWindow.loadFile(path.join(__dirname, 'index.html'));
  return mainWindow;
}

app.whenReady().then(() => {
  loadStudents();
  createWindow();

  app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') app.quit();
  });

  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) createWindow();
  });
});

app.on('before-quit', () => {
  saveStudents();
});

// IPC Handlers
ipcMain.handle('get-students', () => {
  return {
    names,
    surnames,
    ages,
    marks,
    grades,
    banners
  };
});

ipcMain.handle('add-student', (event, student) => {
  if (studentExists(student.banner)) {
    return { success: false, message: `Student ID '${student.banner}' already exists!` };
  }

  const grade = calculationGrade(student.mark);
  
  names.push(student.name);
  surnames.push(student.surname);
  ages.push(student.age);
  marks.push(student.mark);
  grades.push(grade);
  banners.push(student.banner);

  saveStudents();
  return { success: true, message: `${student.name} ${student.surname} added successfully!` };
});

ipcMain.handle('delete-student', (event, index) => {
  if (index >= 0 && index < names.length) {
    const deletedName = `${names[index]} ${surnames[index]}`;
    
    names.splice(index, 1);
    surnames.splice(index, 1);
    ages.splice(index, 1);
    marks.splice(index, 1);
    grades.splice(index, 1);
    banners.splice(index, 1);

    saveStudents();
    return { success: true, message: `${deletedName} deleted!` };
  }
  return { success: false, message: 'Invalid student number!' };
});

ipcMain.handle('search-student', (event, searchType, searchValue) => {
  const results = [];
  
  if (searchType === 'surname') {
    for (let i = 0; i < surnames.length; i++) {
      if (surnames[i].toLowerCase() === searchValue.toLowerCase()) {
        results.push({
          index: i,
          name: names[i],
          surname: surnames[i],
          age: ages[i],
          mark: marks[i],
          grade: grades[i],
          banner: banners[i]
        });
      }
    }
  } else if (searchType === 'banner') {
    for (let i = 0; i < banners.length; i++) {
      if (banners[i].toLowerCase() === searchValue.toLowerCase()) {
        results.push({
          index: i,
          name: names[i],
          surname: surnames[i],
          age: ages[i],
          mark: marks[i],
          grade: grades[i],
          banner: banners[i]
        });
      }
    }
  }
  
  return results;
});

ipcMain.handle('update-student', (event, banner, newMark) => {
  const index = banners.findIndex(b => b.toLowerCase() === banner.toLowerCase());
  if (index !== -1) {
    marks[index] = newMark;
    grades[index] = calculationGrade(newMark);
    saveStudents();
    return { success: true, message: `Updated! New mark: ${newMark} | New grade: ${grades[index]}` };
  }
  return { success: false, message: 'Student ID not found!' };
});

ipcMain.handle('get-stats', () => {
  if (names.length === 0) return null;

  // Find highest mark
  let highestIndex = 0;
  for (let i = 1; i < marks.length; i++) {
    if (marks[i] > marks[highestIndex]) highestIndex = i;
  }

  // Find lowest mark
  let lowestIndex = 0;
  for (let i = 1; i < marks.length; i++) {
    if (marks[i] < marks[lowestIndex]) lowestIndex = i;
  }

  // Find youngest
  let youngestIndex = 0;
  for (let i = 1; i < ages.length; i++) {
    if (ages[i] < ages[youngestIndex]) youngestIndex = i;
  }

  // Find eldest
  let eldestIndex = 0;
  for (let i = 1; i < ages.length; i++) {
    if (ages[i] > ages[eldestIndex]) eldestIndex = i;
  }

  // Calculate average
  const totalMarks = marks.reduce((sum, mark) => sum + mark, 0);
  const averageMark = totalMarks / marks.length;
  const averageGrade = calculationGrade(averageMark);

  // Calculate pass/fail
  const passCount = marks.filter(mark => mark >= 40).length;
  const failCount = marks.length - passCount;
  const passPercent = (passCount / marks.length) * 100;
  const failPercent = (failCount / marks.length) * 100;

  return {
    highest: {
      name: `${names[highestIndex]} ${surnames[highestIndex]}`,
      mark: marks[highestIndex],
      grade: grades[highestIndex]
    },
    lowest: {
      name: `${names[lowestIndex]} ${surnames[lowestIndex]}`,
      mark: marks[lowestIndex],
      grade: grades[lowestIndex]
    },
    youngest: {
      name: `${names[youngestIndex]} ${surnames[youngestIndex]}`,
      age: ages[youngestIndex]
    },
    eldest: {
      name: `${names[eldestIndex]} ${surnames[eldestIndex]}`,
      age: ages[eldestIndex]
    },
    average: {
      mark: averageMark.toFixed(1),
      grade: averageGrade
    },
    passFail: {
      passCount,
      failCount,
      passPercent: passPercent.toFixed(1),
      failPercent: failPercent.toFixed(1)
    }
  };
});

ipcMain.handle('get-grade-distribution', () => {
  if (names.length === 0) return {};

  const gradeCounts = {};
  const gradeOrder = ["A1", "A2", "A3", "B1", "B2", "C", "D", "E"];
  
  for (const grade of grades) {
    gradeCounts[grade] = (gradeCounts[grade] || 0) + 1;
  }

  const distribution = {};
  for (const grade of gradeOrder) {
    if (gradeCounts[grade]) {
      distribution[grade] = {
        count: gradeCounts[grade],
        percent: ((gradeCounts[grade] / grades.length) * 100).toFixed(1)
      };
    }
  }

  return distribution;
});