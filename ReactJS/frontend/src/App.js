import React from "react";

class App extends React.Component {
  state = {
    names: [
      'john',
      'Akashy',
      'sunil',
      'Hardik',
      'virat'
    ],
    searchTerm: ''
  }

  editSearch = (e) => {
    this.setState({searchTerm: e.target.value })
  }
  dynamicSearch = () => {
    return this.state.names.filter( name => name.toLowerCase().includ(this.state.searchTerm.toLowerCase()))

  }

  render() {
    return (
      <div style = {{textAlign: 'center', paddingTop: '30vh'}}>
        <input type= 'text' value = {this.state.searchTerm} onChange = {this.editSearchTerm} placeholder = 'search for name'/>
        <br></br>
        <h3>These are important names: </h3>
        <NamesContainer names = { this.dynamicSearch()} />+
      </div>
    );
  }
}

class NamesConatiner extends Component {
  render() {
    return (
      <div>
        {this.props.names.map(name => <Name name = { name } />)}
      </div>
    )
  }
}

class Name extends Component {
  render() {
    return (
      <div>
        {this.props.name}
      </div>
    )
  }
}