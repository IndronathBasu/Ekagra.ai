const TopicBreakdown = ({ data = [] }) => {
  const defaultData = [
    { topic: 'Array', count: 24, color: 'bg-blue-500' },
    { topic: 'String', count: 18, color: 'bg-green-500' },
    { topic: 'Tree', count: 16, color: 'bg-purple-500' },
    { topic: 'Graph', count: 12, color: 'bg-pink-500' },
    { topic: 'DP', count: 10, color: 'bg-yellow-500' },
  ];

  const breakdownData = data && data.length > 0 ? data : defaultData;
  const total = breakdownData.reduce((sum, item) => sum + item.count, 0);

  return (
    <div className="bg-slate-900 border border-slate-700 rounded-lg p-6">
      <h2 className="text-lg font-semibold text-slate-100 mb-6">Problems by Topic</h2>

      <div className="space-y-3">
        {breakdownData.map((item, idx) => (
          <div key={idx}>
            <div className="flex items-center justify-between mb-1">
              <div className="flex items-center gap-2">
                <div className={`w-3 h-3 rounded-full ${item.color}`}></div>
                <span className="text-sm text-slate-300">{item.topic}</span>
              </div>
              <span className="text-xs font-semibold text-slate-400">
                {item.count}
              </span>
            </div>
            <div className="w-full bg-slate-800 rounded-full h-1.5 overflow-hidden">
              <div
                className={`h-full ${item.color}`}
                style={{ width: `${(item.count / total) * 100}%` }}
              ></div>
            </div>
          </div>
        ))}
      </div>

      <div className="mt-4 pt-4 border-t border-slate-700">
        <p className="text-sm text-slate-400">
          Total: <span className="font-semibold text-slate-300">{total}</span>
        </p>
      </div>
    </div>
  );
};

export default TopicBreakdown;
