import React, {useState} from "react";

const Input = () => {
    const [txtValue, setTextValue] = useState("");

    const onChange = (e) => {
        setTextValue(e.target.value)
    }

    return (
        <div>
            <br/>
            <input type="text" value={txtValue} onChange={onChange}/>
            <p>{txtValue}</p>
        </div>
    )
}

export default Input;