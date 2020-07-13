import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import * as serviceWorker from './serviceWorker';
import {
  TweetsComponents,
  TweetDetailComponent,
  FeedComponents,
} from './tweets';

const appEL = document.getElementById('root');
if (appEL) {
  ReactDOM.render(
    <React.StrictMode>
      <App />
    </React.StrictMode>,
    appEL
  );
}
const e = React.createElement;
const tweetsEl = document.getElementById('tweetme-2');
if (tweetsEl) {
  // console.log(tweetsEl.dataset);
  const MyComponent = e(TweetsComponents, tweetsEl.dataset);
  ReactDOM.render(MyComponent, tweetsEl);
}

const tweetFeedEl = document.getElementById('tweetme-2-feed');
if (tweetFeedEl) {
  // console.log(tweetsEl.dataset);
  // const MyComponent = e(FeedComponents, tweetFeedEl.dataset);
  ReactDOM.render(e(FeedComponents, tweetFeedEl.dataset), tweetFeedEl);
}

const tweetDetailElements = document.querySelectorAll('.tweetme-2-detail');
tweetDetailElements.forEach((container) => {
  ReactDOM.render(e(TweetDetailComponent, container.dataset), container);
});
// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
