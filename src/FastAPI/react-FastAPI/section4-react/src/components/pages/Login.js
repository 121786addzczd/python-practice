import React, { useState } from 'react'
import { Container, Box, Typography, TextField, Button } from "@mui/material";
import { Link } from "react-router-dom";

const Login = () => {
  const [user, setUser] = useState({
    username:"",
    password:"",
  });

  const handleChange = (e) => {
    const {name, value} = e.target;
    console.log(`name:${name}`)
    console.log(`value:${value}`)
    setUser({...user, [name]:value});
  };

  return (
    <>
      <Container maxWidth="xs">
      <Box
          sx={{
            marginTop: 8,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
          }}
      >
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
          label="Password"
          type="password"
          id="password"
          autoComplete="current-password"
          onChange={handleChange}
        />

        <Button fullWidth variant="contained" sx={{ mt: 3, mb: 2 }}>
          ログイン
        </Button>
        <Link to="/register">新規登録はこちら</Link>
      </Box>
      </Container>
    </>
  );
};

export default Login;