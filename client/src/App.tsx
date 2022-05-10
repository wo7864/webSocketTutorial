import React, { useEffect, useMemo, useState } from "react";


function App() {

    const [num, setNum] = useState(0)

    const ws = useMemo(() => {
        const ws = new WebSocket("ws://localhost:8000/ws/")
        ws.onopen = () => {  console.log("connected!!") }
        ws.onmessage = (evt:MessageEvent) => {
            const data = JSON.parse(evt.data)
            setNum(data.num)
        }
        return ws
    }, [])

    const sendMessage = () => {  // 화살표함수로 만들것!!
        const message = JSON.stringify({message:"hello this is client Message"})
        ws.send(message);  // 서버로 메세지 보내는건 send
    }


    return (
        <div className="App">
            <header className="App-header">
                <button onClick={sendMessage}>메세지 보내기</button>
                <span>{num}</span>
            </header>
        </div>
    );
}


export default App;
