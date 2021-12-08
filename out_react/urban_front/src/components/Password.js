import React from 'react';

import {Alert, Button, Form, Navbar, Nav} from 'react-bootstrap'

import image1 from './fleche_gauche2.png'

class Password extends React.Component {
	constructor(){
		super()
	}

	render() {
		return(
			<div className="App">
				<>
				  <Navbar bg="dark" variant="dark">
				    <Form inline>
			    		<a href="/login">
			    			<Button variant="outline-info"> <img alt="jsp" src={image1} class="image-log-off" /> </Button>
			    		</a>
				    </Form>
				  </Navbar>
				</>

	            <Alert variant={"success"}> <h1> Récupérer son mot de passe </h1> </Alert>

	            <Alert variant={"success"}> <h2> Demander un code par mail </h2> </Alert>

	            <div class="aaaao"> Adresse mail </div>
				<div class="aaaap"> <Form> <Form.Control type="text" placeholder="Adresse mail" /> </Form> </div>
				<div class="aaaaq"> <Button variant="success"> Envoyer </Button> </div>

	            <Alert variant={"success"}> <h2> Changer son mot de passe à l'aide d'un code </h2> </Alert>

	            <div class="aaaar"> Adresse mail </div>
				<div class="aaaas"> <Form> <Form.Control type="text" placeholder="Adresse mail" /> </Form> </div>
	            <div class="aaaat"> Code </div>
				<div class="aaaau"> <Form> <Form.Control type="text" placeholder="Code" /> </Form> </div>
	            <div class="aaaav"> Nouveau mot de passe </div>
				<div class="aaaaw"> <Form> <Form.Control type="text" placeholder="Nouveau mot de passe" /> </Form> </div>
				<div class="aaaax"> <Button variant="success"> Envoyer </Button> </div>

	            <Alert variant={"success"}> <h2> Changer son mot de passe à l'aide de celui en cours </h2> </Alert>

	            <div class="aaaay"> Adresse mail </div>
				<div class="aaaaz"> <Form> <Form.Control type="text" placeholder="Adresse mail" /> </Form> </div>
	            <div class="aaaba"> Code </div>
				<div class="aaabb"> <Form> <Form.Control type="text" placeholder="Code" /> </Form> </div>
	            <div class="aaabc"> Nouveau mot de passe </div>
				<div class="aaabd"> <Form> <Form.Control type="text" placeholder="Nouveau mot de passe" /> </Form> </div>
				<div class="aaabe"> <Button variant="success"> Envoyer </Button> </div>

			</div>
		)
	}
}

export default Password;
