import React from 'react';
import {Button} from 'react-bootstrap'

class ElementMatchPerso extends React.Component {
	constructor(){
		super()
	}

	render() {
		console.log(this.props.infos)




		return(
			<div class="aaacb">
				<Button variant={"primary"}>
					Match référencé {this.props.infos.ref_match}
				</Button>
			</div>
		)
	}
}

export default ElementMatchPerso;
