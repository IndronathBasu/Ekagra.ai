import Editor from '@monaco-editor/react';

const CodeEditor = ({ value, onChange, isLoading = false }) => {
  const handleEditorChange = (newValue) => {
    onChange?.(newValue);
  };

  return (
    <div className="bg-slate-900 border border-slate-700 rounded-lg overflow-hidden flex flex-col h-full">
      <div className="bg-slate-800 px-4 py-3 border-b border-slate-700">
        <h3 className="text-sm font-semibold text-slate-300 flex items-center gap-2">
          <span className="w-2 h-2 bg-green-500 rounded-full"></span>
          Python Editor
        </h3>
      </div>

      <div className="flex-1 overflow-hidden">
        <Editor
          height="100%"
          defaultLanguage="python"
          defaultValue={value || '# Write your Python code here\n'}
          value={value}
          onChange={handleEditorChange}
          theme="vs-dark"
          options={{
            minimap: { enabled: false },
            fontSize: 14,
            fontFamily: '"Fira Code", "Courier New", monospace',
            wordWrap: 'on',
            automaticLayout: true,
            padding: { top: 16, bottom: 16 },
            scrollBeyondLastLine: false,
          }}
          loading={isLoading && <div className="text-slate-400 p-4">Loading editor...</div>}
        />
      </div>
    </div>
  );
};

export default CodeEditor;
