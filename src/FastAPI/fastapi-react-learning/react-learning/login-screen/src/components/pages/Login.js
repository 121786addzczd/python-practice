import React from 'react';
import { Container, Box, Typography, TextField, Button } from '@mui/material';
import { Link } from "react-router-dom"; 

const Login = () => {
  return (
    <>
      <Container maxWidth="xs">
        <Box sx={{
          marginTop: 8,
          display: "flex",
          flexDirection: "column",
          alignItems: "center", 
        }}>
          <Typography variant="h5">ログイン画面</Typography>

          <TextField
            margin="normal"
            required
            fullWidth
            name="username"
            label="名前"
            id="username"
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
          />

          <Button fullWidth variant="contained" sx={{ mt: 3, mb: 2 }} >
            ログイン
          </Button>

          <Link to="/register">新規登録はこちら</Link>
        </Box>
      </Container>
    </>
  );
}

export default Login;