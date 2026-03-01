import { Link, useNavigate } from 'react-router-dom';
import useAuth from '../../hooks/useAuth';

const Navbar = () => {
  const { user, logout, isAuthenticated } = useAuth();
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  return (
    <nav className="bg-slate-900 border-b border-slate-700 px-6 py-4">
      <div className="max-w-7xl mx-auto flex items-center justify-between">
        <Link to="/" className="text-xl font-bold text-cyan-400 hover:text-cyan-300">
          Ekagra.ai
        </Link>

        {isAuthenticated ? (
          <div className="flex items-center gap-6">
            <Link
              to="/practice"
              className="text-slate-300 hover:text-sky-400 transition-colors"
            >
              Practice
            </Link>
            <Link
              to="/dashboard"
              className="text-slate-300 hover:text-sky-400 transition-colors"
            >
              Dashboard
            </Link>

            <div className="flex items-center gap-4 pl-4 border-l border-slate-700">
              <span className="text-slate-400 text-sm">{user?.email}</span>
              <button
                onClick={handleLogout}
                className="px-4 py-2 bg-red-600 hover:bg-red-700 text-white rounded transition-colors text-sm"
              >
                Logout
              </button>
            </div>
          </div>
        ) : (
          <div className="flex gap-4">
            <Link
              to="/login"
              className="px-4 py-2 text-slate-300 hover:text-sky-400 transition-colors"
            >
              Login
            </Link>
            <Link
              to="/register"
              className="px-4 py-2 bg-cyan-600 hover:bg-cyan-700 text-white rounded transition-colors"
            >
              Register
            </Link>
          </div>
        )}
      </div>
    </nav>
  );
};

export default Navbar;
