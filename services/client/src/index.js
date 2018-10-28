import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import axios from 'axios';
import RatsList from './components/RatsList';
import AddRat from './components/AddRat';

class App extends Component {
  constructor() {
    super();
    this.state = {
        rats: [],
        color: '',
        weight: '',
    };
    this.addRat = this.addRat.bind(this);
    this.handleChange = this.handleChange.bind(this);
  };
  componentDidMount() {
      this.getRats();
  };

  getRats() {
    axios.get(`${process.env.REACT_APP_RATS_SERVICE_URL}/rats`)
    .then((res) => { this.setState({ rats: res.data.data.rats }); })
    .catch((err) => { console.log(err); });
  }

  addRat(event) {
    event.preventDefault();
    const data = {
      color: this.state.color,
      weight: this.state.weight
    };
    axios.post(`${process.env.REACT_APP_RATS_SERVICE_URL}/rats`, data)
    .then((res) => {
      this.getRats();
      this.setState({ color: '', weight: '' });
    })
    .catch((err) => { console.log(err); });
  };


  handleChange(event) {
    const obj = {};
    obj[event.target.name] = event.target.value;
    this.setState(obj);
  };


  render() {
    return (
      <section className="section">
        <div className="container">
          <div className="columns">
            <div className="column is-one-third">
              <br/>
              <h1 className="title is-1">All Rats</h1>
              <hr/><br/>
              <AddRat
                color={this.state.color}
                weight={this.state.weight}
                addRat={this.addRat}
                handleChange={this.handleChange}
              />
              <br></br>
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
