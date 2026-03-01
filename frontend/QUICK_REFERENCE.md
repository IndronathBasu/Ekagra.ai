# Quick Reference - Frontend Status & Integration Points

## Current Status: ✅ READY FOR BACKEND INTEGRATION

```
┌─────────────────────────────────────────┐
│  Frontend: 100% Complete ✅             │
│  Backend: Waiting for API ⏳            │
│  Integration Effort: ~25 minutes ⚡     │
└─────────────────────────────────────────┘
```

---

## What Works NOW (Without Backend)

```bash
npm run dev          # Start dev server at http://localhost:5173

# You can:
✅ Log in (accepts any email/password)
✅ Register (validates password format)
✅ See practice problems (random from mock data)
✅ Submit code (gets random 70% pass rate)
✅ View dashboard (shows mock analytics)
✅ Switch themes, navigate, use dark mode
✅ Everything is fully responsive
```

---

## What's Hardcoded

| Page | Feature | Current | When Backend Ready |
|------|---------|---------|---|
| Login | Auth | Any credentials accepted | Real password validation |
| Register | Auth | Random user ID | DB user creation + validation |
| Practice | Problems | Random from 2-item array | DB queries + adaptive algorithm |
| Practice | Submission | Random 70% pass rate | Real Python execution |
| Dashboard | Analytics | Mock JSON object | Database aggregations |

---

## Integration Commands (When Backend Ready)

### Step 1: Update Backend URL
```bash
# Edit .env.local
VITE_API_BASE_URL=http://localhost:5000/api
```

### Step 2: Swap These 4 Files
```javascript
// src/pages/Login.jsx (Line 4)
- Remove: // import { authAPI } from '../services/api';
+ Add:    import { authAPI } from '../services/api';

// src/pages/Register.jsx (Line 4)
- Remove: // import { authAPI } from '../services/api';
+ Add:    import { authAPI } from '../services/api';

// src/pages/Practice.jsx (Line 7)
- Remove: import mockApi from '../services/mockApi';
+ Add:    import { practiceAPI } from '../services/api';

// src/pages/Dashboard.jsx (Line 5)
- Remove: import mockApi from '../services/mockApi';
+ Add:    import { dashboardAPI } from '../services/api';
```

### Step 3: Test
```bash
npm run dev
# Try login with real credentials
# Practice problems should load from backend
# Submissions should return real results
```

---

## Required Backend Endpoints (6 Total)

```
Auth:
  POST   /auth/login              → { user, token }
  POST   /auth/register           → { user, token }

Practice:
  GET    /practice/next?mode=X    → { id, title, description, testCases, ... }
  POST   /practice/submit         → { status, message, stats, testCaseResults }

Dashboard:
  GET    /dashboard/analytics     → { problemsSolved, accuracy, masteryData, ... }
  GET    /dashboard/submissions   → [ { id, problemTitle, status, ... } ]
```

**Full Specs**: See [BACKEND_INTEGRATION_GUIDE.md](BACKEND_INTEGRATION_GUIDE.md)

---

## Architecture Diagram

```
┌─────────────────────────────────────────────────────┐
│                React Application                     │
├─────────────────────────────────────────────────────┤
│                                                      │
│  ┌──────────────┐  ┌──────────────┐ ┌────────────┐ │
│  │   Pages      │  │  Components  │ │  Context   │ │
│  ├──────────────┤  ├──────────────┤ ├────────────┤ │
│  │ Login        │  │ CodeEditor   │ │ AuthCtx    │ │
│  │ Register     │  │ ProblemCard  │ │ useAuth    │ │
│  │ Practice     │  │ Dashboard    │ │            │ │
│  │ Dashboard    │  │ ...          │ │            │ │
│  └──────────────┘  └──────────────┘ └────────────┘ │
│         ↓                ↓                  ↓       │
│  ┌─────────────────────────────────────────────┐   │
│  │  Services Layer                             │   │
│  ├──────────────────────────────────────────┤   │
│  │  api.js (REAL API)                       │   │
│  │  ├─ authAPI.login()                      │   │
│  │  ├─ authAPI.register()                   │   │
│  │  ├─ practiceAPI.getNextProblem()         │   │
│  │  ├─ practiceAPI.submitCode()             │   │
│  │  ├─ dashboardAPI.getAnalytics()          │   │
│  │  └─ dashboardAPI.getRecentSubmissions()  │   │
│  │  mockApi.js (CURRENT - Used during dev)  │   │
│  └─────────────────────────────────────────┘   │
│               ↓                                  │
│  ┌─────────────────────────────────┐            │
│  │  Axios Instance                 │            │
│  │  (JWT Interceptor)              │            │
│  │  Adds: Authorization: Bearer {token}         │
│  └─────────────────────────────────┘            │
│               ↓                                  │
└─────────────────────────────────────────────────┘
         ↓
    BACKEND API (Running on port 5000)
         ↓
    DATABASE
```

---

## File Structure

```
frontend/
├── src/
│   ├── pages/              # 4 pages (Login, Register, Practice, Dashboard)
│   ├── components/         # 16+ components (CodeEditor, ProblemCard, etc)
│   ├── services/
│   │   ├── api.js          # ← READY FOR BACKEND (just uncomment imports)
│   │   └── mockApi.js      # Currently used in dev
│   ├── context/            # Auth state management
│   ├── hooks/              # Custom hooks (useAuth, useProblem, useSubmission)
│   ├── utils/              # Helpers, constants, endpoints
│   ├── styles/             # Tailwind + custom CSS
│   ├── App.jsx             # Root component with Router
│   └── main.jsx            # Entry point
├── public/                 # Static files
├── tailwind.config.js      # Tailwind theme (dark mode)
├── vite.config.js          # Build config
├── package.json
└── README.md
```

