import React from 'react';
import axios from 'axios';
import {Routes, Route, Navigate} from 'react-router-dom';
import {Alert, Button, Form, Navbar, Nav} from 'react-bootstrap'

import ElementMatch from "./ElementMatch.js";
import AddMatchModal from "./AddMatchModal.js";

import image1 from './image_logoff_1.png'

class AvailableMatches extends React.Component {
	constructor(){
		super()

    	let logged_temp
	    if (localStorage.getItem("logged") === null) {logged_temp = false ; localStorage.setItem("logged",false)}
	    else {logged_temp = localStorage.getItem("logged")}

		this.state = {
			liste_matchs:[],
      		logged: logged_temp
		}
		this.deconnexionHandler = this.deconnexionHandler.bind(this)
		this.fonctionReRender = this.fonctionReRender.bind(this)
	}

	componentDidMount(){
		axios.get('http://127.0.0.1:1241/match',{params:{token:localStorage.getItem("token")}})
		 	.then(response => {
            if(response.status === 200){
                if (response.data.retour === "ok"){
                  	this.setState({liste_matchs:response.data.valeur})
                                                  }
                                      }
                              }
            ).catch(error => {console.log(error)})
	}

	fonctionReRender(){
		axios.get('http://127.0.0.1:1241/match',{params:{token:localStorage.getItem("token")}})
		 	.then(response => {
            if(response.status === 200){
                if (response.data.retour === "ok"){
                  	this.setState({liste_matchs:response.data.valeur})
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
	  	const {logged} = this.state
	    if (logged === false) {return <Routes> <Route path="*" element={<Navigate to ="/login" />}/> </Routes>}

	    const liste = [].concat(this.state.liste_matchs)
	           .map((elem, i) =>  <ElementMatch infos={elem} fonctionReRender={this.props.fonctionReRender} />);

		return(
			<div className="App">
				<>
				  <Navbar bg="dark" variant="dark">
				  	<div class="aaabh">
					  	<div class="aaabg">
						    <Nav className="mr-auto">
						        <Nav.Link href="">Matchs disponibles</Nav.Link>
						        <Nav.Link href="/mymatchs">Mes matchs</Nav.Link>
						        <Nav.Link href="/myinfos">Mon compte</Nav.Link>
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

				<div class="aaada">
					<div class="aaadb">

						<div class="aaadc"> {liste} </div>

						<AddMatchModal />

					</div>
				</div>

			</div>
		)
	}
}

export default AvailableMatches;
