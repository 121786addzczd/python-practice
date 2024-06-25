import React, { useState } from 'react';

const Form = () => {
  const [form, setForm] = useState({
    name: "",
    age: "",
    gender: "",
  });
  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setForm({ ...form, [name]: value });
  };


  return (
    <>
      <form>
        <label htmlFor="name">名前
          <input id="name" type="text" name="name" value={form.name} onChange={handleInputChange} />
        </label>
        <br />
        <label htmlFor="age">年齢
          <select id="age" name="age" value={form.age} onChange={handleInputChange} >
            <option value={10}>10代</option>
            <option value={20}>20代</option>
            <option value={30}>30代</option>
            <option value={40}>40代</option>
            <option value={50}>50代</option>
          </select>
        </label>
        <br />
        <label htmlFor="gender">性別
          <input id="male" name="gender" type="radio" value="male" onChange={handleInputChange} />男性
          <input id="female" name="gender" type="radio" value="female" onChange={handleInputChange} />女性
          <input id="other" name="gender" type="radio" value="other" onChange={handleInputChange} />その他
        </label>
      </form>
      <p>確認用</p>
      <p>{form.name}</p>
      <p>{form.age}</p>
      <p>{form.gender}</p>
    </>
  );
};

export default Form;