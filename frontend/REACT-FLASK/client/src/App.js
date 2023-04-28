import React, { useState, useEffect} from 'react'

function App() {

  const [data, setData] = useState([{}])

  useEffect( () => {
        fetch("/songs").then(
            res => res.json()
        ).then(
            data => {
                setData(data)
                console.log(data)
            }
        )
    }, [])

  return (
        <div>
            {(typeof data.songs === 'undefined') ? (
                <p>Loading...</p>
            ) : (
                data.songs.map((songs, i) => (
                    <p key={i}>{songs}</p>
                ))
            )}
        </div>
         
    )
}

export default App

