import React, { useEffect, useMemo, useState } from "react";
import Ws from "./components/Ws"
import Sse from "./components/Sse"

type ContentProps = {
    page:String
}

function Content({page}:ContentProps) {
   
    if(page === 'ws')
        return <Ws/>
    else if(page === 'sse')
        return <Sse/>
    else
        return <></>
}


function App(){
    const [page, setPage] = useState('ws')

    return (
        <div>
            <button onClick={()=>setPage('ws')}>ws</button>
            <button onClick={()=>setPage('sse')}>sse</button>
            <Content page={page}/>
        </div>
    )
}


export default App;
