import { Route, Redirect } from 'react-router-dom';
import { useSelector } from 'react-redux';

const PrivateRoute = ({ component: Component, ...rest }) => {
  const { userInfo } = useSelector((state) => state.auth);  // Getting user info from Redux state
  
  return (
    <Route
      {...rest}
      render={(props) => 
        userInfo ? (  // If the user is authenticated, allow access to the route
          <Component {...props} />
        ) : (
          <Redirect to="/login" />  // Otherwise, redirect to login page
        )
      }
    />
  );
};

export default PrivateRoute;
