import { Playlist } from "../types/playlist"
import "../styles/playlist-card.css"

interface Prop{
    playlist: Playlist
}
export const PlayListCard = (prop: Prop)=>{
    return <div className="playlist-card">
        <p className="name">{prop.playlist.name}</p>
        <p className="username">{prop.playlist.user.username}</p>
    </div>
}