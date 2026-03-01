# Backend Integration Guide - Transition from Mock to Real API

**Document Purpose**: Clear guide showing exactly what's hardcoded NOW and what will change when backend API is connected.

---

## Executive Summary

| Aspect | Current State (Mock) | When Backend Ready | Effort |
|--------|-------------------|------------------|--------|
| Data Source | Hardcoded arrays in mockApi.js | Real database via API | Swap 3-4 imports |
| Authentication | Accepts any credentials | Real password validation | 5 min change |
| Problem Fetching | Random from array | DB query via API | 5 min change |
| Code Submission | Random 70% pass rate | Real code execution | 5 min change |
| Dashboard | Mock analytics | Database aggregations | 5 min change |
| **Total Readiness** | ✅ 100% | ⏳ Waiting for backend endpoints | - |

---

## Current State - What's Hardcoded

### 1. Login - HARDCODED
**File**: `src/pages/Login.jsx` (Lines 14-31)

#### ❌ CURRENT CODE (Hardcoded)
```javascript
const handleSubmit = async (e) => {
  e.preventDefault();
  setError('');
  setLoading(true);

  try {
    // Simulates API call delay
    await new Promise(resolve => setTimeout(resolve, 500));

    // HARDCODED: Accepts ANY email/password
    if (!email || !password) {
      throw new Error('Email and password are required');
    }

    // HARDCODED: Creates random user ID
    const mockUser = {
      id: Math.random().toString(36).substr(2, 9),
      email,
      name: email.split('@')[0],
    };

    // HARDCODED: Mock JWT token
    const mockToken = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ';

    login(mockUser, mockToken);
    navigate('/practice');
  } catch (err) {
    setError(err.message || 'Login failed. Please try again.');
  } finally {
    setLoading(false);
  }
};
```

#### ✅ WHEN BACKEND READY
```javascript
import { authAPI } from '../services/api';  // ← Just uncomment this

const handleSubmit = async (e) => {
  e.preventDefault();
  setError('');
  setLoading(true);

  try {
    // REAL: Calls actual backend
    const response = await authAPI.login(email, password);
    const { user, token } = response.data;

    login(user, token);
    navigate('/practice');
  } catch (err) {
    setError(err.response?.data?.message || 'Login failed. Please try again.');
  } finally {
    setLoading(false);
  }
};
```

**Required Backend Endpoint**:
```
POST /auth/login
Request:  { email: "user@example.com", password: "password123" }
Response: { 
  user: { id: 1, email: "user@example.com", name: "John" },
  token: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
Status Code: 200 (success) or 401 (invalid credentials)
```

---

### 2. Register - HARDCODED
**File**: `src/pages/Register.jsx` (Lines 18-40)

#### ❌ CURRENT CODE (Hardcoded)
```javascript
const handleSubmit = async (e) => {
  e.preventDefault();
  setError('');

  if (password !== confirmPassword) {
    setError('Passwords do not match');
    return;
  }

  if (password.length < 6) {
    setError('Password must be at least 6 characters');
    return;
  }

  setLoading(true);

  try {
    // Simulates API call delay
    await new Promise(resolve => setTimeout(resolve, 500));

    // HARDCODED: Creates random user
    const mockUser = {
      id: Math.random().toString(36).substr(2, 9),
      email,
      name: name || email.split('@')[0],
    };

    // HARDCODED: Mock JWT token
    const mockToken = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ';

    login(mockUser, mockToken);
    navigate('/practice');
  } catch (err) {
    setError(err.message || 'Registration failed. Please try again.');
  } finally {
    setLoading(false);
  }
};
```

#### ✅ WHEN BACKEND READY
```javascript
import { authAPI } from '../services/api';  // ← Just uncomment this

const handleSubmit = async (e) => {
  e.preventDefault();
  setError('');

  if (password !== confirmPassword) {
    setError('Passwords do not match');
    return;
  }

  if (password.length < 6) {
    setError('Password must be at least 6 characters');
    return;
  }

  setLoading(true);

  try {
    // REAL: Calls actual backend
    const response = await authAPI.register(email, password, name);
    const { user, token } = response.data;

    login(user, token);
    navigate('/practice');
  } catch (err) {
    setError(err.response?.data?.message || 'Registration failed. Please try again.');
  } finally {
    setLoading(false);
  }
};
```

