import { RefObject, useRef } from "react"
import "../styles/auth.css"


interface Prop{
    type: "login" | "register"
    handleAuth: Function
    openAuth: Function
}

export const Auth = (prop: Prop) =>{
    const userNameRef = useRef<RefObject<HTMLInputElement>>()!
    const passwordRef = useRef()
    return <form action="" className="auth">
        <h1>{prop.type}</h1>
        <label htmlFor="username" >Username</label>
        <input ref={userNameRef as any} type="text" name="username" />
        <label htmlFor="password">password</label>
        <input ref={passwordRef as any} type="password" name="password" />
        <button onClick={(e)=>{
            e.preventDefault()
            prop.handleAuth(prop.type, )
        }} >{prop.type}</button>
        {
            prop.type === "register"? <span>already have an account? <a onClick={(e)=>{
                e.preventDefault()
                prop.openAuth("login")
            }} href="*" >login</a></span>: <span>dont have an account? <a
            onClick={(e)=>{
                e.preventDefault()
                prop.openAuth("register")
            }}
                href="*">register</a></span>
        }
    </form>
}