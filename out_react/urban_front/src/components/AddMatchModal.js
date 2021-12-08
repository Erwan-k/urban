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

    return(

        <Modal
          {...this.props}
          size="lg"
          aria-labelledby="contained-modal-title-vcenter"
          centered
        >
          <Modal.Header>
            <Modal.Title id="contained-modal-title-vcenter">
                Proposer un match
            </Modal.Title>
          </Modal.Header> <br />


          <Modal.Body>

            <h4>Informations match</h4> <br />
            
            <div class="aaafa"> Date </div>
            <div class="aaafb"> <Form> <Form.Control type="text" placeholder="00/00/00" name="nom" value={nom} onChange={this.changeHandler} /> </Form> </div>
            <div class="aaafc"> Heure </div>
            <div class="aaafd"> <Form> <Form.Control type="text" placeholder="00h00" name="nom" value={nom} onChange={this.changeHandler} /> </Form> </div>
            <div class="aaafe"> Adresse </div>
            <div class="aaaff"> <Form> <Form.Control type="text" placeholder="37 rue de Paris, Saint-Germain en Laye" name="nom" value={nom} onChange={this.changeHandler} /> </Form> </div>


          </Modal.Body>
          <Modal.Footer>
            <Button onClick={this.submitHandler}>Proposer</Button>
          </Modal.Footer>
        </Modal>

      )
  }

}

function AddMatchModal(props){
  const [modalShow, setModalShow] = React.useState(false);
  return(
      <div class="aaafg">
          <>
            <Button variant="success" onClick={() => setModalShow(true)}> Proposer un nouveau match </Button>

            <MyVerticallyCenteredModal
              show={modalShow}
              fonctionReRender = {props.fonctionReRender}
              onHide={() => setModalShow(false)}
            />
          </>
      </div>
      )
}

export default AddMatchModal;





