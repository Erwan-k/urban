import React from 'react';

import {Alert, Button, Form, Navbar, Nav} from 'react-bootstrap'

import image1 from './fleche_gauche2.png'

class VerifAdresseMail extends React.Component {
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

	            <Alert variant={"success"}> <h1> Vérifier son adresse mail </h1> </Alert>

	            <Alert variant={"success"}> <h2> Vérifier son adresse mail </h2> </Alert>

	            <div class="aaaaj"> Code de vérification </div> 
	            <div class="aaaah"> <Form> <Form.Control type="text" placeholder="Code de vérification" /> </Form> </div>
				<div class="aaaak"> <Button variant="success"> Vérifier </Button> </div>

	            <Alert variant={"success"}> <h2> Demander un nouvel email de confirmation </h2> </Alert>

	            <div class="aaaal"> Adresse mail </div>
				<div class="aaaam"> <Form> <Form.Control type="text" placeholder="Adresse mail" /> </Form> </div>
				<div class="aaaan"> <Button variant="success"> Envoyer </Button> </div>

			</div>
		)
	}
}

export default VerifAdresseMail;
