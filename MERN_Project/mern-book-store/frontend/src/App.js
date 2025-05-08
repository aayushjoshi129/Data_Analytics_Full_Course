import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import { useSelector } from 'react-redux';

import LoginPage from './pages/Login';
import RegisterPage from './pages/Register';
import UploadPage from './pages/Upload';
import HomePage from './pages/Homepage';
import PrivateRoute from './components/PrivateRoute';

function App() {
  const { userInfo } = useSelector((state) => state.auth);

  return (
    <Router>
      <Switch>
        <Route path="/" exact component={HomePage} />
        <Route path="/login" exact component={LoginPage} />
        <Route path="/register" exact component={RegisterPage} />
        
        <PrivateRoute 
          path="/upload" 
          component={UploadPage} 
        />
        
        {/* Add more protected routes as necessary */}
      </Switch>
    </Router>
  );
}

export default App;
