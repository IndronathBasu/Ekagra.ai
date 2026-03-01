import { useEffect, useState } from 'react';

const Timer = ({ initialSeconds = 0, onTimeUp }) => {
  const [seconds, setSeconds] = useState(initialSeconds);

  useEffect(() => {
    if (seconds <= 0) {
      onTimeUp?.();
      return;
    }

    const interval = setInterval(() => {
      setSeconds((prev) => prev - 1);
    }, 1000);

    return () => clearInterval(interval);
  }, [seconds, onTimeUp]);

  const hours = Math.floor(seconds / 3600);
  const minutes = Math.floor((seconds % 3600) / 60);
  const secs = seconds % 60;

  const formatTime = (value) => String(value).padStart(2, '0');

  return (
    <div className="bg-slate-800 px-4 py-2 rounded-lg inline-block">
      <div className="flex items-center gap-2">
        <span className="text-slate-400 text-xs">Time:</span>
        <span
          className={`font-mono font-semibold text-sm ${
            seconds < 60 ? 'text-red-400' : 'text-cyan-400'
          }`}
        >
          {hours > 0 && `${formatTime(hours)}:`}
          {formatTime(minutes)}:{formatTime(secs)}
        </span>
      </div>
    </div>
  );
};

export default Timer;
