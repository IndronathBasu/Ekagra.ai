const AuthForm = ({ 
  title, 
  fields = [], 
  onSubmit, 
  submitButtonText = 'Submit',
  isLoading = false,
  error = null 
}) => {
  const handleSubmit = (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);
    const data = Object.fromEntries(formData);
    onSubmit(data);
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      {error && (
        <div className="bg-red-900 bg-opacity-30 border border-red-700 text-red-200 px-4 py-3 rounded text-sm">
          {error}
        </div>
      )}

      {fields.map((field) => (
        <div key={field.name}>
          <label htmlFor={field.name} className="block text-sm font-medium text-slate-300 mb-2">
            {field.label}
          </label>
          {field.type === 'textarea' ? (
            <textarea
              id={field.name}
              name={field.name}
              required={field.required}
              placeholder={field.placeholder}
              rows={field.rows || 4}
              className="w-full bg-slate-800 border border-slate-700 rounded px-4 py-2 text-slate-200 placeholder-slate-500 focus:outline-none focus:border-cyan-500 focus:ring-1 focus:ring-cyan-500 transition-colors"
            />
          ) : (
            <input
              id={field.name}
              type={field.type || 'text'}
              name={field.name}
              required={field.required}
              placeholder={field.placeholder}
              className="w-full bg-slate-800 border border-slate-700 rounded px-4 py-2 text-slate-200 placeholder-slate-500 focus:outline-none focus:border-cyan-500 focus:ring-1 focus:ring-cyan-500 transition-colors"
            />
          )}
        </div>
      ))}

      <button
        type="submit"
        disabled={isLoading}
        className="w-full bg-cyan-600 hover:bg-cyan-700 disabled:bg-slate-700 disabled:opacity-50 text-white font-semibold py-2 rounded transition-colors mt-6"
      >
        {isLoading ? 'Processing...' : submitButtonText}
      </button>
    </form>
  );
};

export default AuthForm;
