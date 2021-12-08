import React from 'react';

import {Alert, Button, Form, Navbar, Nav} from 'react-bootstrap'

import image1 from './fleche_gauche2.png'

class SignUp extends React.Component {
	constructor(){
		super()
	}

	render() {
		return(
			<div className="App">
				<>
				  <Navbar bg="dark" variant="dark">
				    <Form inline>
				    	<div class="aaaai">
				    		<a href="/login">
				    			<Button variant="outline-info"> <img alt="jsp" src={image1} class="image-log-off" /> </Button>
				    		</a>
				    	</div>
				    </Form>
				  </Navbar>
				</>

	            <Alert variant={"success"}> <h1> S'inscrire </h1> </Alert>

	            <div class="aaaaj"> Adresse mail </div> 
	            <div class="aaaah"> <Form> <Form.Control type="text" placeholder="Adresse mail" /> </Form> </div>
	            <div class="aaaaj"> Mot de passe </div> 
	            <div class="aaaah"> <Form> <Form.Control type="text" placeholder="Mot de passe" /> </Form> </div>
	            <div class="aaaaj"> Nom </div> 
	            <div class="aaaah"> <Form> <Form.Control type="text" placeholder="Nom" /> </Form> </div>
	            <div class="aaaaj"> Prénom </div> 
	            <div class="aaaah"> <Form> <Form.Control type="text" placeholder="Prénom" /> </Form> </div>
	            <div class="aaaaj"> Age </div> 
	            <div class="aaaah"> <Form> <Form.Control type="number" placeholder="Age" /> </Form> </div>
				<div class="aaaak"> <Button variant="success"> S'inscrire </Button> </div>

			</div>
		)
	}
}

export default SignUp;
