import React, { useState } from 'react';

const Form = () => {
  const [name, setName] = useState("");
  const [age, setAge] = useState("");
  const handleInputChange = (event) => {
    setName(event.target.value);
  };
  const handleAgeChange = (event) => {
    setAge(event.target.value);
  };

  return (
    <>
      <form>
        <label htmlFor="name">名前
          <input id="name" type="text" name="name" value={name} onChange={handleInputChange} />
        </label>
        <br />
        <label htmlFor="age">年齢
          <select id="age" onChange={handleAgeChange}>
            <option value={10}>10代</option>
            <option value={20}>20代</option>
            <option value={30}>30代</option>
            <option value={40}>40代</option>
            <option value={50}>50代</option>
          </select>
        </label>
      </form>
      <p>確認用</p>
      <p>{name}</p>
      <p>{age}</p>
    </>
  );
};

export default Form;