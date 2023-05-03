// https://www.youtube.com/watch?v=EcRFYF4B3IQ
import React, { useState, useEffect} from 'react'

function App() {
    const [userInput, setUserInput] = useState('')
    const [output, setOutput] = useState([{}])
    
    const handleSubmit = (e) => {
        e.preventDefault();
        const submittedSong = {userInput}
        console.log({submittedSong})
    }

  useEffect( () => {
        fetch("/songs").then(
            res => res.json()
        ).then(
            output => {
                setOutput(output)
                console.log(output)
            }
        )
    }, [])

  return (
    //   
        <div>


        <h1 align="center">Tired of your current playlist?</h1>
        <p align="center">[      ]</p>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    required
                    value={userInput}
                    onChange={(e) => setUserInput(e.target.value)}
                />
            </form>
            {/* <p>{userInput}</p> */}



            {(typeof output.songs === 'undefined') ? (
                <p>Loading...</p>
            ) : (
                output.songs.map((songs, i) => (
                    <p key={i}>{songs}</p>
                ))
            )}
        </div>
         
    )
}

export default App

