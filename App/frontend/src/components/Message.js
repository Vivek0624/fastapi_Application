import React, { useState, useEffect } from 'react'
import axios from 'axios';



export default function Message() {
    const [result, setResult] = useState({});


    const message = async () => {
        try {
            let res = await axios.get(`${process.env.REACT_APP_URL}:${parseInt(process.env.REACT_APP_PORT)}`)
            let result = res.data;
            console.log(result)
            setResult(result);
        } catch(error) {
            console.log(error)
        }   
    }

    useEffect(() => {
        message()
        console.log(`${process.env.REACT_APP_URL}:${parseInt(process.env.REACT_APP_PORT)}}`)
        // console.log(parseInt(process.env.REACT_APP_PORT))
    },[])


  return (
    <div>
    {/* {result.map(item => <div>{item.message}</div>)}         */}
        {/* Hello */}
        {result.message}
    </div>
  )
}
