import React from 'react';
import { createTweet } from './lookup';

export function TweetCreate(props) {
  const textAreaRef = React.createRef();
  const { didTweet } = props;
  const handleBackendUpdate = (response, status) => {
    if (status === 201) {
      didTweet(response);
    } else {
      console.log(response);
      alert('an error occured');
    }
  };
  const handleSubmit = (e) => {
    // backend api request
    e.preventDefault();
    const newVal = textAreaRef.current.value;
    createTweet(newVal, handleBackendUpdate);
    textAreaRef.current.value = '';
  };
  return (
    <div className={props.className}>
      <form onSubmit={handleSubmit} name="tweet">
        <textarea
          ref={textAreaRef}
          className="form-control"
          name=""
          id=""
          cols="50"
          rows="5"
          required
        ></textarea>
        <button type="submit" className="btn btn-primary my-3">
          Tweet
        </button>
      </form>
    </div>
  );
}
