import H5AudioPlayer from "react-h5-audio-player"
import { Music } from "../types/music"
import 'react-h5-audio-player/lib/styles.css';

interface Prop{
    music: Music
}


export const Player = (prop: Prop)=>{
    return <H5AudioPlayer
        autoPlay
        src={prop.music.url}
        style={{backgroundColor: "black", color: "white", position: "fixed", bottom: "0px", right: "0px", width: "70%"}}
    />
} 

