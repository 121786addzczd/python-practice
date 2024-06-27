import React, { useState, useContext } from 'react';
import { Container, Box, Typography, TextField, Button } from '@mui/material';
import { Link, useNavigate } from "react-router-dom";
import axios from "axios";
import { LoginUserContext } from '../providers/LoginUserProvider'; // 修正箇所

const Login = () => {
  const { setLoginUser, setIsLogined } = useContext(LoginUserContext); // 修正箇所
  const navigate = useNavigate();
  const [user, setUser] = useState({
    username: "",
    password: "",
  });

  const handleChange = (event) => {
    const { name, value } = event.target;
    setUser({ ...user, [name]: value });
  };

  const onClickLogin = () => {
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

  return (
    <Container maxWidth="xs">
      <Box sx={{ marginTop: 8, display: "flex", flexDirection: "column", alignItems: "center" }}>
        <Typography variant="h5">ログイン画面</Typography>
        <TextField
          margin="normal"
          required
          fullWidth
          name="username"
          label="名前"
          id="username"
          onChange={handleChange}
        />
        <TextField
          margin="normal"
          required
          fullWidth
          name="password"
          label="パスワード"
          type="password"
          id="password"
          autoComplete="current-password"
          onChange={handleChange}
        />
        <Button fullWidth variant="contained" sx={{ mt: 3, mb: 2 }} onClick={onClickLogin}>
          ログイン
        </Button>
        <Link to="/register">新規登録はこちら</Link>
      </Box>
    </Container>
  );
};

export default Login;
