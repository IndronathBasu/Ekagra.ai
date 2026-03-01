import { Routes, Route, Navigate } from 'react-router-dom';
import Navbar from '../components/layout/Navbar';
import ProtectedRoute from '../components/layout/ProtectedRoute';
import Login from '../pages/Login';
import Register from '../pages/Register';
import Practice from '../pages/Practice';
import Dashboard from '../pages/Dashboard';

const AppRoutes = () => {
  return (
    <>
      <Navbar />
      <Routes>
        {/* Auth Routes */}
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />

        {/* Protected Routes */}
        <Route
          path="/practice"
          element={
            <ProtectedRoute>
              <Practice />
            </ProtectedRoute>
          }
        />
        <Route
          path="/dashboard"
          element={
            <ProtectedRoute>
              <Dashboard />
            </ProtectedRoute>
          }
        />

        {/* Default Redirect - Skip login in prototype mode */}
        <Route path="/" element={<Navigate to="/practice" replace />} />
        <Route path="/login" element={<Navigate to="/practice" replace />} />
        <Route path="*" element={<Navigate to="/practice" replace />} />
      </Routes>
    </>
  );
};

export default AppRoutes;
