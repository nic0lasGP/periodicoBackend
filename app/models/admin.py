from pydantic import BaseModel

class Body(BaseModel):
    subtitulo: str
    contenido_html: str

class PostCreate(BaseModel):
    title: str
    slug: str
    body: Body
    user_id: int
    section_id: int

class PostUpdate(BaseModel):
    post_id: int
    title: str
    slug: str
    body: Body
    user_id: int
    section_id: int