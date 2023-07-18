import React, { Component } from "react";

// function syntax [to create a component]
// function Hello(props) {
//     return <h1>Hello {props.name}</h1>;
// }

// Class based component [ES6 class based]
class Hello extends React.Component {
    render() {
        return <h1>Hello {this.props.name}</h1>;
    }
}

export default Hello;
