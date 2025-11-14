const { contextBridge, ipcRenderer } = require('electron');

contextBridge.exposeInMainWorld('electronAPI', {
  getStudents: () => ipcRenderer.invoke('get-students'),
  addStudent: (student) => ipcRenderer.invoke('add-student', student),
  deleteStudent: (index) => ipcRenderer.invoke('delete-student', index),
  searchStudent: (searchType, searchValue) => ipcRenderer.invoke('search-student', searchType, searchValue),
  updateStudent: (banner, newMark) => ipcRenderer.invoke('update-student', banner, newMark),
  getStats: () => ipcRenderer.invoke('get-stats'),
  getGradeDistribution: () => ipcRenderer.invoke('get-grade-distribution')
});