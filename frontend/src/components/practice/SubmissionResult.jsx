const SubmissionResult = ({ result, isLoading }) => {
  if (isLoading) {
    return (
      <div className="bg-slate-900 border border-slate-700 rounded-lg p-6 animate-pulse">
        <div className="h-4 bg-slate-700 rounded w-1/3"></div>
      </div>
    );
  }

  if (!result) {
    return (
      <div className="bg-slate-900 border border-slate-700 rounded-lg p-6 text-center">
        <p className="text-slate-400">Submit your code to see results</p>
      </div>
    );
  }

  const isSuccess = result.status === 'accepted' || result.status === 'passed';
  const statusColor = isSuccess ? 'bg-green-900 text-green-200' : 'bg-red-900 text-red-200';
  const statusIcon = isSuccess ? '✓' : '✗';

  return (
    <div className={`bg-slate-900 border rounded-lg p-6 ${isSuccess ? 'border-green-700' : 'border-red-700'}`}>
      <div className="flex items-start gap-4">
        <div className={`px-3 py-1 rounded font-bold text-lg ${statusColor}`}>
          {statusIcon}
        </div>
        <div className="flex-1">
          <h3 className={`text-lg font-semibold ${isSuccess ? 'text-green-300' : 'text-red-300'}`}>
            {isSuccess ? 'Accepted' : 'Not Accepted'}
          </h3>
          {result.message && (
            <p className="text-slate-400 text-sm mt-2">{result.message}</p>
          )}

          {result.stats && (
            <div className="mt-4 grid grid-cols-2 sm:grid-cols-4 gap-4">
              {result.stats.runtime && (
                <div className="bg-slate-800 rounded p-3 text-center">
                  <p className="text-slate-500 text-xs">Runtime</p>
                  <p className="text-slate-200 font-semibold">{result.stats.runtime}</p>
                </div>
              )}
              {result.stats.memory && (
                <div className="bg-slate-800 rounded p-3 text-center">
                  <p className="text-slate-500 text-xs">Memory</p>
                  <p className="text-slate-200 font-semibold">{result.stats.memory}</p>
                </div>
              )}
              {result.stats.passed !== undefined && (
                <div className="bg-slate-800 rounded p-3 text-center">
                  <p className="text-slate-500 text-xs">Test Cases</p>
                  <p className="text-slate-200 font-semibold">{result.stats.passed}/{result.stats.total}</p>
                </div>
              )}
            </div>
          )}

          {result.error && (
            <div className="mt-4 bg-red-900 bg-opacity-30 border border-red-700 rounded p-3">
              <p className="text-red-200 text-sm font-mono">{result.error}</p>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default SubmissionResult;
