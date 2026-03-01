import axios from 'axios';

// default backend address includes /api to match server prefixes
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://127.0.0.1:8000/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Request interceptor: Add JWT token
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// Response interceptor: Handle 401 errors
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      localStorage.removeItem('token');
      localStorage.removeItem('user');
      window.location.href = '/login';
    }
    return Promise.reject(error);
  }
);

// Auth API endpoints
export const authAPI = {
  login: (email, password) =>
    api.post('/auth/login', { email, password }),
  register: (email, password, name) =>
    api.post('/auth/register', { email, password, name }),
};

// Problems API endpoints
export const problemsAPI = {
  getAllProblems: (skip = 0, limit = 10, difficulty = null, topic = null) => {
    const params = new URLSearchParams();
    params.append('skip', skip);
    params.append('limit', limit);
    if (difficulty) params.append('difficulty_band', difficulty);
    if (topic) params.append('topic', topic);
    return api.get(`/problems?${params}`);
  },
  getProblem: (problemId) =>
    api.get(`/problems/${problemId}`),
};

// Submissions API endpoints
export const submissionAPI = {
  submitCode: (problemId, userId, code, language = 'python') =>
    // include trailing slash to avoid fastapi redirect (avoids 307/405 issues)
    api.post('/submissions/', {
      problem_id: problemId,
      user_id: userId,
      code,
      language,
    }),
  getUserSubmissions: (userId) =>
    api.get(`/submissions/user/${userId}`),
};

// Dashboard API endpoints
export const dashboardAPI = {
  getStats: (userId) =>
    api.get(`/dashboard/stats/${userId}`),
  getSkills: (userId) =>
    api.get(`/dashboard/skills/${userId}`),
  getPerformance: (userId) =>
    api.get(`/dashboard/performance/${userId}`),
  getChartData: (userId) =>
    api.get(`/dashboard/chart-data/${userId}`),
};

export default api;
