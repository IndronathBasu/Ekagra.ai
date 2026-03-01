import { useState, useCallback } from 'react';
import { practiceAPI } from '../services/api';

const useSubmission = () => {
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const submit = useCallback(async (problemId, code) => {
    setLoading(true);
    setError(null);
    try {
      const { data } = await practiceAPI.submitCode(problemId, code);
      setResult(data);
      return data;
    } catch (err) {
      const errorMsg = err.response?.data?.message || err.message;
      setError(errorMsg);
      throw err;
    } finally {
      setLoading(false);
    }
  }, []);

  const clearResult = useCallback(() => setResult(null), []);

  return { result, loading, error, submit, clearResult, setResult };
};

export default useSubmission;
