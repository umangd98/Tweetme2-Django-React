import React from 'react';

export function UserLink(props) {
  // const username = { props };
  const handleUserLink = (e) => {
    window.location.href = `/profile/${props.username}`;
  };
  return (
    <span className="pointer" onClick={handleUserLink}>
      {props.children}
    </span>
  );
}

export function UserPicture(props) {
  const { user } = props;
  return (
    <UserLink username={user.username}>
      <span className="mx-1 px-3 py-2 text-center rounded-circle bg-dark text-white">
        {user.username[0]}
      </span>
    </UserLink>
  );
}
export function UserDisplay(props) {
  const { user, includeFullName } = props;
  const nameDisplay =
    includeFullName === true ? `${user.first_name} ${user.last_name}` : null;

  return (
    <React.Fragment>
      {nameDisplay}
      <UserLink username={user.username}>@{user.username}</UserLink>
    </React.Fragment>
  );
}
