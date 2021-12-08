import React from 'react';
import './App.css';
import {BrowserRouter as Router,Routes,Route} from "react-router-dom";

import Login from "./components/Login.js";
import VerifAdresseMail from "./components/VerifAdresseMail.js";
import SignUp from "./components/SignUp.js";
import Password from "./components/Password.js";
import MyMatchs from "./components/MyMatchs.js";
import AvailableMatches from "./components/AvailableMatches.js";
import MyInfos from "./components/MyInfos.js";

class App extends React.Component {
constructor(){
	super()
}

render() {
		return(
			 <Router>
				<Routes>
					<Route path="/login" element={<Login/>}/> 
					<Route path="/verifadressemail" element={<VerifAdresseMail/>}/> 
					<Route path="/signup" element={<SignUp/>}/> 
					<Route path="/password" element={<Password/>}/> 
					<Route path="/mymatchs" element={<MyMatchs/>}/> 
					<Route path="/availablematches" element={<AvailableMatches/>}/> 
					<Route path="/myinfos" element={<MyInfos/>}/> 
				</Routes>
			</Router>
		)
	}
}

export default App;