---

## Development Commands

```bash
# Install dependencies (first time only)
npm install

# Start dev server (http://localhost:5173)
npm run dev

# Production build
npm run build

# Preview production build
npm run preview

# Lint code
npm run lint

# Format code (setup manually if needed)
npx prettier --write src/
```

---

## Tech Stack

| Technology | Version | Purpose |
|------------|---------|---------|
| React | 19 | UI Framework |
| Vite | 7.3 | Build Tool |
| React Router | 7.13 | Routing |
| Tailwind CSS | 3.3 | Styling (Dark theme) |
| Monaco Editor | Latest | Python Code Editor |
| Axios | 1.13 | HTTP Client |
| date-fns | 2.30 | Date Formatting |

---

## Key Features

### ✅ Authentication
- Login/Register forms with validation
- JWT token storage in localStorage
- Protected routes (redirect to /login if not authenticated)
- Auto-logout on token expiration (when backend added)

### ✅ Code Editor
- Monaco Editor (same as VS Code)
- Python syntax highlighting
- Dark theme (vs-dark)
- Responsive height

### ✅ Problem Display
- Title, difficulty, topic badges
- Full description with formatting
- Constraints and examples
- Test case panel

### ✅ Dashboard
- Performance stats (4 cards)
- Topic mastery charts
- Recent submissions list
- Responsive grid layout

### ✅ Responsive Design
- Mobile (≤640px)
- Tablet (641-1024px)
- Desktop (≥1025px)

---

## Environment Variables

```bash
# .env.local
VITE_API_BASE_URL=http://localhost:5000/api   # Backend URL (change this for integration)
```

---

## API Interceptor (Already Configured)

```javascript
// In api.js - Axios automatically:
1. Reads JWT token from localStorage['auth_token']
2. Adds to every request: Authorization: Bearer {token}
3. Handles 401 responses (token expired)
4. Adds content-type: application/json to requests
```

---

## Error Handling

```javascript
// Frontend handles these error scenarios:
❌ Missing credentials           → "Email and password required"
❌ Invalid credentials            → From backend: "Invalid email or password"
❌ Email already exists           → From backend: "Email already exists"
❌ Network error                  → "Request failed. Check connection."
❌ Submission timeout             → "Request took too long"
❌ Invalid code format            → "Code has syntax errors"
❌ Runtime error                  → Shows error message from backend
❌ Time limit exceeded            → "Execution took too long"
```

---

## Testing Checklist

### Before Integration
- [ ] `npm run dev` starts without errors
- [ ] Can login with any credentials
- [ ] Can register a new account
- [ ] Can load practice problems
- [ ] Can submit code (gets random result)
- [ ] Can view dashboard

### After Backend Integration
- [ ] Login fails with wrong password
- [ ] Register fails if email exists
- [ ] Register fails if password < 6 chars
- [ ] Problems load from database
- [ ] Code submission returns real results
- [ ] Dashboard shows real analytics
- [ ] Token persists after page refresh
- [ ] Logout clears token

---

## Build Information

### Development Build
```
Size: ~340 KB total
Gzipped: ~107 KB
Dependencies: React, Router, Axios, Tailwind, Monaco
Build time: ~2 seconds
```

### Production Build
```bash
npm run build
# Creates dist/ folder with optimized files
# Size: Minimal due to tree-shaking
# Ready to deploy to any static host
```

---

## Common Issues & Solutions

### Issue: "Cannot find module 'api'"
**Solution**: Make sure `src/services/api.js` exists and imports are correct

### Issue: "Localhost port already in use"
**Solution**: Kill process on port 5173 or use `npm run dev -- --port 3000`

### Issue: "Token not sending in requests"
**Solution**: Verify localStorage has `auth_token` key after login

### Issue: "CORS error from backend"
**Solution**: Backend must include `Access-Control-Allow-Origin: http://localhost:5173`

### Issue: "Code editor not loading"
**Solution**: Verify Monaco Editor package installed: `npm list @monaco-editor/react`

---

## Next Steps

1. **Now**: Application is ready for frontend team to use/enhance
2. **Backend Team**: Implement 6 API endpoints from [BACKEND_INTEGRATION_GUIDE.md](BACKEND_INTEGRATION_GUIDE.md)
3. **Integration**: Update 4 files with new imports (~25 minutes total)
4. **Testing**: Run full test suite on staging
5. **Production**: Deploy both frontend and backend together

---

## Support & Documentation

| Document | Purpose |
|----------|---------|
| [TECHNICAL_DOCUMENTATION.md](TECHNICAL_DOCUMENTATION.md) | Complete technical specs of every file |
| [BACKEND_INTEGRATION_GUIDE.md](BACKEND_INTEGRATION_GUIDE.md) | Step-by-step backend integration with code examples |
| [README.md](README.md) | Project setup and getting started guide |
| This file | Quick reference for status and integration |

---

## Questions?

- **Frontend issues**: Check `npm run dev` console for errors
- **Backend specs**: See BACKEND_INTEGRATION_GUIDE.md sections 3.1-3.5
- **Component usage**: Check individual component files in `src/components/`
- **API integration**: See api.js and BACKEND_INTEGRATION_GUIDE.md testing section

**Last Updated**: February 27, 2026  
**Version**: 1.0  
**Status**: ✅ Production Ready (Waiting for Backend)
