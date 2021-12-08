import React from 'react';
import axios from 'axios';
import {Routes, Route, Navigate} from 'react-router-dom';
import {Alert, Button, Form, Navbar, Nav} from 'react-bootstrap'

import image1 from './image_logoff_1.png'

class MyInfos extends React.Component {
	constructor(){
		super()

    	let logged_temp
	    if (localStorage.getItem("logged") === null) {logged_temp = false ; localStorage.setItem("logged",false)}
	    else {logged_temp = localStorage.getItem("logged")}

		this.state = {
			valeurs:{},
      		logged: logged_temp
		}
		this.deconnexionHandler = this.deconnexionHandler.bind(this)
		this.fonctionReRender = this.fonctionReRender.bind(this)
	}

	componentDidMount(){
		axios.get('http://127.0.0.1:1241/account',{params:{token:localStorage.getItem("token")}})
		 	.then(response => {
            if(response.status === 200){
                if (response.data.retour === "ok"){
                  	this.setState({valeurs:response.data.valeur})
                                                  }
                                      }
                              }
            ).catch(error => {console.log(error)})
	}

	fonctionReRender(){
		axios.get('http://127.0.0.1:1241/account',{params:{token:localStorage.getItem("token")}})
		 	.then(response => {
            if(response.status === 200){
                if (response.data.retour === "ok"){
                  	this.setState({valeurs:response.data.valeur})
                                                  }
                                      }
                              }
            ).catch(error => {console.log(error)})
	}

	deconnexionHandler = (e) => {
		e.preventDefault()
		localStorage.setItem("logged",false)
		this.setState({"logged":false})
		localStorage.removeItem("token")
	}

	render() {
	  	const {logged, valeurs} = this.state
	    if (logged === false) {return <Routes> <Route path="*" element={<Navigate to ="/login" />}/> </Routes>}


	    const contenu = <div>
							Nom : {valeurs.nom} <br/>
							Prénom : {valeurs.prenom} <br />
							Age : {valeurs.age}
						</div>

		return(
			<div className="App">
				<>
				  <Navbar bg="dark" variant="dark">
				  	<div class="aaabh">
					  	<div class="aaabg">
						    <Nav className="mr-auto">
						        <Nav.Link href="/availablematches">Matchs disponibles</Nav.Link>
						        <Nav.Link href="/mymatchs">Mes matchs</Nav.Link>
						        <Nav.Link href="">Mon compte</Nav.Link>
					    	</Nav>
				    	</div>
			    		<div class="aaabf">
						    <Form inline>
					    		<Button variant="outline-info" onClick={this.deconnexionHandler}> <img alt="jsp" src={image1} class="image-log-off" /> </Button>
						    </Form>
					    </div>
				    </div>
				  </Navbar>
				</>

				<div class="aaaea">
					<div class="aaaeb">

						<div class="aaaec">
							{contenu}
						</div>

					<Button variant="success"> Modifier ses informations personnelles </Button>

					</div>
				</div>

			</div>
		)
	}
}

export default MyInfos;
