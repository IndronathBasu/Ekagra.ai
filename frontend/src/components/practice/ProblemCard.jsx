const getDifficultyColor = (difficulty) => {
  switch (difficulty) {
    case 'Easy':
      return 'bg-green-900 text-green-200';
    case 'Medium':
      return 'bg-yellow-900 text-yellow-200';
    case 'Hard':
      return 'bg-red-900 text-red-200';
    default:
      return 'bg-slate-700 text-slate-200';
  }
};

const ProblemCard = ({ problem, isLoading }) => {
  if (isLoading) {
    return (
      <div className="bg-slate-900 border border-slate-700 rounded-lg p-6 h-full animate-pulse">
        <div className="space-y-4">
          <div className="h-6 bg-slate-700 rounded w-3/4"></div>
          <div className="h-4 bg-slate-700 rounded w-1/4"></div>
          <div className="space-y-2">
            <div className="h-3 bg-slate-700 rounded"></div>
            <div className="h-3 bg-slate-700 rounded"></div>
            <div className="h-3 bg-slate-700 rounded w-5/6"></div>
          </div>
        </div>
      </div>
    );
  }

  if (!problem) {
    return (
      <div className="bg-slate-900 border border-slate-700 rounded-lg p-6 h-full flex items-center justify-center">
        <p className="text-slate-400">No problem loaded</p>
      </div>
    );
  }

  // Map backend fields to frontend display
  const getDifficultyLabel = (band) => {
    const b = band ?? 1;
    if (b <= 1) return 'Easy';
    if (b <= 3) return 'Medium';
    return 'Hard';
  };

  return (
    <div className="bg-slate-900 border border-slate-700 rounded-lg overflow-hidden flex flex-col h-full">
      <div className="bg-slate-800 px-6 py-4 border-b border-slate-700">
        <h2 className="text-xl font-bold text-slate-100 mb-2">{problem.cluster || problem.topic || 'Problem'}</h2>
        <div className="flex gap-2 flex-wrap">
          <span className={`px-3 py-1 rounded-full text-xs font-semibold ${getDifficultyColor(getDifficultyLabel(problem.difficulty_band))}`}>
            {getDifficultyLabel(problem.difficulty_band)}
          </span>
          {problem.topic && (
            <span className="px-3 py-1 rounded-full text-xs font-semibold bg-blue-900 text-blue-200">
              {problem.topic}
            </span>
          )}
          {problem.subject && (
            <span className="px-3 py-1 rounded-full text-xs font-semibold bg-purple-900 text-purple-200">
              {problem.subject}
            </span>
          )}
        </div>
      </div>

      <div className="px-6 py-4 overflow-y-auto flex-1">
        <div className="space-y-4">
          <div>
            <h3 className="text-sm font-semibold text-slate-300 mb-2">Problem Statement</h3>
            <div className="text-slate-400 text-sm leading-relaxed whitespace-pre-wrap">
              {problem.problem_statement || 'No problem statement available.'}
            </div>
          </div>

          {(problem.example_input || problem.example_output) && (
            <div>
              <h3 className="text-sm font-semibold text-slate-300 mb-2">Example</h3>
              <div className="bg-slate-800 p-3 rounded text-xs space-y-2">
                {problem.example_input && (
                  <p className="text-slate-400">
                    <span className="text-slate-300 font-semibold">Input:</span>
                    <pre className="mt-1 text-slate-300 font-mono">{problem.example_input}</pre>
                  </p>
                )}
                {problem.example_output && (
                  <p className="text-slate-400">
                    <span className="text-slate-300 font-semibold">Output:</span>
                    <pre className="mt-1 text-slate-300 font-mono">{problem.example_output}</pre>
                  </p>
                )}
              </div>
            </div>
          )}

          {problem.concepts && problem.concepts.length > 0 && (
            <div>
              <h3 className="text-sm font-semibold text-slate-300 mb-2">Concepts</h3>
              <div className="flex flex-wrap gap-2">
                {problem.concepts.map((concept, idx) => (
                  <span key={idx} className="px-2 py-1 rounded text-xs bg-slate-800 text-slate-300">
                    {concept}
                  </span>
                ))}
              </div>
            </div>
          )}

          {problem.skills_tested && problem.skills_tested.length > 0 && (
            <div>
              <h3 className="text-sm font-semibold text-slate-300 mb-2">Skills Tested</h3>
              <div className="flex flex-wrap gap-2">
                {problem.skills_tested.map((skill, idx) => (
                  <span key={idx} className="px-2 py-1 rounded text-xs bg-cyan-900 text-cyan-200">
                    {skill}
                  </span>
                ))}
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default ProblemCard;
