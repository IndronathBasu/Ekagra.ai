const MasteryChart = ({ data = [] }) => {
  const defaultData = [
    { topic: 'Array', score: 85 },
    { topic: 'String', score: 72 },
    { topic: 'Tree', score: 68 },
    { topic: 'Graph', score: 45 },
    { topic: 'DP', score: 92 },
  ];

  const chartData = data && data.length > 0 ? data : defaultData;

  return (
    <div className="bg-slate-900 border border-slate-700 rounded-lg p-6">
      <h2 className="text-lg font-semibold text-slate-100 mb-6">Topic Mastery</h2>

      <div className="space-y-4">
        {chartData.map((item, idx) => (
          <div key={idx}>
            <div className="flex items-center justify-between mb-1">
              <span className="text-sm font-medium text-slate-300">{item.topic}</span>
              <span className="text-xs text-slate-400">{item.score}%</span>
            </div>
            <div className="w-full bg-slate-800 rounded-full h-2 overflow-hidden">
              <div
                className={`h-full rounded-full transition-all ${
                  item.score >= 80
                    ? 'bg-green-500'
                    : item.score >= 60
                    ? 'bg-yellow-500'
                    : 'bg-red-500'
                }`}
                style={{ width: `${item.score}%` }}
              ></div>
            </div>
          </div>
        ))}
      </div>

      <div className="mt-6 p-4 bg-slate-800 rounded border border-slate-700">
        <div className="flex items-center justify-between">
          <span className="text-sm text-slate-400">Overall Mastery</span>
          <span className="text-xl font-bold text-cyan-400">
            {Math.round(chartData.reduce((sum, item) => sum + item.score, 0) / chartData.length)}%
          </span>
        </div>
      </div>
    </div>
  );
};

export default MasteryChart;
