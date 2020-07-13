import React, { useState } from 'react';
import {} from './lookup';
import { ActionBtn } from './buttons';
import { UserPicture, UserDisplay } from '../profiles';

export function ParentTweet(props) {
  const { tweet } = props;
  return tweet.parent ? (
    <Tweet isRetweet hideActions className={'mx-auto'} tweet={tweet.parent} />
  ) : null;
}
export const Tweet = (props) => {
  const { tweet, didRetweet, hideActions, isRetweet } = props;
  const [actionTweet, setActionTweet] = useState(
    props.tweet ? props.tweet : null
  );
  let className = props.className ? props.className : 'col-10 mx-auto col-md-6';
  className =
    isRetweet === true ? `${className} p-2 border rounded` : className;
  const handlePerformAction = (newActionTweet, status) => {
    if (status === 200) {
      setActionTweet(newActionTweet);
    } else if (status === 201) {
      // let the tweet list know
      if (didRetweet) {
        didRetweet(newActionTweet);
      }
    }
  };
  const path = window.location.pathname;
  const idRegex = /(?<tweetid>\d+)/;
  const match = path.match(idRegex);
  const urlTweetId = match ? match.groups.tweetid : -1;
  const isDetail = `${tweet.id}` === `${urlTweetId}`;

  const handleLink = (e) => {
    e.preventDefault();
    window.location.href = `/${tweet.id}`;
  };
  return (
    <div className={className}>
      {isRetweet === true && (
        <div className="mb-2">
          <span className="small text-muted">
            Retweet via <UserDisplay user={tweet.user} />
          </span>
        </div>
      )}
      <div className="d-flex">
        <div className="col-1">
          <UserPicture user={tweet.user} />
        </div>
        <div className="col-11">
          <div className="">
            <p>
              <UserDisplay includeFullName user={tweet.user} />
            </p>
            <p>{tweet.content}</p>
            <ParentTweet tweet={tweet} />
          </div>

          <div className="btn btn-group px-0">
            {hideActions !== true && actionTweet && (
              <React.Fragment>
                <ActionBtn
                  tweet={actionTweet}
                  didPerformAction={handlePerformAction}
                  action={{ type: 'like', display: 'Likes' }}
                />
                <ActionBtn
                  tweet={actionTweet}
                  didPerformAction={handlePerformAction}
                  action={{ type: 'unlike', display: 'Unlike' }}
                />
                <ActionBtn
                  tweet={actionTweet}
                  didPerformAction={handlePerformAction}
                  action={{ type: 'retweet', display: 'Retweet' }}
                />
              </React.Fragment>
            )}
            {isDetail === true ? null : (
              <button className="btn btn-primary" onClick={handleLink}>
                View
              </button>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};