**Required Backend Endpoint**:
```
POST /auth/register
Request:  {
  email: "newuser@example.com",
  password: "password123",
  name: "New User"
}
Response: {
  user: { id: 2, email: "newuser@example.com", name: "New User" },
  token: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
Status Code: 201 (created) or 400 (email exists)
```

---

### 3. Practice Page - Problem Loading - HARDCODED
**File**: `src/pages/Practice.jsx` (Lines 32-51)

#### ❌ CURRENT CODE (Hardcoded)
```javascript
const loadProblem = async () => {
  setLoading(true);
  setResult(null);
  setTestCases([]);

  try {
    // Simulates API delay
    await new Promise(resolve => setTimeout(resolve, 300));

    // HARDCODED: Picks random problem from array
    const problemData = mockProblems[
      Math.floor(Math.random() * mockProblems.length)
    ];

    setProblem(problemData);
    setCode(problemData.boilerplate || '# Write your solution here\n');
    setTestCases(problemData.testCases || []);
  } catch (error) {
    console.error('Failed to load problem:', error);
    setResult({
      status: 'error',
      message: 'Failed to load problem. Please try again.',
    });
  } finally {
    setLoading(false);
  }
};
```

#### ✅ WHEN BACKEND READY
```javascript
import { practiceAPI } from '../services/api';  // ← Change import

const loadProblem = async () => {
  setLoading(true);
  setResult(null);
  setTestCases([]);

  try {
    // REAL: Calls backend API passing the mode
    const response = await practiceAPI.getNextProblem(mode);
    const problemData = response.data;

    setProblem(problemData);
    setCode(problemData.boilerplate || '# Write your solution here\n');
    setTestCases(problemData.testCases || []);
  } catch (error) {
    console.error('Failed to load problem:', error);
    setResult({
      status: 'error',
      message: 'Failed to load problem. Please try again.',
    });
  } finally {
    setLoading(false);
  }
};
```

**Required Backend Endpoint**:
```
GET /practice/next?mode=adaptive

Query Parameters:
  mode: 'adaptive' | 'easy' | 'medium' | 'hard'

Response: {
  id: 1,
  title: "Two Sum",
  difficulty: "Easy",
  topic: "Array",
  description: "Given an array of integers nums and an integer target, return the indices of the two numbers that add up to target.",
  constraints: [
    "2 <= nums.length <= 10^4",
    "-10^9 <= nums[i] <= 10^9",
    "-10^9 <= target <= 10^9"
  ],
  examples: [
    {
      input: "nums = [2,7,11,15], target = 9",
      output: "[0,1]"
    }
  ],
  boilerplate: "def twoSum(nums, target):\n    pass",
  timeLimit: 1,
  testCases: [
    {
      input: "[2,7,11,15], 9",
      expectedOutput: "[0,1]"
    },
    {
      input: "[3,2,4], 6",
      expectedOutput: "[1,2]"
    }
  ]
}
```

---

### 4. Practice Page - Code Submission - HARDCODED
**File**: `src/pages/Practice.jsx` (Lines 54-115)

