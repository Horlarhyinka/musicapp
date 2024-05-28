import "../styles/profile-card.css"

interface Prop{
    username: string
}
export const ProfileCard = (prop: Prop)=>{

    return <div className="profile-card">
        <span>{prop.username[0].toUpperCase()}</span>
        <h4>{prop.username}</h4>
    </div>
}