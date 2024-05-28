import { PlayListCard } from "../components/playlist-card"
import { ProfileCard } from "../components/profile-card"
import { Playlist } from "../types/playlist"

import "../styles/side-bar.css"

interface Props{
    username: string
    active: number
    playlists: Playlist[]
    isAuthenticated: boolean
    toggleAuthOverlay: Function
}

export const SideBar = (props: Props) =>{
    return <div className="side-bar">
        {props.isAuthenticated && <ProfileCard username={props.username} />}
        {props.isAuthenticated?
        <button>new playlist</button>:
        <button onClick={()=>{props.toggleAuthOverlay()}} >login</button>
        }
        <hr></hr>
        <div className="playlists">
            {props.playlists.map(p=><PlayListCard key={p.id} playlist={p} />)}
        </div>
    </div>
}