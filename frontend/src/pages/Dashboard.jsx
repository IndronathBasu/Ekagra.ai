import { useState } from 'react';
import MasteryChart from '../components/dashboard/MasteryChart';
import TopicBreakdown from '../components/dashboard/TopicBreakdown';
import PerformanceStats from '../components/dashboard/PerformanceStats';
import RecentSubmissions from '../components/dashboard/RecentSubmissions';
import useAuth from '../hooks/useAuth';
import { mockAnalytics } from '../services/mockApi';

const Dashboard = () => {
  const { user } = useAuth();

  // Hardcoded analytics data derived from mockAnalytics
  const [analytics] = useState(() => ({
    stats: {
      total_problems_solved: mockAnalytics.problemsSolved,
      acceptance_rate: (mockAnalytics.accuracy || 0) / 100,
      average_execution_time: (mockAnalytics.avgTime || 0) * 1000, // convert \"minutes\"-style value to ms
      total_submissions: mockAnalytics.problemsSolved * 2,
    },
    masteryData: mockAnalytics.masteryData,
    topicBreakdown: mockAnalytics.topicBreakdown,
    performanceStats: mockAnalytics.performanceStats,
    recentSubmissions: [
      {
        id: 1,
        problemTitle: 'Two Sum',
        difficulty: 'Easy',
        status: 'accepted',
        runtime: '42ms',
        timestamp: new Date(Date.now() - 60 * 60 * 1000),
      },
      {
        id: 2,
        problemTitle: 'Reverse String',
        difficulty: 'Easy',
        status: 'accepted',
        runtime: '58ms',
        timestamp: new Date(Date.now() - 2 * 60 * 60 * 1000),
      },
      {
        id: 3,
        problemTitle: 'Valid Parentheses',
        difficulty: 'Easy',
        status: 'wrong_answer',
        runtime: '65ms',
        timestamp: new Date(Date.now() - 3 * 60 * 60 * 1000),
      },
      {
        id: 4,
        problemTitle: 'Climbing Stairs',
        difficulty: 'Easy',
        status: 'accepted',
        runtime: '37ms',
        timestamp: new Date(Date.now() - 5 * 60 * 60 * 1000),
      },
      {
        id: 5,
        problemTitle: 'Longest Substring Without Repeating Characters',
        difficulty: 'Medium',
        status: 'accepted',
        runtime: '89ms',
        timestamp: new Date(Date.now() - 24 * 60 * 60 * 1000),
      },
    ],
  }));

  const loading = false;
  const error = null;

  return (
    <div className="min-h-screen bg-slate-950">
      <div className="max-w-7xl mx-auto px-4 py-8">
        {/* Header */}
        <div className="mb-8">
          <h1 className="text-4xl font-bold text-slate-100 mb-2">Dashboard</h1>
          <p className="text-slate-400">Track your learning progress</p>
        </div>

        {error && (
          <div className="bg-red-900 bg-opacity-30 border border-red-700 text-red-200 px-6 py-4 rounded-lg mb-8">
            {error}
          </div>
        )}

        {/* Stats Cards */}
        <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
          <div className="bg-slate-900 border border-slate-700 rounded-lg p-6">
            <p className="text-slate-400 text-sm mb-2">Problems Solved</p>
            <p className="text-3xl font-bold text-cyan-400">
              {analytics?.stats?.total_problems_solved || 0}
            </p>
          </div>

          <div className="bg-slate-900 border border-slate-700 rounded-lg p-6">
            <p className="text-slate-400 text-sm mb-2">Success Rate</p>
            <p className="text-3xl font-bold text-green-400">
              {((analytics?.stats?.acceptance_rate || 0) * 100).toFixed(1)}%
            </p>
          </div>

          <div className="bg-slate-900 border border-slate-700 rounded-lg p-6">
            <p className="text-slate-400 text-sm mb-2">Avg. Execution Time</p>
            <p className="text-3xl font-bold text-yellow-400">
              {(analytics?.stats?.average_execution_time || 0).toFixed(0)}
              <span className="text-sm ml-1">ms</span>
            </p>
          </div>

          <div className="bg-slate-900 border border-slate-700 rounded-lg p-6">
            <p className="text-slate-400 text-sm mb-2">Total Submissions</p>
            <p className="text-3xl font-bold text-orange-400">
              {analytics?.stats?.total_submissions || 0}
            </p>
          </div>
        </div>

        {/* Charts and Breakdown */}
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-8">
          <div className="lg:col-span-2">
            <MasteryChart data={analytics?.masteryData} />
          </div>
          <div>
            <TopicBreakdown data={analytics?.topicBreakdown} />
          </div>
        </div>

        {/* Performance Stats */}
        <div className="mb-8">
          <PerformanceStats stats={analytics?.performanceStats} />
        </div>

        {/* Recent Submissions */}
        <div>
          <RecentSubmissions submissions={analytics?.recentSubmissions} />
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
