import React, { useState } from 'react';
import { useLocation } from 'react-router-dom';

export const Result = () => {
  const location = useLocation();
  const [result, setResult] = useState(location.state);
  return (
    <>
      <h1>送信結果ページ</h1>
      <p>名前：{result.name}</p>
      <p>年齢：{result.age}</p>
      <p>性別：{result.gender}</p>
      <p>コメント：{result.comment}</p>
    </>
  );
};

export default Result;