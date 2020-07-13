import React, { useState, useEffect } from 'react';
import { loadTweets } from './lookup';
import { Tweet } from './detail';
export const TweetList = (props) => {
  const [tweetsInit, setTweetsInit] = useState([]);
  const [nextUrl, setnextUrl] = useState(null);
  const [tweets, setTweets] = useState([]);
  const [tweetsDidSet, setTweetsDidSet] = useState(false);
  useEffect(() => {
    const final = [...props.newTweets].concat(tweetsInit);
    // console.log(props.newTweets);
    if (final.length !== tweets.length) {
      setTweets(final);
    }
    // console.log('in first use effect');

    return () => {};
  }, [tweetsInit, props.newTweets, tweets]);
  useEffect(() => {
    if (tweetsDidSet === false) {
      const myCallback = (response, status) => {
        if (status === 200) {
          setnextUrl(response.next);
          setTweetsDidSet(true);
          setTweetsInit(response.results);
        }
      };
      // console.log('in second use effect');

      loadTweets(props.username, myCallback);
    }
  }, [tweetsInit, tweetsDidSet, props.username]);
  const handleDidRetweet = (newTweet) => {
    const updatedTweetsInit = [...tweetsInit];
    updatedTweetsInit.unshift(newTweet);
    setTweetsInit(updatedTweetsInit);
    const updateFinalTweets = [...tweets];
    updateFinalTweets.unshift(newTweet);
    setTweets(updatedTweetsInit);
  };
  const handleLoadNext = (e) => {
    e.preventDefault();
    if (nextUrl !== null) {
      loadTweets(
        props.username,
        (response, status) => {
          if (status === 200) {
            setnextUrl(response.next);
            const newTweets = [...tweets].concat(response.results);
            setTweetsInit(newTweets);
            setTweets(newTweets);
          }
        },
        nextUrl
      );
    }
  };
  return (
    <React.Fragment>
      {tweets.map((item, index) => {
        return (
          <Tweet
            didRetweet={handleDidRetweet}
            className="my-5 py-5 border bg-white text-dark"
            tweet={item}
            key={index}
          />
        );
      })}
      {nextUrl !== null && (
        <button onClick={handleLoadNext} className="btn btn-secondary">
          Load Next
        </button>
      )}
    </React.Fragment>
  );
};
