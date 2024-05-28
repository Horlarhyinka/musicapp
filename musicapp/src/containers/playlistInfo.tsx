import "../styles/playlist-info.css"

import { Playlist } from "../types/playlist"


interface Prop{
    playlist: Playlist
}

export const PlaylistInfo = (prop: Prop)=>{
    return <div className="playlist-info">
        <h1 className="name">{prop.playlist.name}<span>{prop.playlist.is_public? "Public": "private"}</span></h1>
        <p className="username">{prop.playlist.user.username}</p>
        <p className="description">{prop.playlist.description}</p>
    </div>
}