import { useState, useCallback } from 'react';
import { practiceAPI } from '../services/api';

const useProblem = () => {
  const [problem, setProblem] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const fetchProblem = useCallback(async (mode = 'adaptive') => {
    setLoading(true);
    setError(null);
    try {
      const { data } = await practiceAPI.getNextProblem(mode);
      setProblem(data);
      return data;
    } catch (err) {
      setError(err.message);
      throw err;
    } finally {
      setLoading(false);
    }
  }, []);

  return { problem, setProblem, loading, error, fetchProblem };
};

export default useProblem;
