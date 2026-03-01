// API Configuration
export const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:5000/api';

// Practice Modes
export const PRACTICE_MODES = {
  ADAPTIVE: 'adaptive',
  EASY: 'easy',
  MEDIUM: 'medium',
  HARD: 'hard',
};

// Difficulty Levels
export const DIFFICULTY_LEVELS = {
  EASY: 'Easy',
  MEDIUM: 'Medium',
  HARD: 'Hard',
};

// Submission Status
export const SUBMISSION_STATUS = {
  ACCEPTED: 'accepted',
  WRONG_ANSWER: 'wrong_answer',
  TIME_LIMIT_EXCEEDED: 'time_limit_exceeded',
  RUNTIME_ERROR: 'runtime_error',
  COMPILATION_ERROR: 'compilation_error',
  PENDING: 'pending',
};

// Languages
export const PROGRAMMING_LANGUAGES = {
  PYTHON: 'python',
  JAVASCRIPT: 'javascript',
  JAVA: 'java',
  CPP: 'cpp',
};

// UI Constants
export const EDITOR_HEIGHT = '500px';
export const EDITOR_THEME = 'vs-dark';
export const EDITOR_LANGUAGE = 'python';
