import React from 'react';
import {Button} from 'react-bootstrap'

class ElementMatch extends React.Component {
	constructor(){
		super()
	}

	render() {
		console.log(this.props.infos)

		let couleur
		if (this.props.infos.am_i_origin === 1) {couleur = "success"}
		else {couleur = "primary"}


		return(
			<div class="aaadd">
				<Button variant={couleur}>
					<div> {this.props.infos.day} </div>
					<div> {this.props.infos.hour} </div>
					<div> {this.props.infos.nbr_rouge}/5 </div>
					<div> {this.props.infos.nbr_bleu}/5 </div>
				</Button>
			</div>
		)
	}
}

export default ElementMatch;
