import { backendLookup } from '../lookup';

export function loadFeed(callback, nextUrl) {
  let endpoint = '/tweets/feed';
  if (nextUrl !== null && nextUrl !== undefined) {
    endpoint = nextUrl.replace('http://localhost:8000/api', '');
  }
  backendLookup('GET', endpoint, callback);
}

export function loadTweets(username, callback, nextUrl) {
  let endpoint = '/tweets/';
  if (username) {
    endpoint = `/tweets/?username=${username}`;
  }
  if (nextUrl !== null && nextUrl !== undefined) {
    endpoint = nextUrl.replace('http://localhost:8000/api', '');
  }
  backendLookup('GET', endpoint, callback);
}

export function loadTweetDetail(tweetId, callback) {
  let endpoint = '/tweets/';
  if (tweetId) {
    endpoint = `/tweets/${tweetId}`;
  }
  backendLookup('GET', endpoint, callback);
}

export const createTweet = (newTweet, callback) => {
  backendLookup('POST', '/tweets/create', callback, { content: newTweet });
};

export const tweetAction = (tweetId, action, callback) => {
  backendLookup('POST', '/tweets/action', callback, {
    id: tweetId,
    action: action,
  });
};
