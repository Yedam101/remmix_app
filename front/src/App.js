import './App.css';
import { Component } from 'react';

import TOC from './components/TOC';
import Content from './components/Content';
import Subject from './components/Subject';
import Test from './components/Test';


class App extends Component {
  render() {
    return (
      <div className='App'>
        <Subject title='WEB' sub="world wide web"></Subject>
        <Subject title='React' sub="for UI"></Subject>
        <Test just="JUST" test="TEST"></Test>
        <TOC></TOC>
        <Content></Content>
      </div>
    )
  }
}

export default App;
