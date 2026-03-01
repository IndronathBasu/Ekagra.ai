import { useState, useEffect } from "react";
import { AuthContext } from "./AuthContextObject";

// Prototype mode: Auto-login with dev user
const DEV_USER = {
  id: 1,  // Frontend expects 'id' not 'user_id'
  user_id: 1,  // Keep both for compatibility
  email: "dev@example.com",
  name: "Dev User",
};
const DEV_TOKEN = "prototype-token"; // Not used when DISABLE_AUTH=true

export function AuthProvider({ children }) {
  // Auto-login with dev user for prototype
  const [user, setUser] = useState(() => {
    const storedUser = localStorage.getItem("user");
    if (storedUser) {
      return JSON.parse(storedUser);
    }
    // Auto-set dev user for prototype
    localStorage.setItem("user", JSON.stringify(DEV_USER));
    return DEV_USER;
  });
  
  const [token, setToken] = useState(() => {
    const storedToken = localStorage.getItem("token");
    if (storedToken) {
      return storedToken;
    }
    // Auto-set dev token for prototype
    localStorage.setItem("token", DEV_TOKEN);
    return DEV_TOKEN;
  });

  // Ensure dev user is always set on mount
  useEffect(() => {
    if (!user || user.user_id !== 1) {
      setUser(DEV_USER);
      localStorage.setItem("user", JSON.stringify(DEV_USER));
    }
    if (!token) {
      setToken(DEV_TOKEN);
      localStorage.setItem("token", DEV_TOKEN);
    }
  }, []);

  const login = (userData, authToken) => {
    setUser(userData);
    setToken(authToken);
    localStorage.setItem("token", authToken);
    localStorage.setItem("user", JSON.stringify(userData));
  };

  const logout = () => {
    // In prototype mode, logout just re-logs in as dev user
    setUser(DEV_USER);
    setToken(DEV_TOKEN);
    localStorage.setItem("token", DEV_TOKEN);
    localStorage.setItem("user", JSON.stringify(DEV_USER));
  };

  return (
    <AuthContext.Provider
      value={{
        user,
        token,
        login,
        logout,
        isAuthenticated: true, // Always authenticated in prototype mode
      }}
    >
      {children}
    </AuthContext.Provider>
  );
}