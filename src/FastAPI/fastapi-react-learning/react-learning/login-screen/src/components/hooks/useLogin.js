
import React, { useContext } from 'react';
import { useNavigate } from "react-router-dom";
import axios from "axios";
import { LoginUserContext } from '../providers/LoginUserProvider';

export const useLogin = () => {
  const { setLoginUser, setIsLogined } = useContext(LoginUserContext);
  const navigate = useNavigate();
  const login = (user) => {
    const endpoint = "https://jsonplaceholder.typicode.com/users";
    const queries = { username: user.username, id: user.password };
    axios.get(endpoint, { params: queries }).then((res) => {
      if (res.data[0] === undefined) {
        navigate("/loginfailed");
      } else {
        setLoginUser(res.data[0].username);
        setIsLogined(true);
        navigate("/", { state: { username: "テストユーザー"} });
      }
    });
  };
  return {login};
};
