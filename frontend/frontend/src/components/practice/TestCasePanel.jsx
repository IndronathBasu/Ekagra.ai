const TestCasePanel = ({ testCases = [] }) => {
  if (!testCases || testCases.length === 0) {
    return (
      <div className="bg-slate-900 border border-slate-700 rounded-lg p-6">
        <p className="text-slate-400 text-sm">No test cases available</p>
      </div>
    );
  }

  return (
    <div className="bg-slate-900 border border-slate-700 rounded-lg overflow-hidden">
      <div className="bg-slate-800 px-6 py-4 border-b border-slate-700">
        <h3 className="text-sm font-semibold text-slate-300">
          Test Cases ({testCases.length})
        </h3>
      </div>

      <div className="divide-y divide-slate-700">
        {testCases.map((testCase, idx) => (
          <div key={idx} className="p-6 hover:bg-slate-800 transition-colors">
            <div className="flex items-start gap-3 mb-3">
              <span className="text-cyan-400 font-semibold text-sm">Case {idx + 1}</span>
              {testCase.status && (
                <span
                  className={`text-xs font-semibold px-2 py-1 rounded ${
                    testCase.status === 'passed'
                      ? 'bg-green-900 text-green-200'
                      : 'bg-red-900 text-red-200'
                  }`}
                >
                  {testCase.status === 'passed' ? '✓ Passed' : '✗ Failed'}
                </span>
              )}
            </div>

            <div className="space-y-2 text-sm">
              <div>
                <p className="text-slate-400 mb-1">Input:</p>
                <pre className="bg-slate-800 p-3 rounded text-slate-300 font-mono text-xs overflow-x-auto">
                  {typeof testCase.input === 'string'
                    ? testCase.input
                    : JSON.stringify(testCase.input, null, 2)}
                </pre>
              </div>

              <div>
                <p className="text-slate-400 mb-1">Expected Output:</p>
                <pre className="bg-slate-800 p-3 rounded text-slate-300 font-mono text-xs overflow-x-auto">
                  {typeof testCase.expectedOutput === 'string'
                    ? testCase.expectedOutput
                    : JSON.stringify(testCase.expectedOutput, null, 2)}
                </pre>
              </div>

              {testCase.actualOutput !== undefined && (
                <div>
                  <p className="text-slate-400 mb-1">Your Output:</p>
                  <pre className="bg-slate-800 p-3 rounded text-slate-300 font-mono text-xs overflow-x-auto">
                    {typeof testCase.actualOutput === 'string'
                      ? testCase.actualOutput
                      : JSON.stringify(testCase.actualOutput, null, 2)}
                  </pre>
                </div>
              )}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default TestCasePanel;
