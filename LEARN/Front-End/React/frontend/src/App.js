import logo from "./logo.svg";
import "./App.css";
import Hello from "./components/Hello";
import Counter from "./components/Counter";
// Stateless component [functional component]
function App() {
    return (
        <div>
            <Hello name="Luke Cage!" />
            <Counter />
        </div>
    );
}

export default App;
