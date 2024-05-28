import { useState } from "react"
import "./App.css"
import playlists from "./assets/playlists"
import tracks from "./assets/tracks"
import { Player } from "./components/player"
import { PlaylistInfo } from "./containers/playlistInfo"
import { SideBar } from "./containers/sidebar"
import { TracksList } from "./containers/tracksList"
import { Music } from "./types/music"
import { Overlay } from "./containers/overlay"
import { Auth } from "./containers/auth"
import axios from "axios"

const api_url = "http://localhost:8000/api/"

function App() {

  type AuthType = "login" | "register"

  const [playing, setplaying] = useState<Music>(tracks[0].music)
  const [authOverLayOpen, setAuthOverlayOpen] = useState<boolean>(false)
  const [authType, setAuthType] = useState<AuthType>("login")

  function toggleAuthOverLay(){
    return setAuthOverlayOpen(!authOverLayOpen)
  }

  function openAuthOverLay(type: AuthType){
    setAuthType(type)
    return setAuthOverlayOpen(true)
  }

  function handleChangeMusic(music: Music){
    setplaying(music)
  }

  function handleAuth(type: AuthType, data: {username?: string, password?: string}){
    if(!data.username || !data.password){
      alert("username and password is required.")
    }
    if(type=="register"){
      const url = api_url + "auth/users/"
      axios.post(url, data)
      .then((res)=>{
        console.log(res.data)
        if(res.status !== 201){
          alert("authentication failed")
        }else{
          openAuthOverLay("login")
        }

      })
    }else{

    }
  }

  const [isAuthenticated, setIsAuthenticated] = useState<boolean>(false)

  return (
    <>
    {authOverLayOpen && <Overlay toggleOverlay={toggleAuthOverLay} element={<Auth handleAuth={handleAuth} type={authType} openAuth={openAuthOverLay} />} />}
    <SideBar isAuthenticated={isAuthenticated} toggleAuthOverlay={toggleAuthOverLay} username="Horlarh" active={1} playlists={playlists} />
    <div className="content">
      <PlaylistInfo playlist={playlists[0]} />
      <TracksList handleChangeMusic={handleChangeMusic} playing={playing} tracks={tracks} />
      <Player music={playing} />
    </div>

    </>
  )
}

export default App
