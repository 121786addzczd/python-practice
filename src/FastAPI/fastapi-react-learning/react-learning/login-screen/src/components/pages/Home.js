import React from 'react';
import Header from "../templates/Header";
import { useLocation } from "react-router-dom";
import { useState } from "react";

const Home = () => {
  const location = useLocation();
  const [data, setData] = useState(location.state);
  return (
    <>
      <Header name="xyz" />
      ホーム画面
      {data.username}
    </>
  )
}

export default Home;