#### ❌ CURRENT CODE (Hardcoded - Random 70% Pass Rate)
```javascript
const handleSubmit = async () => {
  if (!problem || !code.trim()) {
    setResult({
      status: 'error',
      message: 'Please write some code before submitting.',
    });
    return;
  }

  setSubmitting(true);

  try {
    // Simulates API delay
    await new Promise(resolve => setTimeout(resolve, 800));

    // HARDCODED: Random decision (70% accept, 30% reject)
    const isAccepted = Math.random() > 0.3;

    if (isAccepted) {
      setResult({
        status: 'accepted',
        message: 'All test cases passed!',
        stats: {
          // HARDCODED: Random values
          runtime: Math.floor(Math.random() * 100) + 10 + 'ms',
          memory: (Math.random() * 10 + 5).toFixed(1) + 'MB',
          passed: problem.testCases?.length || 3,
          total: problem.testCases?.length || 3,
        },
      });

      if (testCases.length > 0) {
        setTestCases((prev) =>
          prev.map((testCase) => ({
            ...testCase,
            status: 'passed',
            actualOutput: testCase.expectedOutput,
          }))
        );
      }
    } else {
      // HARDCODED: Mock failure
      const failedIdx = Math.floor(Math.random() * (problem.testCases?.length || 3));
      setResult({
        status: 'wrong_answer',
        message: `Wrong Answer on test case ${failedIdx + 1}`,
        stats: {
          runtime: Math.floor(Math.random() * 100) + 10 + 'ms',
          memory: (Math.random() * 10 + 5).toFixed(1) + 'MB',
          passed: failedIdx,
          total: problem.testCases?.length || 3,
        },
      });

      if (testCases.length > 0) {
        setTestCases((prev) =>
          prev.map((testCase, idx) => ({
            ...testCase,
            status: idx < failedIdx ? 'passed' : 'failed',
            actualOutput: idx < failedIdx ? testCase.expectedOutput : 'wrong output',
          }))
        );
      }
    }
  } catch (error) {
    console.error('Submission failed:', error);
    setResult({
      status: 'error',
      message: 'Submission failed. Please try again.',
    });
  } finally {
    setSubmitting(false);
  }
};
```

#### ✅ WHEN BACKEND READY
```javascript
import { practiceAPI } from '../services/api';  // ← Change import

const handleSubmit = async () => {
  if (!problem || !code.trim()) {
    setResult({
      status: 'error',
      message: 'Please write some code before submitting.',
    });
    return;
  }

  setSubmitting(true);

  try {
    // REAL: Sends code to backend for execution
    const response = await practiceAPI.submitCode(problem.id, code);
    const submissionResult = response.data;

    setResult({
      status: submissionResult.status,
      message: submissionResult.message,
      error: submissionResult.error,
      stats: {
        runtime: submissionResult.runtime,
        memory: submissionResult.memory,
        passed: submissionResult.passedTests,
        total: submissionResult.totalTests,
      },
    });

    // Update test cases with actual results
    if (submissionResult.testCaseResults) {
      setTestCases((prev) =>
        prev.map((testCase, idx) => ({
          ...testCase,
          status: submissionResult.testCaseResults[idx]?.status,
          actualOutput: submissionResult.testCaseResults[idx]?.output,
        }))
      );
    }
  } catch (error) {
    console.error('Submission failed:', error);
    setResult({
      status: 'error',
      message: error.response?.data?.message || 'Submission failed. Please try again.',
      error: error.response?.data?.error,
    });
  } finally {
    setSubmitting(false);
  }
};
```

**Required Backend Endpoint**:
```
POST /practice/submit

Request: {
  problemId: 1,
  code: "def twoSum(nums, target):\n    for i in range(len(nums)):\n        for j in range(i+1, len(nums)):\n            if nums[i] + nums[j] == target:\n                return [i, j]",
  language: "python"
}

Response: {
  status: "accepted" | "wrong_answer" | "runtime_error" | "time_limit_exceeded",
  message: "All test cases passed!" | "Wrong Answer on test case 1",
  runtime: "42ms",
  memory: "12.2MB",
  passedTests: 3,
  totalTests: 3,
  testCaseResults: [
    {
      status: "passed" | "failed",
      input: "[2,7,11,15], 9",
      expectedOutput: "[0,1]",
      output: "[0,1]"
    }
  ],
  error: null | "Runtime Error: ....."
}

Status Codes:
  200: Execution successful
  400: Invalid code format
  500: Server error during execution
```

---

### 5. Dashboard Page - HARDCODED
**File**: `src/pages/Dashboard.jsx` (Lines 16-42)

