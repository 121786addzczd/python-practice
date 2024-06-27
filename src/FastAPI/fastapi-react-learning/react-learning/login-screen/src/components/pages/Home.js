import React, { useContext } from 'react';
import Header from "../templates/Header";
import { Navigate, useLocation } from "react-router-dom";
import { useState } from "react";
import { LoginUserContext } from '../providers/LoginUserProvider';

const Home = () => {
  const location = useLocation();
  const [data, setData] = useState(location.state);
  const { isLogined } = useContext(LoginUserContext);
  if (!isLogined) {
    return <Navigate to="/login" />;
  } else {
    return (
      <>
        <Header name="xyz" />
        ホーム画面
        {data.username}
      </>
    );
  }
}

export default Home;