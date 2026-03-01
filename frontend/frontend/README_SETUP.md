# Ekagra.ai Frontend

A production-level frontend for an Adaptive Python Practice Platform built with Vite, React, and modern web technologies.

## Tech Stack

- **Framework**: React 19 with Vite
- **Styling**: Tailwind CSS
- **Code Editor**: Monaco Editor (@monaco-editor/react)
- **Routing**: React Router DOM v7
- **HTTP Client**: Axios
- **State Management**: React Context API
- **Utilities**: date-fns for date formatting

## Project Structure

```
src/
├── routes/                 # Route configuration
│   └── AppRoutes.jsx       # Main routing setup
├── pages/                  # Page components
│   ├── Login.jsx          # Authentication page
│   ├── Register.jsx       # Registration page
│   ├── Practice.jsx       # Main practice interface
│   └── Dashboard.jsx      # Analytics dashboard
├── components/
│   ├── layout/            # Navigation & layout
│   │   ├── Navbar.jsx
│   │   └── ProtectedRoute.jsx
│   ├── auth/              # Authentication forms
│   │   └── AuthForm.jsx
│   ├── practice/          # Practice page components
│   │   ├── CodeEditor.jsx
│   │   ├── ProblemCard.jsx
│   │   ├── SubmissionResult.jsx
│   │   ├── TestCasePanel.jsx
│   │   ├── ModeSelector.jsx
│   │   └── Timer.jsx
│   └── dashboard/         # Dashboard components
│       ├── MasteryChart.jsx
│       ├── TopicBreakdown.jsx
│       ├── PerformanceStats.jsx
│       └── RecentSubmissions.jsx
├── services/              # API services
│   ├── api.js            # Axios instance & API calls
│   └── mockApi.js        # Mock data for development
├── context/              # React Context
│   ├── AuthContext.jsx
│   └── AuthContextObject.jsx
├── hooks/                # Custom hooks
│   ├── useAuth.js
│   ├── useProblem.js
│   └── useSubmission.js
├── utils/                # Utilities & constants
│   ├── constants.js
│   ├── helpers.js
│   └── apiEndpoints.js
├── styles/               # Global styles
│   ├── global.css       # Tailwind & base styles
│   └── layout.css       # Component utilities
└── App.jsx              # Root component
```

## Setup Instructions

### Prerequisites

- Node.js 18+ and npm

### Installation

1. **Clone and install dependencies**
   ```bash
   npm install
   ```

2. **Configure environment**
   ```bash
   # Copy example env file
   cp .env.example .env.local
   
   # Update VITE_API_BASE_URL if your backend runs on a different port
   ```

3. **Start development server**
   ```bash
   npm run dev
   ```

The app will be available at `http://localhost:5173`

## API Integration

The frontend expects a backend API at `http://localhost:5000/api` (configurable via `.env.local`)

### Required Endpoints

**Authentication:**
- `POST /auth/login` - Login user
- `POST /auth/register` - Register new user

**Practice:**
- `GET /practice/next?mode=adaptive` - Fetch next problem
- `POST /practice/submit` - Submit code solution

**Dashboard:**
- `GET /dashboard/analytics` - Get user analytics
- `GET /dashboard/submissions` - Get recent submissions

## Features

### ✅ Implemented

- **Authentication**: Login/Register with JWT token storage
- **Protected Routes**: Route protection for authenticated users
- **Practice Interface**:
  - Monaco code editor with Python syntax highlighting
  - Problem description panel with constraints & examples
  - Split-view layout (problem + editor)
  - Mode selector (Adaptive/Easy/Medium/Hard)
  - Code submission with result display
  - Test case panel
  - Optional timer
- **Dashboard**:
  - Topic mastery chart
  - Problem breakdown by topic
  - Performance metrics
  - Recent submissions list
- **Dark Theme**: Inspired by VS Code and LeetCode
- **Responsive Design**: Works on mobile, tablet, and desktop

## Styling

All styling uses **Tailwind CSS** with custom dark theme configuration:
- Primary color: Cyan (#06b6d4)
- Background: Slate-950 (#030712)
- Cards: Slate-900 (#0f172a)
- Borders: Slate-700 (#334155)

## Development

### Available Scripts

```bash
# Start dev server
npm run dev

# Build for production
npm run build

# Preview production build
npm preview

# Lint code
npm run lint
```

### Key Implementation Details

1. **State Management**: Uses React Context API for auth state
2. **API Calls**: All backend calls go through `services/api.js` with axios
3. **Error Handling**: All API errors caught and displayed to user
4. **Loading States**: Components show loading skeletons during fetch
5. **Code Editor**: Monaco editor with Python language support

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `VITE_API_BASE_URL` | Backend API base URL | `http://localhost:5000/api` |

## Browser Support

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## Performance Optimizations

- Lazy loaded components
- Optimized Monaco editor (minimap disabled)
- Image optimization
- CSS minification in production

## Production Build

```bash
npm run build
# Creates dist/ folder ready for deployment
```

Deploy to Vercel, Netlify, or any static host.

## Troubleshooting

### Monaco Editor issues

If the editor doesn't load, ensure your backend CORS is configured correctly.

### API connection errors

Check that:
1. Backend is running on the configured port
2. CORS headers are properly set
3. `.env.local` has correct API URL

### Tailwind styles not loading

Ensure `postcss` and `autoprefixer` are properly installed:
```bash
npm install postcss autoprefixer --save-dev
```

## Further Development

- [ ] Add PWA support
- [ ] Implement code formatting
- [ ] Add syntax error highlighting
- [ ] Implement collaborative coding
- [ ] Add problem bookmarking
- [ ] Implement discussion forum
- [ ] Add video explanations

## License

MIT
