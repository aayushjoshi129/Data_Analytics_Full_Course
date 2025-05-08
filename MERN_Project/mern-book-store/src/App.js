// import React from 'react';
// import logo from './logo.svg';
// import './App.css';

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://youtube.com"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React with Aayush Joshi 121
//         </a>
//       </header>
//     </div>
//   );
// }

// export default App;



import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import { useSelector } from 'react-redux';

import LoginPage from '../frontend/src/pages/Login';
import RegisterPage from '../frontend/src/pages/Register';
import UploadPage from '../frontend/src/pages/Upload';
import HomePage from '../frontend/src/pages/Homepage';
import PrivateRoute from '../frontend/src/components/PrivateRoute';

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
