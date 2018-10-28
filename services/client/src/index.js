import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import axios from 'axios';
import RatsList from './components/RatsList';

class App extends Component {
  constructor() {
    super();
    this.state = {
        rats: []
    }
  };
  componentDidMount() {
      this.getRats();
  };

  getRats() {
    axios.get(`${process.env.REACT_APP_RATS_SERVICE_URL}/rats`)
    .then((res) => { this.setState({ rats: res.data.data.rats }); })
    .catch((err) => { console.log(err); });
  }

  render() {
    return (
      <section className="section">
        <div className="container">
          <div className="columns">
            <div className="column is-one-third">
              <br/>
              <h1 className="title is-1">All Rats</h1>
              <hr/><br/>
              <RatsList rats={this.state.rats}/>
            </div>
          </div>
        </div>
      </section>
    )
  }
};

ReactDOM.render(
  <App />,
  document.getElementById('root')
);
