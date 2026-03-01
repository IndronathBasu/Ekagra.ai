import { useState, useEffect, useCallback } from 'react';
import ProblemCard from '../components/practice/ProblemCard';
import CodeEditor from '../components/practice/CodeEditor';
import SubmissionResult from '../components/practice/SubmissionResult';
import TestCasePanel from '../components/practice/TestCasePanel';
import ModeSelector from '../components/practice/ModeSelector';
import Timer from '../components/practice/Timer';
import { problemsAPI, submissionAPI } from '../services/api';
import { mockProblems, mockSubmitCode } from '../services/mockApi';
import useAuth from '../hooks/useAuth';

const Practice = () => {
  const [mode, setMode] = useState('adaptive');
  const [problem, setProblem] = useState(null);
  const [problems, setProblems] = useState([]);
  const [code, setCode] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [submitting, setSubmitting] = useState(false);
  const [testCases, setTestCases] = useState([]);
  const [useMockData, setUseMockData] = useState(false);

  const { user } = useAuth();

  const loadProblems = useCallback(async () => {
    setLoading(true);
    setResult(null); // Clear previous errors
    try {
      setUseMockData(false);
      const response = await problemsAPI.getAllProblems(0, 20);
      const data = Array.isArray(response?.data) ? response.data : [];
      setProblems(data);
      if (data.length > 0) {
        selectProblem(data[0]);
      } else {
        setResult({
          status: 'error',
          message: 'No problems available. Run: cd backend && python seed_problems.py',
        });
      }
    } catch (error) {
      // Fallback to hardcoded mock problems when backend is unavailable
      setUseMockData(true);
      const mockData = mockProblems.map((p) => ({
        ...p,
        cluster: p.title || p.topic,
        difficulty_band: p.difficulty === 'Easy' ? 1 : p.difficulty === 'Medium' ? 2 : 3,
        problem_statement: p.description,
        example_input: p.examples?.[0]?.input,
        example_output: p.examples?.[0]?.output,
        subject: p.topic,
      }));
      setProblems(mockData);
      if (mockData.length > 0) {
        selectProblem(mockData[0]);
      }
    } finally {
      setLoading(false);
    }
  }, []);

  // Load problems on mount
  useEffect(() => {
    loadProblems();
  }, [loadProblems]);

  const selectProblem = (selectedProblem) => {
    setProblem(selectedProblem);
    setCode(selectedProblem?.boilerplate || '# Write your solution here\n');
    setResult(null);
    setTestCases(selectedProblem?.testCases || []);
  };

  const handleSubmit = async () => {
    if (!problem || !code.trim()) {
      setResult({
        status: 'error',
        message: 'Please write some code before submitting.',
      });
      return;
    }

    if (!user || !user.id) {
      setResult({
        status: 'error',
        message: 'User not found. Please log in again.',
      });
      return;
    }

    setSubmitting(true);

    try {
      if (useMockData) {
        // Use mock submission when backend is unavailable
        const mockResponse = await mockSubmitCode(problem.id, code);
        const { status, message, runtime, memory, passedTests, totalTests } = mockResponse;
        const isAccepted = status === 'accepted';
        setResult({
          status: isAccepted ? 'accepted' : 'wrong_answer',
          message: message || (isAccepted ? 'All test cases passed!' : 'Some test cases failed.'),
          stats: {
            runtime: runtime || '42ms',
            memory: memory || '12.2MB',
            passed: passedTests,
            total: totalTests,
          },
        });
      } else {
        const response = await submissionAPI.submitCode(
          problem.id,
          user.id,
          code,
          'python'
        );

        const { status, score, execution_time_ms, mastery_delta, updated_super_band } = response.data;

        const isAccepted = status === 'passed';

        if (isAccepted) {
          setResult({
            status: 'accepted',
            message: 'All test cases passed!',
            stats: {
              runtime: execution_time_ms + 'ms',
              score: (score * 100).toFixed(1) + '%',
              masteryDelta: mastery_delta?.toFixed(2) || 0,
              superBand: updated_super_band || 0,
            },
          });
        } else if (status === 'runtime_error') {
          setResult({
            status: 'runtime_error',
            message: 'Runtime Error - Check your code for errors.',
            stats: {
              runtime: execution_time_ms + 'ms',
            },
          });
        } else {
          setResult({
            status: 'wrong_answer',
            message: `Wrong Answer - Score: ${(score * 100).toFixed(1)}%`,
            stats: {
              runtime: execution_time_ms + 'ms',
              score: (score * 100).toFixed(1) + '%',
            },
          });
        }
      }
    } catch (error) {
      console.error('Submission failed:', error);
      const errorMsg = error.response?.data?.detail || error.message || 'Submission failed. Please try again.';
      setResult({
        status: 'error',
        message: errorMsg,
      });
    } finally {
      setSubmitting(false);
    }
  };

  const handleLoadNextProblem = () => {
    if (problems.length > 0) {
      const nextIdx = Math.floor(Math.random() * problems.length);
      selectProblem(problems[nextIdx]);
    }
  };

  return (
    <div className="min-h-screen bg-slate-950">
      <div className="max-w-7xl mx-auto px-4 py-8">
        {/* Mode Selector */}
        <ModeSelector
          selectedMode={mode}
          onModeChange={setMode}
          isLoading={loading}
        />

        {/* Main Layout */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-8">
          {/* Problem Panel */}
          <div className="min-h-96">
            <ProblemCard problem={problem} isLoading={loading} />
          </div>

          {/* Code Editor Panel */}
          <div className="min-h-96 flex flex-col">
            <CodeEditor
              value={code}
              onChange={setCode}
              isLoading={loading}
            />

            {/* Submit Button & Timer */}
            <div className="mt-4 flex items-center justify-between gap-4">
              <button
                onClick={handleSubmit}
                disabled={submitting || loading}
                className="flex-1 bg-green-600 hover:bg-green-700 disabled:bg-slate-700 disabled:opacity-50 text-white font-semibold py-3 rounded transition-colors"
              >
                {submitting ? 'Submitting...' : 'Submit'}
              </button>

              <button
                onClick={handleLoadNextProblem}
                disabled={loading}
                className="px-6 py-3 bg-slate-800 hover:bg-slate-700 disabled:opacity-50 text-slate-300 font-semibold rounded transition-colors"
              >
                Next Problem
              </button>

              {/* Timer */}
              {problem?.timeLimit && (
                <Timer initialSeconds={problem.timeLimit * 60} />
              )}
            </div>
          </div>
        </div>

        {/* Retry button when problems fail to load */}
        {result?.status === 'error' && problems.length === 0 && (
          <div className="mb-4 flex justify-center">
            <button
              onClick={loadProblems}
              className="px-6 py-2 bg-cyan-600 hover:bg-cyan-700 text-white font-semibold rounded"
            >
              Retry Load Problems
            </button>
          </div>
        )}

        {/* Submission Result */}
        {result && (
          <div className="mb-8">
            <SubmissionResult result={result} isLoading={submitting} />
          </div>
        )}

        {/* Test Cases */}
        {testCases.length > 0 && (
          <div>
            <TestCasePanel testCases={testCases} />
          </div>
        )}
      </div>
    </div>
  );
};

export default Practice;