#### ❌ CURRENT CODE (Hardcoded)
```javascript
const fetchAnalytics = async () => {
  setLoading(true);
  setError(null);

  try {
    // Simulates API delay
    await new Promise(resolve => setTimeout(resolve, 300));

    // HARDCODED: Uses mock analytics
    setAnalytics({
      ...mockAnalytics,
      recentSubmissions: [
        {
          id: 1,
          problemTitle: 'Two Sum',
          difficulty: 'Easy',
          status: 'accepted',
          runtime: '42ms',
          timestamp: new Date(Date.now() - 3600000),
        },
        {
          id: 2,
          problemTitle: 'Reverse String',
          difficulty: 'Easy',
          status: 'accepted',
          runtime: '58ms',
          timestamp: new Date(Date.now() - 7200000),
        },
        {
          id: 3,
          problemTitle: 'Palindrome Check',
          difficulty: 'Medium',
          status: 'wrong_answer',
          runtime: '120ms',
          timestamp: new Date(Date.now() - 10800000),
        },
      ],
    });
  } catch (err) {
    console.error('Failed to fetch analytics:', err);
    setError('Failed to load dashboard. Please try again.');
  } finally {
    setLoading(false);
  }
};
```

#### ✅ WHEN BACKEND READY
```javascript
import { dashboardAPI } from '../services/api';  // ← Change import

const fetchAnalytics = async () => {
  setLoading(true);
  setError(null);

  try {
    // REAL: Calls backend for analytics and submissions
    const [analyticsRes, submissionsRes] = await Promise.all([
      dashboardAPI.getAnalytics(),
      dashboardAPI.getRecentSubmissions(10),
    ]);

    setAnalytics({
      ...analyticsRes.data,
      recentSubmissions: submissionsRes.data,
    });
  } catch (err) {
    console.error('Failed to fetch analytics:', err);
    setError('Failed to load dashboard. Please try again.');
  } finally {
    setLoading(false);
  }
};
```

**Required Backend Endpoints**:
```
GET /dashboard/analytics

Response: {
  problemsSolved: 42,
  accuracy: 78,
  avgTime: 12.5,
  streak: 7,
  masteryData: [
    { topic: "Array", score: 85 },
    { topic: "String", score: 72 },
    { topic: "Tree", score: 68 },
    { topic: "Graph", score: 45 },
    { topic: "DP", score: 92 }
  ],
  topicBreakdown: [
    { topic: "Array", count: 24, color: "bg-blue-500" },
    { topic: "String", count: 18, color: "bg-green-500" },
    ...
  ],
  performanceStats: {
    successRate: 78,
    avgAttempts: 1.8,
    bestScore: 95,
    averageScore: 72
  }
}

---

GET /dashboard/submissions?limit=10

Response: [
  {
    id: 1,
    problemTitle: "Two Sum",
    difficulty: "Easy",
    status: "accepted",
    runtime: "42ms",
    timestamp: "2026-02-27T10:30:00Z"
  },
  {
    id: 2,
    problemTitle: "Reverse String",
    difficulty: "Easy",
    status: "accepted",
    runtime: "58ms",
    timestamp: "2026-02-27T09:30:00Z"
  },
  ...
]
```

---

## Migration Checklist

### Phase 1: Backend Setup (Backend Team)
- [ ] Implement `/auth/login` endpoint
- [ ] Implement `/auth/register` endpoint  
- [ ] Implement `/practice/next?mode=adaptive` endpoint
- [ ] Implement `/practice/submit` endpoint
- [ ] Implement `/dashboard/analytics` endpoint
- [ ] Implement `/dashboard/submissions?limit=10` endpoint
- [ ] Set up CORS to allow requests from `http://localhost:5173`
- [ ] Test all endpoints with Postman

### Phase 2: Environment Setup (Frontend & DevOps)
- [ ] Update `.env.local` with backend URL
- [ ] Verify backend is running on port 5000
- [ ] Test API connectivity

### Phase 3: Code Changes (Frontend Team)
- [ ] Replace imports in `Login.jsx` (Line 4)
- [ ] Replace imports in `Register.jsx` (Line 4)
- [ ] Replace imports in `Practice.jsx` (Line 7)
- [ ] Replace imports in `Dashboard.jsx` (Line 5)
- [ ] Test login flow with real credentials
- [ ] Test problem loading and submission
- [ ] Test dashboard analytics

### Phase 4: Testing (QA Team)
- [ ] Test login with valid/invalid credentials
- [ ] Test register with duplicate email
- [ ] Test problem fetching in all modes
- [ ] Test code submission with various responses
- [ ] Test dashboard data aggregation
- [ ] Test error handling for API failures
- [ ] Test token persistence and refresh
- [ ] Test protected route redirects

