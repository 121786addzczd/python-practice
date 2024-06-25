import React, { useState } from 'react';

const Form = () => {
  const [form, setForm] = useState({
    name: "",
    age: "",
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
      </form>
      <p>確認用</p>
      <p>{form.name}</p>
      <p>{form.age}</p>
    </>
  );
};

export default Form;