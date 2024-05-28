import { User } from "./user"


export interface Playlist{
    name: string
    description: string
    is_public: boolean
    user: User,
    id: number
}