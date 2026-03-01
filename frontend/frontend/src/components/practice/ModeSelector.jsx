const ModeSelector = ({ selectedMode, onModeChange, isLoading }) => {
  const modes = [
    { id: 'adaptive', label: 'Adaptive', description: 'Personalized difficulty' },
    { id: 'easy', label: 'Easy', description: 'Build foundations' },
    { id: 'medium', label: 'Medium', description: 'Challenge yourself' },
    { id: 'hard', label: 'Hard', description: 'Master concepts' },
  ];

  return (
    <div className="flex gap-3 mb-6 flex-wrap">
      {modes.map((mode) => (
        <button
          key={mode.id}
          onClick={() => onModeChange(mode.id)}
          disabled={isLoading}
          className={`px-4 py-2 rounded-lg transition-all ${
            selectedMode === mode.id
              ? 'bg-cyan-600 text-white shadow-lg'
              : 'bg-slate-800 text-slate-300 hover:bg-slate-700'
          } ${isLoading ? 'opacity-50 cursor-not-allowed' : ''}`}
          title={mode.description}
        >
          {mode.label}
        </button>
      ))}
    </div>
  );
};

export default ModeSelector;
