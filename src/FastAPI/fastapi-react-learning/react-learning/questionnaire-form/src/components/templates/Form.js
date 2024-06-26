import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Container, Box, Typography, TextField, InputLabel, Select, MenuItem, FormLabel, RadioGroup, FormControlLabel, Radio, Button } from '@mui/material';
import SendIcon from '@mui/icons-material/Send';

const Form = () => {
  const [form, setForm] = useState({
    name: "",
    age: "",
    gender: "",
    comment: "",
  });
  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setForm({ ...form, [name]: value });
  };

  const navigate = useNavigate();

  const goToResult = (form) => {
    navigate("/result", { state: form });
  };

  const handleSubmit = (event) => {
    goToResult(form);
  };

  return (
    <Container maxWidth="sm">
      <Box sx={{
        marginTop: 1,
        display: "flex",
        flexDirection: "column",
        alignItems: "center", 
      }}>
        <Typography variant="h5">アンケート提出</Typography>
        <TextField id="name" name="name" label="名前" variant="outlined" value={form.name} onChange={handleInputChange} fullWidth />
        
        <Box sx={{ width: "100%", mt: 2 }}>
          <InputLabel id="demo-simple-select-label">年齢</InputLabel>
          <Select
            labelId="demo-simple-select-label"
            id="demo-simple-select"
            value={form.age}
            name="age"
            onChange={handleInputChange}
            fullWidth
          >
            <MenuItem value={10}>10代</MenuItem>
            <MenuItem value={20}>20代</MenuItem>
            <MenuItem value={30}>30代</MenuItem>
            <MenuItem value={40}>40代</MenuItem>
            <MenuItem value={50}>50代</MenuItem>
          </Select>
        </Box>

        <Box sx={{ width: "100%", mt: 2 }}>
          <FormLabel id="demo-radio-buttons-group-label">性別</FormLabel>
          <Box sx={{ border: 1, borderRadius: 1, borderColor: "grey.500" }}>
          <RadioGroup
            aria-labelledby="demo-radio-buttons-group-label"
            defaultValue="female"
            name="gender"
            onChange={handleInputChange}
          >
            <FormControlLabel value="female" control={<Radio />} label="女性" />
            <FormControlLabel value="male" control={<Radio />} label="男性" />
            <FormControlLabel value="other" control={<Radio />} label="その他" />
          </RadioGroup>
          </Box>
        </Box>

        <TextField id="comment" name="comment" label="コメント" variant="outlined" value={form.comment} onChange={handleInputChange} fullWidth sx={{ mt: 2 }} />

        <Button variant="contained" onClick={handleSubmit} sx={{ mt: 2 }} endIcon={<SendIcon />} fullWidth>送信</Button>
      </Box>
    </Container>
  );
};

export default Form;