### Phase 5: Deployment
- [ ] Build production version
- [ ] Deploy to staging environment
- [ ] Final testing on staging
- [ ] Deploy to production

---

## Files Ready Waiting for Backend

| File | Current Status | Change Required | Estimated Time |
|------|---|---|---|
| `src/pages/Login.jsx` | Using mock | Change import + swap code block | 5 min |
| `src/pages/Register.jsx` | Using mock | Change import + swap code block | 5 min |
| `src/pages/Practice.jsx` | Using mock | Change import (2 places) + swap code blocks | 10 min |
| `src/pages/Dashboard.jsx` | Using mock | Change import + swap code block | 5 min |
| `src/services/api.js` | Ready | No changes needed | 0 min |
| `src/hooks/useProblem.js` | Ready | No changes needed | 0 min |
| `src/hooks/useSubmission.js` | Ready | No changes needed | 0 min |
| `src/context/AuthContext.jsx` | Ready | No changes needed | 0 min |

**Total Migration Time**: ~25 minutes

---

## Testing Script for Backend Integration

Once backend is ready, use this script to verify everything works:

```javascript
// Test login
POST http://localhost:5000/api/auth/login
{
  "email": "test@example.com",
  "password": "password123"
}
Expected: { user: {...}, token: "..." }

// Test get problem
GET http://localhost:5000/api/practice/next?mode=adaptive
Authorization: Bearer {token}
Expected: { id: 1, title: "...", ... }

// Test submit code
POST http://localhost:5000/api/practice/submit
Authorization: Bearer {token}
{
  "problemId": 1,
  "code": "def twoSum(nums, target):\n    return [0, 1]",
  "language": "python"
}
Expected: { status: "accepted", message: "...", ... }

// Test analytics
GET http://localhost:5000/api/dashboard/analytics
Authorization: Bearer {token}
Expected: { problemsSolved: 42, accuracy: 78, ... }
```

---

## Error Handling Guide

When backend is connected, expect these possible errors:

### 401 Unauthorized
```json
{
  "error": "Invalid credentials",
  "code": "INVALID_CREDENTIALS"
}
```
**Frontend Handled By**: Error message in red banner

### 400 Bad Request
```json
{
  "error": "Email already exists",
  "code": "EMAIL_EXISTS"
}
```
**Frontend Handled By**: Error message in form

### 500 Server Error
```json
{
  "error": "Internal server error",
  "code": "SERVER_ERROR"
}
```
**Frontend Handled By**: Generic error message + console log

### Network Timeout
```
Error: timeout of 30000ms exceeded
```
**Frontend Handled By**: "Request timeout" error message

---

## Performance Considerations

### Current (Mock)
- Database fetches: None (hardcoded)
- API latency: ~300-800ms (simulated)
- Load time: <100ms (instant)

### When Backend Connected
- Database fetches: Actual DB queries required
- API latency: Network dependent (typically 100-500ms)
- Load time: Database + serialization

**Recommendations for Backend**:
1. Add database indexes on frequently queried fields
2. Implement query pagination for submissions list
3. Cache analytics data with TTL
4. Use connection pooling for database
5. Implement API rate limiting to prevent abuse

---

## Rollback Plan

If backend integration fails:

1. Revert imports back to mock data
2. Check backend error logs
3. Verify endpoint responses match spec
4. Test individual endpoints with Postman
5. Check JWT token format and validation
6. Verify CORS headers on backend

---

## Summary

**What's Done** ✅
- 100% frontend UI/UX complete
- All components built and tested
- Routing configured
- State management working
- Mock data provides full testing

**What's Waiting** ⏳
- Backend API endpoints (6 endpoints needed)
- Real database integration
- Code execution environment

**Time to Production** ⏱️
- Backend implementation: Backend team's estimate
- Frontend integration: ~25 minutes
- Testing & QA: ~2-3 days

**Risk Level**: 🟢 **LOW**
- Clean separation makes swapping easy
- No frontend architectural changes needed
- Simple find/replace for imports

---

**Document Version**: 1.0  
**Created**: February 27, 2026  
**For**: Engineering Team, Project Managers, DevOps
