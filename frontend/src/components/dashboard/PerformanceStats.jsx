const PerformanceStats = ({ stats = {} }) => {
  const defaultStats = {
    successRate: 78,
    avgAttempts: 1.8,
    bestScore: 95,
    averageScore: 72,
  };

  const displayStats = { ...defaultStats, ...stats };

  return (
    <div className="bg-slate-900 border border-slate-700 rounded-lg p-6">
      <h2 className="text-lg font-semibold text-slate-100 mb-6">Performance Metrics</h2>

      <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
        <div className="bg-slate-800 rounded-lg p-4 text-center">
          <p className="text-slate-400 text-xs mb-2">Success Rate</p>
          <p className="text-2xl font-bold text-green-400">{displayStats.successRate}%</p>
        </div>

        <div className="bg-slate-800 rounded-lg p-4 text-center">
          <p className="text-slate-400 text-xs mb-2">Avg Attempts</p>
          <p className="text-2xl font-bold text-blue-400">{displayStats.avgAttempts}</p>
        </div>

        <div className="bg-slate-800 rounded-lg p-4 text-center">
          <p className="text-slate-400 text-xs mb-2">Best Score</p>
          <p className="text-2xl font-bold text-yellow-400">{displayStats.bestScore}</p>
        </div>

        <div className="bg-slate-800 rounded-lg p-4 text-center">
          <p className="text-slate-400 text-xs mb-2">Avg Score</p>
          <p className="text-2xl font-bold text-purple-400">{displayStats.averageScore}</p>
        </div>
      </div>

      {/* Trend Info */}
      <div className="mt-6 p-4 bg-slate-800 rounded border border-slate-700">
        <p className="text-sm text-slate-400 mb-2">This Week</p>
        <p className="text-lg font-semibold text-cyan-400">+12% improvement</p>
        <p className="text-xs text-slate-500 mt-1">5 problems solved, 80% accuracy</p>
      </div>
    </div>
  );
};

export default PerformanceStats;
