// Auth Endpoints
export const AUTH_ENDPOINTS = {
  LOGIN: '/auth/login',
  REGISTER: '/auth/register',
  LOGOUT: '/auth/logout',
  REFRESH: '/auth/refresh',
  ME: '/auth/me',
};

// Practice Endpoints
export const PRACTICE_ENDPOINTS = {
  GET_PROBLEM: '/practice/next',
  SUBMIT: '/practice/submit',
  GET_SUBMISSION: '/practice/submission/:id',
  LIST_PROBLEMS: '/practice/problems',
};

// Dashboard Endpoints
export const DASHBOARD_ENDPOINTS = {
  ANALYTICS: '/dashboard/analytics',
  SUBMISSIONS: '/dashboard/submissions',
  STATS: '/dashboard/stats',
  MASTERY: '/dashboard/mastery',
};

// User Endpoints
export const USER_ENDPOINTS = {
  PROFILE: '/user/profile',
  UPDATE_PROFILE: '/user/profile',
  PREFERENCES: '/user/preferences',
};
