import "../styles/tracks-list.css"

import { TrackCard } from "../components/track-card"
import { Track } from "../types/track"
import { Music } from "../types/music"

interface Prop{
    tracks: Track[],
    playing: Music,
    handleChangeMusic: Function
}

export const TracksList = (prop: Prop)=>{
    return <div className="tracks-list">
        {
            prop.tracks.map(track=>{
                return <TrackCard handleChangeMusic={prop.handleChangeMusic} isPlaying={track.music.id === prop.playing.id} key={track.id} music={track.music} />
            })
        }
    </div>
}