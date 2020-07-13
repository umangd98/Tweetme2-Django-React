import React, { useState, useEffect } from 'react';
import { TweetList } from './list';
import { TweetCreate } from './create';
import { loadTweetDetail } from './lookup';
import { Tweet } from './detail';
import { FeedList } from './feeds';

export const FeedComponents = (props) => {
  console.log(props);
  const canTweet = props.canTweet === 'false' ? false : true;
  const [newTweets, setNewTweets] = useState([]);
  const handleNewTweet = (newTweet) => {
    let tempNewTweets = [...newTweets];
    tempNewTweets.unshift(newTweet);
    setNewTweets(tempNewTweets);
  };

  return (
    <div className={props.className}>
      {canTweet === true && (
        <TweetCreate didTweet={handleNewTweet} className="col-12 mb-3" />
      )}
      <FeedList newTweets={newTweets} {...props} />
    </div>
  );
};

export const TweetsComponents = (props) => {
  console.log(props);
  const canTweet = props.canTweet === 'false' ? false : true;
  const [newTweets, setNewTweets] = useState([]);
  const handleNewTweet = (newTweet) => {
    let tempNewTweets = [...newTweets];
    tempNewTweets.unshift(newTweet);
    setNewTweets(tempNewTweets);
  };

  return (
    <div className={props.className}>
      {canTweet === true && (
        <TweetCreate didTweet={handleNewTweet} className="col-12 mb-3" />
      )}
      <TweetList newTweets={newTweets} {...props} />
    </div>
  );
};

export function TweetDetailComponent(props) {
  const { tweetId } = props;
  const [didLookup, setdidLookup] = useState(false);
  const [tweet, settweet] = useState(null);
  const handleBackendLookup = (res, status) => {
    if (status === 200) {
      settweet(res);
    } else {
      alert('error finding our tweet');
    }
  };
  useEffect(() => {
    if (didLookup === false) {
      loadTweetDetail(tweetId, handleBackendLookup);
      setdidLookup(true);
    }
  }, [didLookup, setdidLookup, tweetId]);
  return tweet === null ? null : (
    <Tweet tweet={tweet} className={props.className} />
  );
}
