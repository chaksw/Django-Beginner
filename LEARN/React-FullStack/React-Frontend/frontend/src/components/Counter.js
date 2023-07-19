import React, { useState } from "react";

function Counter() {
    // Declare a new state variable
    const [count, setCount] = useState(100);
    return (
        <div>
            <h2>{count}</h2>
            <br></br>
            <button onClick={() => setCount(count + 100)}>Click Plus</button>
            <br></br>
            <br></br>
            <button onClick={() => setCount(count - 100)}>Click Minus</button>
        </div>
    );
}
export default Counter;
