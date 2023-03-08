import { Component } from "react";

class Test extends Component {
    render() {
      return(
        <div>
          <p>
            {this.props.just}
          </p>
          <p>
            {this.props.test}
          </p>
        </div>
      )
    }
  }
export default Test;