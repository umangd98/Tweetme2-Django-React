import React from 'react';
import { tweetAction } from './lookup';

export function ActionBtn(props) {
  const { tweet, action, didPerformAction } = props;
  const likes = tweet.likes ? tweet.likes : 0;

  const actionDisplay = action.display ? action.display : 'Action';
  const handleActionBackendEvent = (response, status) => {
    console.log(status, response);
    if ((status === 200 || status === 201) && didPerformAction) {
      didPerformAction(response, status);
    }
  };
  const handleClick = (e) => {
    e.preventDefault();
    tweetAction(tweet.id, action.type, handleActionBackendEvent);
  };
  const display =
    action.type === 'like' ? `${likes} ${actionDisplay}` : actionDisplay;
  return (
    <button className="btn btn-outline-primary btn-sm" onClick={handleClick}>
      {display}
    </button>
  );
}
