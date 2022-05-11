import React, { useEffect, useMemo, useState } from "react";


function Sse() {

    const [num, setNum] = useState(0)
    const [id, setId ] = useState('tt')

    useEffect(() => {
        if(!id) return
        const sseEvents = new EventSource(`http://localhost:8000/events/${id}/`)
        sseEvents.onopen = function () {
            console.log('conn')
            // 연결 됐을 때 
        }
        sseEvents.onerror = function (error) {
            // 에러 났을 때
        }
        sseEvents.onmessage = function (stream) {
            // 메세지 받았을 때
            const parsedData = JSON.parse(stream.data)
            console.log(parsedData)
        }

    }, [id])

    const handleClick = async () => {
        const data = await fetch(`http://localhost:8000/test/${id}/`)
        console.log(data)
    }

    return (
        <div>
            <header>
                <span>sse</span>
            </header>
            <span>{num}</span>
            <input type="text" onBlur={(e) => setId(e.target.value)}/>
            <button onClick={handleClick}>click</button>
        </div>
    );
}


export default Sse;
