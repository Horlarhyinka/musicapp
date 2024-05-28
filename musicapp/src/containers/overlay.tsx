import react from "react"
import "../styles/overlay.css"

interface Prop{
    element: react.JSX.Element
    toggleOverlay: Function
}

export const Overlay: react.FC<Prop> = ({ element, toggleOverlay }) =>{
    return <div id="overlay" 
    onClick={(e: react.MouseEvent<HTMLDivElement>)=>{
        console.log("verlay clicked...", (e.target as HTMLElement).id)
        if((e.target as HTMLElement).id === "overlay"){
            toggleOverlay()
        }
    }}
     className="overlay">
        {
            element
        }
    </div>
}