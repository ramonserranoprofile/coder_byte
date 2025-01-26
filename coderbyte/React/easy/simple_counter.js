import React, { useState } from "react";

const Counter = () => {
    const [count, setCount] = useState(0);

    const increment = () => {
        setCount(prevCount => prevCount + 1);
    };

    return (
        <div id="mainArea">
            <p>
                {`Button Count: `}
                <span>{count}</span>
            </p>
            <button onClick={increment} id="mainButton">
                Increase
            </button>
        </div>
    );
};

export default Counter;
// const root = createRoot(document.getElementById("root"));
// root.render(<Counter />);
