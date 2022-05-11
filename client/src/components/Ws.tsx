import React, { useEffect, useState } from "react";


function App() {

    const [num, setNum] = useState(-1)


    useEffect(() => {
        const ws = new WebSocket("ws://localhost:8000/ws/1234/")
        ws.onopen = () => { console.log("connected!!") }
        ws.onmessage = (evt: MessageEvent) => {
            const data = JSON.parse(evt.data)
            setNum(data.num)
        }

        let live = true
        const data = { type: 'start' }
        const message = JSON.stringify(data)
        const func = () => {
            setTimeout(() => {
                if (!live) return
                ws.send(message)
                func()
            }, 5000)
        }
        func()

        return () => { live = false; ws.close(); }

    }, [])

    return (
        <div className="App">
            <header className="App-header">
                <span>{num === -1 ? '로딩중입니다.' : num}</span>
            </header>
        </div>
    );
}


export default App;
