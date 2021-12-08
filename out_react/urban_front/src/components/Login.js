import React from 'react';
import axios from 'axios';
import {Routes, Route, Navigate} from 'react-router-dom';
import {Alert, Form, Row, Col, Button} from 'react-bootstrap'

import image1 from './image_user_1.png'


class Login extends React.Component {
	constructor(){
		super()
    	let logged_temp
	    if (localStorage.getItem("logged") === null) {logged_temp = false ; localStorage.setItem("logged",false)}
	    else {logged_temp = localStorage.getItem("logged")}

		this.state = {
			adresse_mail:"",
			mot_de_passe:"",
      		logged: logged_temp
		}

		this.changeHandler = this.changeHandler.bind(this)
		this.seConnecter = this.seConnecter.bind(this)
	}

	changeHandler = (e) => {this.setState({[e.target.name]: e.target.value})}

	seConnecter = (e) => {
		e.preventDefault()
		axios.get('http://127.0.0.1:1241/login',{params:{adresse_mail:this.state.adresse_mail,mdp:this.state.mot_de_passe}})
		 	.then(response => {
            if(response.status === 200){
                if (response.data.retour === "ok"){
                  	localStorage.setItem("token",response.data.token)
                  	localStorage.setItem("logged",true)
                  	this.setState({logged:true})
                                                  }
                                      }
                              }
            ).catch(error => {console.log(error)})

	}

	render() {
	  	const {adresse_mail,mot_de_passe,logged} = this.state
	    if (logged === true) {return <Routes> <Route path="*" element={<Navigate to ="/mymatchs" />}/> </Routes>}

		return(
			<div className="App">

	            <Alert variant={"success"}> <h1> Urban </h1> </Alert>

	            <div class="aaaae"> <img alt="jsp" src={image1} class="image-user-1" /> </div>

	            <div class="aaaaa"> Adresse mail </div>
	            <div class="aaaab"> <Form> <Form.Control type="text" placeholder="Adresse mail" name="adresse_mail" onChange={this.changeHandler} value={adresse_mail} /> </Form> </div>
	            <div class="aaaac"> Mot de passe </div>
	            <div class="aaaad"> <Form> <Form.Control type="password" placeholder="Mot de passe" name="mot_de_passe" onChange={this.changeHandler} value={mot_de_passe} /> </Form> </div>
		        <div class="aaaaf"> <Button variant="success" onClick={this.seConnecter}> Se connecter </Button> </div>

		        <div class="aaaag">
		        	<a href="/signup"> S'inscrire </a> <br/>
		        	<a href="/verifadressemail"> Mail de confirmation </a> <br/>
		        	<a href="/password"> Mot de passe oublié ? </a>
		        </div>

			</div>
		)
	}
}

export default Login;
