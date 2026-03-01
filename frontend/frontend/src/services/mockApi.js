// Mock API for development - replace with real API calls when backend is ready

export const mockProblems = [
  {
    id: 1,
    title: 'Two Sum',
    difficulty: 'Easy',
    topic: 'Array',
    description:
      'Given an array of integers nums and an integer target, return the indices of the two numbers that add up to target. You may assume that each input has exactly one solution, and you may not use the same element twice.',
    constraints: [
      '2 <= nums.length <= 104',
      '-109 <= nums[i] <= 109',
      '-109 <= target <= 109',
    ],
    examples: [
      {
        input: 'nums = [2,7,11,15], target = 9',
        output: '[0,1]',
      },
    ],
    boilerplate: 'def twoSum(nums, target):\n    pass',
    timeLimit: 1,
    testCases: [
      { input: '[2,7,11,15], 9', expectedOutput: '[0,1]' },
      { input: '[3,2,4], 6', expectedOutput: '[1,2]' },
    ],
  },
  {
    id: 2,
    title: 'Reverse String',
    difficulty: 'Easy',
    topic: 'String',
    description:
      'Write a function that reverses a string. The input string is given as an array of characters s.',
    constraints: ['1 <= s.length <= 105', 's[i] is a printable ascii character.'],
    examples: [{ input: "s = ['h','e','l','l','o']", output: "['o','l','l','e','h']" }],
    boilerplate: 'def reverseString(s):\n    pass',
    timeLimit: 1,
    testCases: [
      { input: "['h','e','l','l','o']", expectedOutput: "['o','l','l','e','h']" },
    ],
  },
  {
    id: 3,
    title: 'Valid Parentheses',
    difficulty: 'Easy',
    topic: 'String',
    description:
      'Given a string s containing just the characters "(", ")", "{", "}", "[", and "]", determine if the input string is valid. An input string is valid if: 1) Open brackets must be closed by the same type of brackets. 2) Open brackets must be closed in the correct order.',
    constraints: ['1 <= s.length <= 104', 's consists of parentheses only "()[]{}".'],
    examples: [
      { input: 's = "()"', output: 'True' },
      { input: 's = "()[]{}"', output: 'True' },
      { input: 's = "(]"', output: 'False' },
    ],
    boilerplate: 'def isValid(s):\n    pass',
    timeLimit: 1,
    testCases: [
      { input: '"()"', expectedOutput: 'True' },
      { input: '"()[]{}"', expectedOutput: 'True' },
      { input: '"(]"', expectedOutput: 'False' },
    ],
  },
  {
    id: 4,
    title: 'Climbing Stairs',
    difficulty: 'Easy',
    topic: 'Dynamic Programming',
    description:
      'You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?',
    constraints: ['1 <= n <= 45'],
    examples: [
      { input: 'n = 2', output: '2' },
      { input: 'n = 3', output: '3' },
    ],
    boilerplate: 'def climbStairs(n):\n    pass',
    timeLimit: 1,
    testCases: [
      { input: '2', expectedOutput: '2' },
      { input: '3', expectedOutput: '3' },
      { input: '4', expectedOutput: '5' },
    ],
  },
  {
    id: 5,
    title: 'Longest Substring Without Repeating Characters',
    difficulty: 'Medium',
    topic: 'String',
    description:
      'Given a string s, find the length of the longest substring without repeating characters.',
    constraints: ['0 <= s.length <= 5 * 104', 's consists of English letters, digits, symbols and spaces.'],
    examples: [
      { input: 's = "abcabcbb"', output: '3' },
      { input: 's = "bbbbb"', output: '1' },
      { input: 's = "pwwkew"', output: '3' },
    ],
    boilerplate: 'def lengthOfLongestSubstring(s):\n    pass',
    timeLimit: 2,
    testCases: [
      { input: '"abcabcbb"', expectedOutput: '3' },
      { input: '"bbbbb"', expectedOutput: '1' },
      { input: '"pwwkew"', expectedOutput: '3' },
    ],
  },
];

export const mockAnalytics = {
  problemsSolved: 42,
  accuracy: 78,
  avgTime: 12.5,
  streak: 7,
  masteryData: [
    { topic: 'Array', score: 85 },
    { topic: 'String', score: 72 },
    { topic: 'Tree', score: 68 },
    { topic: 'Graph', score: 45 },
    { topic: 'DP', score: 92 },
  ],
  topicBreakdown: [
    { topic: 'Array', count: 24, color: 'bg-blue-500' },
    { topic: 'String', count: 18, color: 'bg-green-500' },
    { topic: 'Tree', count: 16, color: 'bg-purple-500' },
    { topic: 'Graph', count: 12, color: 'bg-pink-500' },
    { topic: 'DP', count: 10, color: 'bg-yellow-500' },
  ],
  performanceStats: {
    successRate: 78,
    avgAttempts: 1.8,
    bestScore: 95,
    averageScore: 72,
  },
};

// Mock functions
export const mockFetchData = () => Promise.resolve({});
export const mockLoginUser = (email, password) => {
  return Promise.resolve({
    user: { id: 1, email, name: 'Test User' },
    token: 'mock-jwt-token',
  });
};
export const mockFetchProblem = () => {
  return Promise.resolve(mockProblems[0]);
};
export const mockSubmitCode = (problemId, code) => {
  return Promise.resolve({
    status: 'accepted',
    message: 'All test cases passed!',
    runtime: '42ms',
    memory: '12.2MB',
    passedTests: 3,
    totalTests: 3,
  });
};
