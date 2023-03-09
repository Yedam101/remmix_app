
import { Component } from 'react';

import RegisterPage from './components/TOC';
import Content from './components/Content';




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
        <Content></Content>
      </div>
    )
  }
}

export default App;
