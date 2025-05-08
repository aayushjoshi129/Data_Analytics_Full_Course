import React, { useState } from 'react';
import axios from 'axios';
import { useHistory } from 'react-router-dom';  // Use useHistory instead of useNavigate

const Register = () => {
  const [formData, setFormData] = useState({ name: '', email: '', password: '' });
  const history = useHistory();  // Initialize useHistory hook

  const handleSubmit = async (e) => {
    e.preventDefault();
    await axios.post('/api/users/register', formData);
    history.push('/login');  // Use history.push() to navigate to the login page
  };

  return (
    <form onSubmit={handleSubmit} className='p-4 max-w-md mx-auto'>
      <h2 className='text-lg font-bold mb-4'>Register</h2>
      <input 
        type='text' 
        placeholder='Name' 
        className='input' 
        value={formData.name} 
        onChange={(e) => setFormData({...formData, name: e.target.value})} 
        required 
      />
      <input 
        type='email' 
        placeholder='Email' 
        className='input mt-2' 
        value={formData.email} 
        onChange={(e) => setFormData({...formData, email: e.target.value})} 
        required 
      />
      <input 
        type='password' 
        placeholder='Password' 
        className='input mt-2' 
        value={formData.password} 
        onChange={(e) => setFormData({...formData, password: e.target.value})} 
        required 
      />
      <button type='submit' className='btn mt-4'>Register</button>
    </form>
  );
};

export default Register;
