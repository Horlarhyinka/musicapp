import { useState } from "react";
import "../styles/track-card.css"

import { Music } from "../types/music"
import { Icon } from '@iconify/react';

interface Prop{
    music: Music
    isPlaying?: boolean
    handleChangeMusic: Function
}


export const TrackCard = (prop: Prop)=>{
    const play_icn = "fe:play"
    const pause_icn = "basil:pause-solid"
    const [btnOpen, setBtnOpen] = useState<boolean>(false)
    const toggleBtn = ()=>setBtnOpen(!btnOpen)
    return <div className="track-card">
        {/* <img src={prop.music.cover} alt={prop.music.name} /> */}
        <div style={{backgroundImage: `url('${prop.music.cover}')`}} className="cover">
            {
                prop.isPlaying && <div className="mini-player default">
                    <Icon className="icn" icon="fluent:speaker-2-48-regular"  style={{color: "white"}} />
                   </div>
            } 
        <div onClick={()=>{prop.handleChangeMusic(prop.music)}} className="mini-player pause-play">
            <Icon className="icn pause-play" icon={prop.isPlaying?pause_icn: play_icn}  style={{color: "white"}} />
        </div>
            
                
        </div>
        <div className="wrapper">
            <p className="name">{prop.music.name}</p>
            <p className="artist">{prop.music.artist}</p>
        </div>
        {btnOpen && <div className="remove-add-btn" >remove from playlist</div>}
        <Icon onClick={()=>{
            toggleBtn()
        }} className="menu-icn" icon="charm:menu-kebab"  style={{color: "white"}} />

    </div>
}