import { formatDistanceToNow } from 'date-fns';

const getStatusBadgeColor = (status) => {
  switch (status) {
    case 'accepted':
    case 'passed':
      return 'bg-green-900 text-green-200';
    case 'wrong_answer':
      return 'bg-red-900 text-red-200';
    case 'time_limit_exceeded':
      return 'bg-orange-900 text-orange-200';
    case 'runtime_error':
      return 'bg-red-900 text-red-200';
    default:
      return 'bg-slate-700 text-slate-200';
  }
};

const getDifficultyColor = (difficulty) => {
  switch (difficulty) {
    case 'Easy':
      return 'text-green-400';
    case 'Medium':
      return 'text-yellow-400';
    case 'Hard':
      return 'text-red-400';
    default:
      return 'text-slate-400';
  }
};

const RecentSubmissions = ({ submissions = [] }) => {
  const defaultSubmissions = [
    {
      id: 1,
      problemTitle: 'Two Sum',
      difficulty: 'Easy',
      status: 'accepted',
      runtime: '42ms',
      timestamp: new Date(Date.now() - 3600000),
    },
    {
      id: 2,
      problemTitle: 'Palindrome Number',
      difficulty: 'Easy',
      status: 'accepted',
      runtime: '58ms',
      timestamp: new Date(Date.now() - 7200000),
    },
  ];

  const submissionList = submissions && submissions.length > 0 ? submissions : defaultSubmissions;

  if (submissionList.length === 0) {
    return (
      <div className="bg-slate-900 border border-slate-700 rounded-lg p-6">
        <h2 className="text-lg font-semibold text-slate-100 mb-6">Recent Submissions</h2>
        <p className="text-slate-400 text-center py-8">No submissions yet</p>
      </div>
    );
  }

  return (
    <div className="bg-slate-900 border border-slate-700 rounded-lg overflow-hidden">
      <div className="px-6 py-4 bg-slate-800 border-b border-slate-700">
        <h2 className="text-lg font-semibold text-slate-100">Recent Submissions</h2>
      </div>

      <div className="divide-y divide-slate-700">
        {submissionList.slice(0, 10).map((submission) => (
          <div
            key={submission.id}
            className="px-6 py-4 hover:bg-slate-800 transition-colors"
          >
            <div className="flex items-center justify-between">
              <div>
                <p className="font-semibold text-slate-200">{submission.problemTitle}</p>
                <div className="flex gap-3 mt-1">
                  <span className={`text-sm font-semibold ${getDifficultyColor(submission.difficulty)}`}>
                    {submission.difficulty}
                  </span>
                  <span
                    className={`text-sm px-2 py-0.5 rounded font-semibold ${getStatusBadgeColor(
                      submission.status
                    )}`}
                  >
                    {submission.status}
                  </span>
                </div>
              </div>

              <div className="text-right">
                <p className="text-slate-300 text-sm">{submission.runtime}</p>
                <p className="text-slate-500 text-xs mt-1">
                  {submission.timestamp instanceof Date
                    ? formatDistanceToNow(submission.timestamp, { addSuffix: true })
                    : 'Recently'}
                </p>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default RecentSubmissions;
