import { createSlice } from '@reduxjs/toolkit';

const authSlice = createSlice({
  name: 'auth',
  initialState: {
    userInfo: null,
  },
  reducers: {
    loginSuccess(state, action) {
      state.userInfo = action.payload;
    },
    logout(state) {
      state.userInfo = null;
    },
    // Ensure this action is defined and exported
    loginUser(state, action) {
      state.userInfo = action.payload;
    },
  },
});

export const { loginSuccess, logout, loginUser } = authSlice.actions;
export default authSlice.reducer;
