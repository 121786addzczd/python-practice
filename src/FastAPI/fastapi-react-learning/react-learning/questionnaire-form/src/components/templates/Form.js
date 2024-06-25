import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

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

  const goToResult = () => {
    navigate("/result");
  };

  const handleSubmit = (event) => {
    goToResult();
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
        <br />
        <label htmlFor="comment">コメント
          <textarea id="comment" name="comment" placeholder='コメントを入れてください' value={form.comment} onChange={handleInputChange}></textarea>
        </label>
      </form>
      <button onClick={handleSubmit}>送信</button>
    </>
  );
};

export default Form;