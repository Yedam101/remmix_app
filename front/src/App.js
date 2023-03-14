
import { Component } from 'react';

import RegisterPage from './components/TOC';




class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      subject : {title:'WEB', sub:'World Wide Web'},
      ttet : {just:'JUST', test:'TEST'}
    }
  }
  render() {
    return (
      <div className='App'>
        <RegisterPage></RegisterPage>
      </div>
    )
  }
}

export default App;
