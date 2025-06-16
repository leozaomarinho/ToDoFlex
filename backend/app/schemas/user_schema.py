from pydantic import BaseModel, EmailStr

# schema base pode ser util para herança
class UserBase(BaseModel):
    username: str
    email: EmailStr


# schema de criação de usuario
class UserCreate(UserBase):
    password: str

# schema de resposta
class UserResponse(UserBase):
    id: int

    class Config:
        from_atributes = True  # Permite que o Pydantic use atributos de classe como campos
        orm_mode = True  # Permite que o Pydantic converta modelos ORM em dicionários