import React from 'react';
import axios from 'axios';
import {Button, Col, Form, Modal, Row} from 'react-bootstrap'

function Ajouter_eleve(argument,fonctionReRender){
  axios.post('http://127.0.0.1:8791/eleve2', {} )
      .then(response => {
        console.log(response)
          if(response.status === 200){
              if (response.data.retour === "ok"){
                  fonctionReRender()
                                                }
                                     }
                        }
            ).catch(error => {console.log(error)})

}

class MyVerticallyCenteredModal extends React.Component{
  constructor(){
    super()
    this.state = {
      date:1,
      heure:"",
      adresse:""
    }
    this.submitHandler = this.submitHandler.bind(this)
    this.changeHandler = this.changeHandler.bind(this)
  }

  submitHandler = (e) => {
    e.preventDefault()
    Ajouter_eleve(this.state,this.props.fonctionReRender)
    this.props.onHide()
  }

  changeHandler = (e) => {this.setState({[e.target.name]: e.target.value})}

  render(){

  	const {nom,niveau} = this.state
  	console.log("hey there")
  	console.log(this.props.infos)

    return(

        <Modal
          {...this.props}
          size="lg"
          aria-labelledby="contained-modal-title-vcenter"
          centered
        >
          <Modal.Header>
            <Modal.Title id="contained-modal-title-vcenter">
                Rejoindre le match du {this.props.infos.day} à {this.props.infos.hour}
            </Modal.Title>
          </Modal.Header> <br />


          <Modal.Body>

            <h4>Information match</h4> <br />
            
            Le match aura lieu le {this.props.infos.day} à {this.props.infos.hour}. <br /> <br />

            <h4> Participants </h4> <br />

            L'équipe rouge se composera des joueurs suivants : <br />

            L'équipe bleu se composera des joueurs suivants : <br />

            Voici la liste supplémentaire pour ce match : <br /> <br />

            <h4> Inscription </h4> <br />

            

          </Modal.Body>
          <Modal.Footer>
            <Button variant="danger"> S'inscrire dans l'équipe rouge </Button> <Button> S'inscrire dans l'équipe bleue </Button> <Button variant="dark"> S'inscrire sur la liste supplémentaire </Button>
		</Modal.Footer>
        </Modal>

      )
  }

}





function ElementMatch(props){
	const [modalShow, setModalShow] = React.useState(false);

	let couleur
	if (props.infos.am_i_origin === 1) {couleur = "success"}
	else {couleur = "primary"}

  return(
      <div class="aaafg">
          <>
			<div class="aaadd">
				<Button variant={couleur} onClick={() => setModalShow(true)}>
					<div> {props.infos.day} </div>
					<div> {props.infos.hour} </div>
					<div> {props.infos.nbr_rouge}/5 </div>
					<div> {props.infos.nbr_bleu}/5 </div>
				</Button>
				<MyVerticallyCenteredModal
	              show={modalShow}
	              infos = {props.infos}
	              fonctionReRender = {props.fonctionReRender}
	              onHide={() => setModalShow(false)}
	            />
			</div>
          </>
      </div>
      )
}

export default ElementMatch;


