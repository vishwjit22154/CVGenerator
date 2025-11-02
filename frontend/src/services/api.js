import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const coverLetterAPI = {
  // Health check
  async checkHealth() {
    const response = await api.get('/health');
    return response.data;
  },

  // Generate cover letter
  async generateCoverLetter(data) {
    const response = await api.post('/generate', data);
    return response.data;
  },

  // Export cover letter
  async exportCoverLetter(data, format) {
    const response = await api.post('/export', 
      { ...data, format },
      { responseType: 'blob' }
    );
    return response;
  },

  // Analyze keywords
  async analyzeKeywords(jobDescription, coverLetter) {
    const response = await api.post('/analyze-keywords', {
      job_description: jobDescription,
      cover_letter: coverLetter,
    });
    return response.data;
  },
};

export default api;

